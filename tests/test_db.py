

# import pytest
from page_analyzer.db import get_all_urls
# import os
# from pytest_postgresql import factories




# def test_example_postgres(postgresql):
#     """Check main postgresql fixture."""
#     with postgresql.cursor() as cur:
#         cur.execute('CREATE TABLE urls (id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, name varchar(255) UNIQUE, created_at timestamp NOT NULL);')
#         cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#     postgresql.commit()
#
#
# def test_get_all_urls(postgresql):
#     # Set the DATABASE_URL environment variable to the temporary database connection string
#     # os.environ['DATABASE_URL'] = database
#
#     # Insert some rows into the urls and url_checks tables
#     # conn = connect(postgresql)
#     with postgresql.cursor() as cur:
#         cur.execute('CREATE TABLE urls (id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, name varchar(255) UNIQUE, created_at timestamp NOT NULL);')
#
#         cur.execute('CREATE TABLE url_checks (id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, url_id int REFERENCES urls (id), status_code int, h1 varchar(255), title varchar(255), description varchar(255), created_at timestamp NOT NULL);')
#
#         cur.execute("INSERT INTO urls (name, created_at) VALUES ('URL 1', '2022-01-01')")
#         cur.execute("INSERT INTO url_checks (url_id, created_at, status_code) VALUES (1, '2022-01-01', 200)")
#         cur.execute("INSERT INTO url_checks (url_id, created_at, status_code) VALUES (1, '2022-01-02', 200)")
#         cur.execute("INSERT INTO urls (name, created_at) VALUES ('URL 2', '2022-01-03')")
#         cur.execute("INSERT INTO url_checks (url_id, created_at, status_code) VALUES (2, '2022-01-03', 404)")
#         cur.execute("INSERT INTO url_checks (url_id, created_at, status_code) VALUES (2, '2022-01-04', 200)")
#     postgresql.commit()
#     # conn.close()
#
#     # Call the get_all_urls function
#     result = get_all_urls()
#
#     # Assert that the function returns the expected result
#     assert result == [
#         {'id': 1, 'name': 'URL 1', 'last_check': '2022-01-02', 'status_code': 200},
#         {'id': 2, 'name': 'URL 2', 'last_check': '2022-01-04', 'status_code': 200}
#     ]


# from psycopg2 import connect
import unittest.mock
import psycopg2


def test_get_all_urls(monkeypatch):
    # Create a mock cursor object
    mock_cursor = unittest.mock.MagicMock(cursor_factory=psycopg2.extras.RealDictCursor)
    mock_cursor.fetchall.return_value = [
        {'id': 1, 'name': 'URL 1', 'last_check': '2022-01-02', 'status_code': 200},
        {'id': 2, 'name': 'URL 2', 'last_check': '2022-01-04', 'status_code': 200}
    ]

    # Create a mock connection object
    mock_conn = unittest.mock.MagicMock(psycopg2.connect)
    mock_conn.cursor.side_effect = mock_cursor

    # Patch the connect function to return the mock connection object
    monkeypatch.setattr(psycopg2, 'connect', mock_conn)

    # Call the get_all_urls function
    result = get_all_urls()

    # Assert that the function returns the expected result
    assert result == [
        {'id': 1, 'name': 'URL 1', 'last_check': '2022-01-02', 'status_code': 200},
        {'id': 2, 'name': 'URL 2', 'last_check': '2022-01-04', 'status_code': 200}
    ]

    # Assert that the mock cursor object's execute method was called
    mock_cursor.execute.assert_called_once()

    # Assert that the mock connection object's close method was called
    mock_conn.close.assert_called_once()

