import threading
import pandas as pd
from typing import Optional
from operator import attrgetter
from fastapi import APIRouter

from api_types import QueryBody, StatusResponse, \
    TimeResponse, TripResponse, UserResponse


class Router:
    """Router class for the API

    Attributes:
        router (APIRouter): FastAPI router object
        df (Optional[pd.DataFrame]): Pandas dataframe containing the loaded data
        date_unfiltered_df (Optional[pd.DataFrame]): Pandas dataframe without date filters

    TODO:
        * Make class into a singleton
        * Threading for data loading and api endpoint resolution [?]

    """

    df: Optional[pd.DataFrame]
    date_unfiltered_df: Optional[pd.DataFrame]

    def __init__(self):

        self.router = APIRouter()
        self.df = None
        self.date_unfiltered_df = None

        self.filtered_by_month = False
        self.filtered_by_day = False

        self.router.add_api_route('/load', self.load_data, methods=['POST'])

        self.router.add_api_route('/get_time', self.get_time_info, methods=['GET'])
        self.router.add_api_route('/get_trip', self.get_trip_info, methods=['GET'])
        self.router.add_api_route('/get_user', self.get_user_info, methods=['GET'])
        self.router.add_api_route('/ok', self.get_api_status, methods=['GET'])

    def get_api_status(self) -> StatusResponse:
        """
        API endpoint to check if the API is loaded

        Returns:
            StatusResponse: Response object containing status code and message
        """

        return {
            'code': 200,
            'status': 'OK'
        }

    def load_data(self, query: QueryBody) -> StatusResponse:
        """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            query (QueryBody): Object containing data loading parameters

        Returns:
            StatusResponse: Response object containing status code and message
        """

        city, month, day = attrgetter('city', 'month', 'day')(query)

        CITY_MAP = {
            'Chicago': 'chicago.csv',
            'New York City': 'new_york_city.csv',
            'Washington': 'washington.csv',
        }

        selected_city = CITY_MAP[city]

        df = pd.read_csv(selected_city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour
        df['day_of_week'] = df['Start Time'].dt.day_name()
        df['month'] = df['Start Time'].dt.month
        df['trip'] = df['Start Station'] + ' - ' + df['End Station']

        self.filtered_by_month = month != 0
        self.filtered_by_day = day != ''

        self.date_unfiltered_df = df.copy(True)

        df = df[df['month'] == month] if self.filtered_by_month else df
        df = df[df['day_of_week'] == day] if self.filtered_by_day else df

        self.df = df

        return {
            'code': 200,
            'status': 'OK'
        }

    def get_time_info(self) -> TimeResponse:
        """
        API endpoint to get time info

        Returns:
            TimeResponse: Response object containing most popular hour, day and month
        """
        popular_month = self.df['month'].mode()[0] if not self.filtered_by_month else None
        popular_day = self.df['day_of_week'].mode()[0] if not self.filtered_by_day else None
        popular_hour = self.df['hour'].mode()[0]

        month_count = self.df['month'].value_counts()[popular_month] if not self.filtered_by_month else None
        day_count = self.df['day_of_week'].value_counts()[popular_day] if not self.filtered_by_day else None
        hour_count = self.df['hour'].value_counts()[popular_hour]

        res = {
            'month': {
                'value': popular_month.item(),
                'count': month_count.item()
            } if not self.filtered_by_month else None,
            'day': {
                'value': popular_day,
                'count': day_count.item()
            } if not self.filtered_by_day else None,
            'hour': {
                'value': popular_hour.item(),
                'count': hour_count.item()
            }
        }

        return res

    def get_trip_info(self) -> TripResponse:
        """
        API endpoint to get trip info

        Returns:
            TripResponse: Response object containing most popular trip, duration and stations
        """

        start_station = self.df['Start Station'].mode()[0]
        count_start_station = self.df['Start Station'].value_counts()[start_station]

        end_station = self.df['End Station'].mode()[0]
        count_end_station = self.df['End Station'].value_counts()[end_station]

        trip = self.df['trip'].mode()[0]
        count_trip = self.df['trip'].value_counts()[trip]

        total_duration = self.df['Trip Duration'].sum()
        avg_duration = self.df['Trip Duration'].mean()

        res = {
            'duration': {
                'total': total_duration.item(),
                'avg': avg_duration.item()
            },
            'station': {
                'start': {
                    'value': start_station,
                    'count': count_start_station.item()
                },
                'end': {
                    'value': end_station,
                    'count': count_end_station.item()
                },
            },
            'full_trip': trip,
            'count': count_trip.item()
        }

        return res

    def get_user_info(self) -> UserResponse:
        """
        API endpoint to get user info

        Returns:
            UserResponse: Response object containing minimally user types, and also gender and birth year if available
        """

        subscriber, customer, *_ = self.date_unfiltered_df['User Type'].value_counts()
        has_gender_data = 'Gender' in self.date_unfiltered_df
        has_birth_data = 'Birth Year' in self.date_unfiltered_df

        if not has_birth_data and not has_gender_data:
            return {
                'type': {
                    'subscriber': subscriber,
                    'customer': customer
                },
            }

        male, female = self.date_unfiltered_df['Gender'].value_counts()
        earliest_year = self.date_unfiltered_df['Birth Year'].min()
        recent_year = self.date_unfiltered_df['Birth Year'].max()
        common_year = self.date_unfiltered_df['Birth Year'].mode()[0]

        res = {
            'type': {
                'subscriber': subscriber,
                'customer': customer,
            },
            'gender': {
                'male': male,
                'female': female,
            },
            'birth': {
                'earliest': earliest_year,
                'latest': recent_year,
                'mode': common_year,
            },
        }

        return res
