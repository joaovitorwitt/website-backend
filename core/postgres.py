

from typing import Any

import psycopg
import settings

from core.utils import mount_response_dict
from core.string import format_title_for_url

from core.log import Log

logger = Log('database-instance')
class PostgresConnection:

    def __init__(self, name: str, user: str = None, password: str = None, port: int = None, **kwargs) -> None:
        self.name = name
        self.user = user
        self.password = password
        self.port = port

        self.kwargs = kwargs

        if self.user is None:
            self.user = settings.DEFAULT_POSTGRES_USER

        if self.password is None:
            self.password = settings.DEFAULT_POSTGRES_PASSWORD

        if self.port is None:
            self.port = settings.DEFAULT_POSTGRES_PORT


    def connect(self):
        conn = psycopg.connect(dbname=self.name, user=self.user, password=self.password, port=self.port)
        return conn

    def insert(self, table: str, **kwargs: dict) -> Any:
        conn = self.connect()

        cur = conn.cursor()

        if table == 'Articles':
            cur.execute(
                f'INSERT INTO "{table}" ("UUID", "Title", "Description", "created_at", "date", "Content", "image_url", "url_title") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (kwargs['id'], kwargs['title'], kwargs['description'], kwargs['created_at'], kwargs['date'], kwargs['content'], kwargs['image_url'], kwargs['url_title'])
            )

        if table == 'Projects':
            cur.execute(
                f'INSERT INTO "{table}" ("UUID", "Title", "Description", "created_at", "date", "project_link", "image_url", "url_title") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (kwargs['id'], kwargs['title'], kwargs['description'], kwargs['created_at'], kwargs['date'], kwargs['project_link'], kwargs['image_url'], kwargs['url_title'])
            )

        conn.commit()
        cur.close()
        conn.close()


    def retrieve_all(self, table: str, **kwargs: dict) -> Any: # pylint: disable=unused-argument
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(f'SELECT * FROM "{table}"')

        rows = cur.fetchall()
        columns = [row[0] for row in cur.description]

        cur.close()
        conn.close()

        data = mount_response_dict(rows, columns)

        return data

    def retrieve_single(self, table: str, **kwargs: dict) -> Any:
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(f'SELECT * FROM "{table}" WHERE id = {kwargs["id"]}')

        rows = cur.fetchall()
        columns = [row[0] for row in cur.description]

        cur.close()
        conn.close()

        data = mount_response_dict(rows, columns)
        return data

    def delete(self, table: str, **kwargs: dict) -> None:
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(f'DELETE FROM "{table}" WHERE id = {kwargs["id"]}')

        conn.commit()
        cur.close()
        conn.close()


    def update(self, table: str, **kwargs: dict) -> Any:
        conn = self.connect()
        cur = conn.cursor()

        if kwargs['content'] is not None:
            cur.execute(f"UPDATE \"{table}\" SET \"Content\" = '{kwargs['content']}' WHERE id = {kwargs['id']}")

        if kwargs['title'] is not None:
            cur.execute(f"UPDATE \"{table}\" SET \"Title\" = '{kwargs['title']}' WHERE id = {kwargs['id']}")
            new_url_title = format_title_for_url(kwargs['title'])
            cur.execute(f"UPDATE \"{table}\" SET \"url_title\" = '{new_url_title}' WHERE id = {kwargs['id']}")

        if kwargs['description'] is not None:
            cur.execute(f"UPDATE \"{table}\" SET \"Description\" = '{kwargs['description']}' WHERE id = {kwargs['id']}")

        if kwargs['image_url'] is not None:
            cur.execute(f"UPDATE \"{table}\" SET \"image_url\" = '{kwargs['image_url']}' WHERE id = {kwargs['id']}")


        conn.commit()
        cur.close()
        conn.close()
