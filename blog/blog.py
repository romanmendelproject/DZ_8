from base_connect import Session, Base, engine
from models import Post, Tag, User, tags_posts_table
from sqlalchemy import func
from data_base import create_data


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    db_check = session.query(Post).all()
    if db_check:
        pass
    else: 
        create_data()