"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv
import os


class PostgresData:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="north",
            user="postgres",
            password=os.getenv("DB_PASSWORD")
        )
        self.cur = self.conn.cursor()
        self.csv_data = ["customers_data", "employees_data", "orders_data"]

    @staticmethod
    def get_csv_data(file_name):
        """ Получаем данные из файлов формата .csv """

        csv_file = open(f"north_data/{file_name}.csv", "r", encoding="utf-8", newline="")
        return csv.reader(csv_file, delimiter=",", quotechar='"')

    def write_to_database(self, database):
        """ Записываем данные в базу данных """

        database_name = database.split("_")[0]
        csv_data = self.get_csv_data(database)

        with self.conn as conn:
            with conn.cursor() as cur:
                next(csv_data)
                for items in csv_data:
                    row = []
                    for item in items:
                        if len(item) == 1:
                            row.append(item)
                        elif len(item) > 1:
                            row.append("'" + str(item.replace("'", "`")) + "'")

                    cur.execute(f"""INSERT INTO {database_name} VALUES
({(', '.join(row))});""")

        cur.close()

    def main_function(self):
        counter = 1
        for database in self.csv_data:
            self.write_to_database(database)
            print(f"{counter}")
            counter += 1



pg = PostgresData()
pg.main_function()
