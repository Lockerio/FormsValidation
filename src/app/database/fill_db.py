from app.database.database import db

data_to_insert = [
    {"name": "registration form",
     "email": "email",
     "password": "text",
     "first_name": "text",
     "last_name": "text",
     "date_of_birth": "date",
     "phone_number": "phone_number"},

    {"name": "feedback form",
     "email": "email",
     "full_name": "text",
     "feedback subject": "text",
     "feedback message": "text"},

    {"name": "contact form",
     "email": "email",
     "full_name": "text",
     "date_of_birth": "date",
     "phone_number": "phone_number"}
]

collection = db["forms"]
collection.insert_many(data_to_insert)
