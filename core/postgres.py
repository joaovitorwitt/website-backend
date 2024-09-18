

import psycopg
import settings



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

    def insert(self, table: str, **kwargs):
        conn = self.connect()
    
        cur = conn.cursor()
        
        cur.execute(
            'INSERT INTO "Articles" ("UUID", "Title", "Description", "created_at", "date", "Content", "image_url", "url_title") VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (kwargs['id'], kwargs['title'], kwargs['description'], kwargs['created_at'], kwargs['date'], kwargs['content'], kwargs['image_url'], kwargs['url_title'])
        )
        conn.commit()
        cur.close()
        conn.close()
    