"""
id: telegram's unique identifier 
username: user's name 
interests: [foreign key Tags] of tags list user interested in
sources: sources users are interested in to be notified when an update is out there (will be imnplemented later)
interval: how often a user wants to be notified about updates e.g. once a week or once a month
"""

from app.models.db_connection import news_db
from app.utils.logger_conf import setup_logger

logger = setup_logger("users table")

def create_useres_table():
    with news_db.connect_to_postrgres() as conn:
        with conn.cursor() as curs:
            try:
                curs.execute("""
                            CREATE TABLE users(
                                id SERIAL PRIMARY KEY,
                                username VARCHAR(50) NOT NULL,
                                sources VARCHAR(80),
                                notification_interval INTERVAL 
                            )
                            """)   
                logger.info("users table has been created.")
                conn.commit()
            except Exception as e:
                logger.error(f"Error creating Tag table: {e}")
                
create_useres_table()