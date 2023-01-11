import psycopg
import psycopg2
from config import DatabaseConfig
from psycopg.rows import dict_row
from psycopg2.extras import RealDictCursor


class BasePgDriver:

    def get_default_row_factory(self): ...

    def __init__(self,
                 db_dsn: str = None,
                 db_name: str = DatabaseConfig.DB_NAME,
                 db_user: str = DatabaseConfig.DB_USER,
                 db_host: str = DatabaseConfig.DB_HOST,
                 db_port: str = DatabaseConfig.DB_PORT,
                 db_password: str = DatabaseConfig.DB_PASSWORD,
                 row_factory: callable = None
                 ) -> object:
        """   """
        self._db_name = db_name
        self._db_password = db_password
        self._db_user = db_user
        self._db_host = db_host
        self._db_port = db_port
        self._dsn = db_dsn
        if row_factory:
            self._row_factory = row_factory

        if any([self._db_name, self._db_password, self._db_port, self._db_user, self._db_host]):
            if self._dsn is not None:
                raise ValueError("Если заполняется DSN, остальные поля должны быть пустыми")
            if not all([self._db_name, self._db_password, self._db_port, self._db_user, self._db_host]):
                raise ValueError("В драйвере заполнены не все поля для подключения к БД")
            self._dsn = f"postgresql://{self._db_user}:{self._db_password}@{self._db_host}:{self._db_port}/{self._db_name}"
        else:
            if not self._dsn:
                self._dsn = DatabaseConfig.DB_URL


class APgDriver(BasePgDriver):

    def _get_default_row_factory(self): return dict_row

    async def __aenter__(self):
        self.conn = await psycopg.AsyncConnection.connect(self._dsn, row_factory=self._get_default_row_factory())
        self.curr = self.conn.cursor()
        return self.curr

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.commit()
        await self.conn.close()
        await self.curr.close()


class PgDriver(BasePgDriver):
    """
    Контекстный менеджер для работы с БД прямыми SQL запросами.
    Usage:
        from core.contrrollers.database import PgDriver
        with PgDriver() as curr:
            curr.execute("SELECT first_name, last_name FROM usession")
            result = curr.fetchall()
            for row in result:
                print(row["first_name"], row["last_name"])
    Usage with SqlAlchemy models:
        from core.models.operator import Operator
        from core.contrrollers.database import PgDriver
        with PgDriver() as curr:
            curr.execute("SELECT * FROM operators")
            items = curr.fetchall()
        if not items:
            return None
        return [Operator(**item) for item in items]
    """

    def _get_default_row_factory(self): return RealDictCursor

    def __enter__(self):
        self.conn = psycopg2.connect(self._dsn, cursor_factory=self._get_default_row_factory())
        self.curr = self.conn.cursor()
        return self.curr

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.curr.close()
