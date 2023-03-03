"""Context manager for database"""
import sqlite3


class Database:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        # sprawdzamy czy cos jest danego typu
        # sprawdzamy czy exc_value jest Exception
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()
