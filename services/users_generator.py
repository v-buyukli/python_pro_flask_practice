from faker import Faker


def generate_users(number):
    fake = Faker()
    users = [f"{fake.name()} ({fake.email()})" for _ in range(number)]
    return users
