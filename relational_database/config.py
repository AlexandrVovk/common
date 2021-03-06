import os

DATABASE = {
    "database": "cursor_db",
    "user": "cursor",
    "password": "12345",
    "port": 5432
}

TEST_DATABASE = {
    "database": "test_cursor_db",
    "user": "test_cursor",
    "password": "test",
    "port": 5432
}

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

FIXTURES_PATH = os.path.join(PROJECT_PATH, "fixtures")
