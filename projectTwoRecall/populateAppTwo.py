import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projectTwoRecall.settings')

import django
django.setup()

from faker import Faker
from appTwo.models import Users

fake = Faker()

def addData():
    fake_name = fake.name()
    fake_email = fake.email()
    fake_comment = fake.text(max_nb_chars=221)
    U = Users.objects.get_or_create(name=fake_name, email=fake_email, comment=fake_comment)[0]
    U.save()

def populate(n):
    for i in range(n):
        addData()


if(__name__=='__main__'):
    print('\nCreating Fake Data in DB....')
    populate(30)
    print('\nFake Data has been inserted !!\n')
