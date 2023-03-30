from globals import PROMPTS, MONTHS
from window import Window
from utils import clear_terminal, throw_error, repeating_prompt

from datetime import datetime
from typing import List
from data_types import QueryBody, UserResponse, TripResponse, TimeResponse
from parse import Parser

import threading
import os
import math
from time import sleep

import difflib
import numpy as np
from pandas import DataFrame

global query_body
query_body: QueryBody = {
    'city': '',
    'filter': '',
    'month': '',
    'day': ''
}


def query(window_content: List[str], prompt: str, key: str):
    """
    Query the user for input for a specific key in the query_body dictionary

    Args:
        window_content (List[str]): List of strings to display in the window
        prompt (str): Prompt to display to the user
        key (str): Key to update in the query_body dictionary

    """
    clear_terminal()

    win = Window(80)

    try:
        win = Window(os.get_terminal_size().columns - 2)
    except OSError:
        win = Window(80)

    while query_body[key] not in PROMPTS[key]:
        win.create(window_content)

        res = input(prompt)
        closest_match = difflib.get_close_matches(res, PROMPTS[key], 1, 0.5)

        if len(closest_match) == 0:
            throw_error()
        else:
            query_body[key] = closest_match[0]
            break


def query_page():
    """
    Query the user for input for the query_body dictionary
    """

    query(
        ['Hi there!',
         'Let\'s look at some US bike-share data!',
         'Would you like to see data for Chicago, New York, or Washington?'
         ],
        'Please type the name of the city you would like to see data for: ',
        'city'
    )

    query(
        ['Would you like to filter the data by month, day, or not at all?'],
        'Please type the name of the filter you would like to use (none for not at all): ',
        'filter'
    )

    if query_body['filter'] == 'Month' or query_body['filter'] == 'Both':
        query(
            ['Which month - Jan, Feb, Mar, Apr, May, or Jun?'],
            'Please type the name of the month you would like to see data for: ',
            'month'
        )

    if query_body['filter'] == 'Day' or query_body['filter'] == 'Both':
        query(
            ['Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?'],
            'Please type the name of the day you would like to see data for: ',
            'day'
        )


def time_section(win: Window, time: TimeResponse):
    win.create(['Time Information [Busiest Periods]'])

    win.create_stacked([
        [
            f'Hour: {time["hour"]["value"]}',
            f'{time["hour"]["count"]} users'
        ],
        [
            f'Day: {time["day"]["value"]}',
            f'{time["day"]["count"]} users'
        ] if time['day'] is not None else [],
        [
            f'Month: {MONTHS[time["month"]["value"] - 1]}',
            f'{time["month"]["count"]} users'
        ] if time['month'] is not None else [],
    ])


def trip_section(win: Window, trip: TripResponse):
    win.create(['Trip Information'])

    win.create([
        'Most popular trip:',
        trip['full_trip'],
        f'{trip["count"]} users'
    ])

    win.create([
        f'Most popular start station: {trip["station"]["start"]["value"]}',
        f'{trip["station"]["start"]["count"]} users',
    ])
    win.create([
        f'Most popular end station: {trip["station"]["end"]["value"]}',
        f'{trip["station"]["end"]["count"]} users',
    ])

    win.create_stacked([
        [
            f'Total days ridden: {round(float(trip["duration"]["total"]) / 86400)} days',
        ],
        [
            f'Average trip duration: {int(trip["duration"]["avg"] / 60)} minutes',
        ]
    ])


def user_section(win: Window, user: UserResponse):
    win.create(['User Information'])

    win.create_stacked([
        [
            f'Total subscribers: {user["type"]["subscriber"]}',
            f'{round(user["type"]["subscriber"] / user["total"] * 100)}%'
        ],
        [
            f'Total customers: {user["type"]["customer"]}',
            f'{round(user["type"]["customer"] / user["total"] * 100)}%'
        ]
    ])

    has_gender_data = user.get('gender') is not None
    has_birth_data = user.get('birth') is not None

    if has_gender_data:
        win.create_stacked([
            [
                'Male users:',
                f'{user["gender"]["male"]}'
            ],
            [
                'Female users',
                f'{user["gender"]["female"]}',
            ],
        ])

    if has_birth_data:
        win.create_stacked([
            [
                'Youngest user:',
                f'{round(datetime.now().year - user["birth"]["latest"])}'
            ],
            [
                'Oldest user',
                f'{round(datetime.now().year - user["birth"]["earliest"])}',
            ],
            [
                'Most common user age',
                f'{round(datetime.now().year - user["birth"]["mode"])}',
            ]
        ])


def results_page(time: TimeResponse, trip: TripResponse, user: UserResponse):
    """
    Display the results of the query to the user

    Args:
        time (TimeResponse): Time response from the parser
        trip (TripResponse): Trip response from the parser
        user (UserResponse): User response from the parser

    """

    clear_terminal()

    win = Window(80)

    try:
        win = Window(os.get_terminal_size().columns - 2)
    except OSError:
        win = Window(80)

    time_section(win, time)
    trip_section(win, trip)
    user_section(win, user)


def raw_data_page(win: Window, raw: DataFrame):
    """
    Display the raw data to the user

    Args:
        win (Window): Window object
        raw (DataFrame): Raw data from the parser

    """

    headers = np.array(raw.columns)[:, np.newaxis][1:-1]
    items = np.array(raw.values)[:, 1:-1].astype(str)

    thirds = math.ceil(len(headers) / 3)

    win.create(['Raw Data'])

    for i in range(0, thirds):
        win.create_stacked(headers[i * 3:3 + (i * 3)])
        segment = items[:, i * 3:3 + (i * 3)].transpose()
        win.create_stacked(segment)

    pass


def main():
    """
    Main function
    """

    global query_body
    is_repeating = True
    viewing_raw = True

    head = 0
    tail = 5

    parser = Parser()

    _win = Window(80)

    try:
        _win = Window(os.get_terminal_size().columns - 2)
    except OSError:
        _win = Window(80)

    while is_repeating:
        query_page()
        parser.load_data(query_body)

        _time = parser.get_time_info()
        _trip = parser.get_trip_info()
        _user = parser.get_user_info()

        results_page(_time, _trip, _user)

        sleep(3)

        while viewing_raw:
            clear_terminal()
            _raw = parser.get_raw_data(head, tail)
            raw_data_page(_win, _raw)
            viewing_raw = repeating_prompt(_win, 'Would you like to view more raw data?')
            if viewing_raw:
                head += 5
                tail += 5

        is_repeating = repeating_prompt(_win, 'Would you like to restart?')
        if is_repeating:
            query_body = {
                'city': '',
                'filter': '',
                'month': '',
                'day': '',
            }

    clear_terminal()
    _win.create(['Goodbye!'])


if __name__ == '__main__':
    main()
