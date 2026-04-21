

import logging

import psycopg
import settings

from core.utils import mount_response_dict


log = logging.getLogger(__name__)


class PostgresConnection:

    def __init__(self, name: str = None, user: str = None, password: str = None, port: int = None, host: str = None, **kwargs) -> None:
        self.name = name or settings.DEFAULT_POSTGRES_DB
        self.user = user or settings.DEFAULT_POSTGRES_USER
        self.password = password or settings.DEFAULT_POSTGRES_PASSWORD
        self.port = port or settings.DEFAULT_POSTGRES_PORT
        self.host = host or settings.DEFAULT_POSTGRES_HOST

        self.kwargs = kwargs


    def connect(self):
        """
        Creates the postgres connection
        """
        conn = psycopg.connect(dbname=self.name, user=self.user, password=self.password, port=self.port, host=self.host)
        return conn

    def insert(self, table: str, **kwargs: dict) -> None:
        conn = self.connect()

        cur = conn.cursor()

        if table == 'Articles':
            cur.execute(
                f'INSERT INTO "{table}" ("UUID", "Title", "Description", "created_at", "date", "Content", "image_url", "url_title") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (kwargs['id'], kwargs['title'], kwargs['description'], kwargs['created_at'], kwargs['date'], kwargs['content'], kwargs['image_url'], kwargs['url_title'])
            )

        if table == 'Projects':
            cur.execute(
                f'INSERT INTO "{table}" ("UUID", "Title", "Description", "created_at", "date", "Content", "image_url", "url_title") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (kwargs['id'], kwargs['title'], kwargs['description'], kwargs['created_at'], kwargs['date'], kwargs['content'], kwargs['image_url'], kwargs['url_title'])
            )

        conn.commit()
        cur.close()
        conn.close()


    def retrieve_all(self, table: str, **kwargs: dict) -> dict: # pylint: disable=unused-argument
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(f'SELECT * FROM "{table}"')

        rows = cur.fetchall()
        columns = [row[0] for row in cur.description]

        cur.close()
        conn.close()

        data = mount_response_dict(rows, columns)

        return data

    def retrieve_single(self, table: str, **kwargs: dict) -> list:
        conn = self.connect()
        cur = conn.cursor()

        cur.execute(f'SELECT * FROM "{table}" WHERE id = {kwargs["id"]}')

        rows = cur.fetchall()
        columns = [row[0] for row in cur.description]

        cur.close()
        conn.close()

        data = mount_response_dict(rows, columns)
        return data
    
    # TODO: adapt this method to the code, remove the other two since there was
    # duplicated code, now i added a flag to check if we should retrieve all
    # the instances of just a single based on the id
    def retrieve(self, table: str, type: str = 'all', **kwargs: dict) -> list:
        conn = self.connect()
        cur = conn.cursor()

        if type == 'all':
            cur.execute(f'SELECT * FROM "{table}"')
        else:
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
