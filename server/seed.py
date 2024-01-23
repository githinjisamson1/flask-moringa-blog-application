from config import db, app, bcrypt
from faker import Faker
from models import User, Comment, Vote, Post
from random import choice

# instantiate Faker
fake = Faker()


# function to seed the database
def seed_database():
    # empty records for all tables
    print("Deleting records 🚮🚮🚮...")
    User.query.delete()
    Comment.query.delete()
    Vote.query.delete()
    Post.query.delete()

    emails = ['allan.njoroge@student.moringaschool.com', 'samson.githinji@student.moringaschool.com', 'noni.muthoni@student.moringaschool.com',
              'mercy.mwongeli@student.moringaschool.com', 'nahason.murithi@student.moringaschool.com']

    usernames = ['allanimated', 'githinjisamson1',
                 'generalimuthoni', 'mercymwongeli', 'nahasonmurithi']

    full_names = ['Allan Njoroge', 'Samson Githinji',
                  'Noni Muthoni', 'Mercy Mwongeli', 'Nahason Murithi']

    passwords = ['daskjdka', 'duejnsdbh',
                 'eruiapodxdba', 'aueoqnckas', 'dlkaojuhs']

    print("Inserting users  👫👫👫...")
    for i in range(5):
        # generate 10 user instances
        user = User(
            username=usernames[i],
            email=emails[i],
            full_name=full_names[i],
            _password_hash=bcrypt.generate_password_hash(
                passwords[i].encode('utf-8'))

        )

        db.session.add(user)
        db.session.commit()

    # extract user_id since users have already been seeded atp
    users_ids = [user.id for user in User.query.all()]

    phases = [0, 1, 2, 3, 4, 5]

    print("Inserting posts 🧾🧾🧾...")
    for _ in range(5):
        # generate 5 post instances
        post = Post(
            phase=choice(phases),
            title=fake.text(max_nb_chars=100),
            content=fake.text(max_nb_chars=1000),
            resources=fake.url(),
            user_id=choice(users_ids)
        )

        db.session.add(post)
        db.session.commit()

    # extract post_id since posts have already been seeded atp

    post_ids = [post.id for post in Post.query.all()]

    print("Inserting comments 📑📑📑...")
    for _ in range(10):
        comment = Comment(
            content=fake.text(max_nb_chars=200),
            user_id=choice(users_ids),
            post_id=choice(post_ids)
        )
        db.session.add(comment)
        db.session.commit()

    vote_types = [0, 1]

    print("Inserting votes 🗳🗳🗳...")

    for _ in range(10):
        vote = Vote(
            vote_type=choice(vote_types),
            user_id=choice(users_ids),
            post_id=choice(post_ids)
        )
        db.session.add(vote)
        db.session.commit()

    print("Complete 🤝🤝🤝...")


if __name__ == "__main__":
    with app.app_context():
        seed_database()
