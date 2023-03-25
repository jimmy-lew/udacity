import time
import threading
import pandas as pd
from typing import Optional
import numpy as np
from fastapi import APIRouter

from model_types import QueryBody, TimeResponse, TripResponse, UserResponse, QueryResponse


class Router:

    df: Optional[pd.DataFrame]

    def __init__(self):

        self.router = APIRouter()
        self.df = None
        self.router.add_api_route('/get_time', self.get_time_info, methods=['POST'])

    def load(self, query: QueryBody):
        """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (QueryBody) query - contains:
                (str) city - name of the city to analyze
                (str) filter - type of filter, either month, day, both or none
                (str) month - name of the month to filter by, or "all" to apply no month filter
                (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """

        city, _, month, day = query

        CITY_MAP = {
            'Chicago': 'chicago.csv',
            'New York City': 'new_york_city.csv',
            'Washington': 'washington.csv',
        }

        selected_city = CITY_MAP[city]

        df = pd.read_csv(selected_city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['hour'] = df['Start Time'].dt.hour

        self.df = df

        pass

    def get_time_info(self) -> TimeResponse:
        pass

    def get_trip_info(self) -> TripResponse:
        pass

    def get_user_info(self) -> UserResponse:
        pass

    def get(self) -> QueryResponse:
        return None
