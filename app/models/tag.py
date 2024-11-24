"""
id: unique key
tag: name of the tag
"""

from db_connection import news_db
from app.utils.logger_conf import setup_logger

logger = setup_logger("tag table")

def create_tag_table():
    with news_db.connect_to_postrgres() as conn:
        with conn.cursor() as curs:
            try:
                curs.execute("""
                        CREATE TABLE tag(
                            ID SERIAL PRIMARY KEY,
                            tag VARCHAR(50)
                    )
                            """)    
                logger.info("tag table has been created.")    
            except Exception as e:
                logger.error(f"Error creating Tag table: {e}")
                
create_tag_table()