from app.models.db_connection import news_db
from app.utils.logger_conf import setup_logger

logger = setup_logger("user_interests table")

def create_user_interests_table():
    with news_db.connect_to_postrgres() as conn:
        with conn.cursor() as curs:
            try:
                curs.execute("""
                            CREATE TABLE user_interests(
                                user_id INT REFERENCES users(id) ON DELETE CASCADE,
                                tag_id INT REFERENCES tag(id) ON DELETE CASCADE,
                                PRIMARY KEY (user_id, tag_id)
                            )
                            """)   
                logger.info("user_interests table has been created.")
                conn.commit()
            except Exception as e:
                logger.error(f"Error creating Tag table: {e}")
                
create_user_interests_table()