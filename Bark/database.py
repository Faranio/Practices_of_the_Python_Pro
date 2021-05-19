import sqlite3


class DatabaseManager:
    def __init__(self, database_filename):
        self.connection = sqlite3.connect(database_filename)

    def _execute(self, statement, values=None):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor

    def _create_placeholders(self, data):
        return [f'{column} = ?' for column in data.keys()]

    def create_table(self, table_name, columns):
        columns_with_types = [f'{column_name} {data_type}' for column_name, data_type in columns.items()]
        statement = f'''CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_with_types)});'''
        self._execute(statement)

    def add(self, table_name, data):
        placeholders = ', '.join('?' * len(data))
        column_names = ', '.join(data.keys())
        column_values = tuple(data.values())
        statement = f'''INSERT INTO {table_name} ({column_names}) VALUES ({placeholders});'''
        self._execute(statement, column_values)

    def update(self, table_name, criteria, data):
        update_placeholders = ' AND '.join(self._create_placeholders(criteria))
        data_placeholders = ', '.join(self._create_placeholders(data))
        values = tuple(data.values()) + tuple(criteria.values())
        statement = f'''UPDATE {table_name} SET {data_placeholders} WHERE {update_placeholders}'''
        self._execute(statement, values)

    def delete(self, table_name, criteria):
        placeholders = self._create_placeholders(criteria)
        delete_criteria = ' AND '.join(placeholders)
        criteria_values = tuple(criteria.values())
        statement = f'''DELETE FROM {table_name} WHERE {delete_criteria};'''
        self._execute(statement, criteria_values)

    def select(self, table_name, criteria=None, order_by=None):
        statement = f'''SELECT * FROM {table_name}'''

        if criteria:
            criteria_values = tuple(criteria.values())
            placeholders = self._create_placeholders(criteria)
            select_criteria = ' AND '.join(placeholders)
            statement += f''' WHERE {select_criteria}'''
        else:
            criteria_values = None

        if order_by:
            statement += f''' ORDER BY {order_by}'''

        return self._execute(statement, criteria_values)

    def __del__(self):
        self.connection.close()
