import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("postgres://zatylpqzillbmi:0809083c6de24ebedf74cfab1a89c37eb1ddde3f4cd75ed8bf695e91b827cc69@ec2-23-23-93-115.compute-1.amazonaws.com:5432/db59slghfhohl1"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    users = db.execute("SELECT username1, password FROM credentials WHERE id = 1").fetchall()
    for user in users:
        print(f"{user.origin} to {user.destination}, {user.duration} minutes.")

if __name__ == "__main__":
    main()
