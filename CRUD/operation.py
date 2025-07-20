from. import config
import random
import string

def create_first_data():
    data = config.TEMPLATE.copy()
    data["pk"] = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    
    author = input("Author : ")
    title = input("Title : ")
    year = input("Year : ")

    data["author"] = author
    data["title"] = title
    data["year"] = year

    return data


