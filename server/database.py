'''
Author: jiandong.ye
email: yejiandong@bytedance.com
Date: 2020-12-23 23:41:55
description: 
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from model.User import User
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    from model.User import User
    init_db()
    u = User('admin', 'admin@localhost')
    db_session.add(u)
    db_session.commit()