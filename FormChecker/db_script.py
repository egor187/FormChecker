import random
import datetime

from FormChecker.models import FormTemplate


form_template_names = (
    "Order form",
    "Male form",
    "SUR form",
    "Check form",
    "Class form",
    "Another form",
)

email_choices = (
    "a@gmail.com",
    "b@gmail.com",
    "c@gmail.com",
    "d@gmail.com",
    "e@gmail.com",
    "f@gmail.com",
)

phone_number_choices = (
    "+7 925 111 22 33",
    "+7 925 111 22 44",
    "+7 925 111 22 55",
    "+7 925 111 22 66",
    "+7 925 111 22 77",
    "+7 925 111 22 88",
)

text_choices = [
    "Hello",
    "Hi",
    "Wow",
    "Bye",
]


if __name__ == "__main__":
    for index in range(6):
        FormTemplate.objects.create(
            name=form_template_names[index],
            email=email_choices[index],
            tel_number=phone_number_choices[index],
            date=datetime.date.today() - datetime.timedelta(random.randint(1, 365)),
            text=random.choice(text_choices)
        )
