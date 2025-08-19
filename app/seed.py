"""TODO"""
import random
import time
from faker import Faker
from sqlalchemy.orm import Session
from app.infrastructure import database
from app.infrastructure.database import models

fake = Faker()

def seed(db: Session, num_users: int = 1000, posts_per_user: int = 1000):
    """TODO"""
    start = time.time()
    print(f"Inserindo {num_users} usuários com {posts_per_user} posts cada...")

    users = []
    for _ in range(num_users):
        user = models.User(
            username=fake.unique.user_name(),
            email=fake.unique.email()
        )
        db.add(user)
        users.append(user)
    db.commit()

    print("Usuários criados. Inserindo posts...")

    for user in users:
        for _ in range(posts_per_user):
            post = models.Post(
                user_id=user.id,
                content=fake.text(max_nb_chars=200),
                likes=random.randint(0, 100)
            )
            db.add(post)
        db.commit()  # Um commit por usuário

    print(f"✅ Dados inseridos com sucesso em {round(time.time() - start, 2)} segundos.")

if __name__ == "__main__":
    db_gen = database.get_db()
    db = next(db_gen)
    try:
        seed(db)
    finally:
        db_gen.close()
