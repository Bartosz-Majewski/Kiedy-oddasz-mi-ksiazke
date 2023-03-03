"""Tests for methods from borowers.py"""
import sqlite3
import pytest
from borowers import get_borowers_by_return_date


@pytest.fixture
def create_connection():
    """test if the database was created correctly"""
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE borows(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        name TEXT,
        book_title TEXT,
        book_return_at DATA)''')

    sample_data = [
        (1, 'adam@mail.com', 'Adam', 'Biblia Excela', '2020-11-12'),
        (2, 'kacper@mail.com', 'Kacper', 'Atlas anatomiczny', '2020-12-13'),
        (3, 'alina@mail.com', 'Alina', 'Programowanie w Pythonie', '2019-11-11')
    ]

    cursor.executemany('INSERT INTO borows VALUES (?, ?, ?, ?)', sample_data)
    return connection


def test_borowers(create_connection):
    """test if it fetches data from the database correctly"""
    borowers = get_borowers_by_return_date(create_connection, '2020-12-12')
    assert len(borowers) == 2
    assert borowers[0].name == 'Adam'
    assert borowers[1].name == 'Alina'
