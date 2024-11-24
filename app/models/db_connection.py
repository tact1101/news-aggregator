import psycopg2
import abc
from contextlib import contextmanager
from app.utils.logger_conf import setup_logger

logger = setup_logger("db_connection")

class SingleConnection(abc.ABCMeta):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleConnection, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class PostgresConnection(metaclass=SingleConnection):
    """Uses Singletone thus the class remains the only one connection"""
    def __init__(self, database, user, psw, host, port) -> None :
        self.dbaname = database
        self.user = user
        self.psw = psw
        self.host = host
        self.port = port
    
    @contextmanager
    def connect_to_postrgres(self):
        try:
            conn = psycopg2.connect(database=self.dbaname, user=self.user, password=self.psw, host=self.host, port=self.port)
            yield conn
        except Exception as e:
            logger.error(f"Error connecting to postgre: {e}")
        finally:
            conn.close()
    
news_db = PostgresConnection(database="newsDB", user="postgres", psw="sudo", host="localhost", port="5433")

# with news_db.connect_to_postrgres() as conn:
#     with conn.cursor() as curs:
#         curs.execute("SELECT 1;")
