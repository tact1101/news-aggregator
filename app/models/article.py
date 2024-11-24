"""
Has fields:
    id: unique key
    Name: name of the article
    Content: text in the article
    source-link: site the article was taken from
    tag: [foreign key Tags] tags list
    data-time: field with yyyy.mm.dd
"""
from app.models.db_connection import news_db
from app.utils.logger_conf import setup_logger

logger = setup_logger("article table")

def create_article_table():
    with news_db.connect_to_postrgres() as conn:
        with conn.cursor() as curs:   
            try:
                curs.execute("""
                    CREATE TABLE article (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(80),
                        content TEXT,
                        source_link VARCHAR(255),
                        tag_id INT REFERENCES tag(id),
                        date_time DATE
                    ) 
                    """)
                conn.commit()
                logger.info("article table has been created.")
            except Exception as e:
                logger.error(f"Error creating article table: {e}")

create_article_table()