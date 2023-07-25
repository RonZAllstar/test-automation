import random


class UserGenerator(object):

    @classmethod
    def generate_user_details(cls):
        print("Generating user details")
        customer_col = ["AAA", "BBB"]
        roles = ["Admin", "Customer"]
        email = ["admin@mail.com", "customer@mail.com"]
        cell = ["082555", "083444"]

        user_details = {
            "first_name": "FName" + str(random.randint(1, 2)),
            "last_name": "LName" + str(random.randint(1, 2)),
            "username": "User" + str(random.randint(1, 1000)),
            "password": "Pass" + str(random.randint(1, 2)),
            "customer": "Company " + str(random.choice(customer_col)),
            "role": random.choice(roles),
            "email": random.choice(email),
            "cell": random.choice(cell)
        }

        return user_details
