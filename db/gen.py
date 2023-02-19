import csv
import random
from faker import Faker
fake = Faker()

num_user = 50000
num_movie = 20
min_age = 10
max_age = 80

userlist = []
ratinglist = []

def gen(num_user):
    for i in range(num_user):
        name = fake.unique.name()
        age = random.randint(min_age, max_age)
        row = [i, name, age]
        userlist.append(row)
        movieset = set()
        while len(movieset) < 10 + random.randint(0, 5):
            movieset.add(random.randint(0, num_movie))
        for mid in movieset:
            age_movie = random.randint(min_age, age)
            rowr = [i, mid, random.randint(0, 10), age_movie]
            ratinglist.append(rowr)
            if random.randint(0,3) == 0:
                age_movie = random.randint(min_age, age)
                rowr = [i, mid, random.randint(0, 10), age_movie]
                ratinglist.append(rowr)

def write_user():
    with open('user.csv', 'w') as f:
        writer = csv.writer(f)
        for row in userlist:
            writer.writerow(row)

def write_rating():
    with open('rating.csv', 'w') as f:
        writer = csv.writer(f)
        for row in ratinglist:
            writer.writerow(row)


gen(num_user)
write_user()
write_rating()