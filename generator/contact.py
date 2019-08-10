from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# Fixed data
# from data.contact import constant as test_data добавить в файл add_contact_test.py
constant = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1"),
    Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2")
]


# Random data
# from data.contact import test_data добавить в файл add_contact_test.py
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                  address="", homephone="", mobilephone="", workphone="", fax="",
                  email1="", email2="", email3="", homepage="", bday="12", bmonth="February",
                  byear="", aday="15", amonth="March", ayear="", address2="",
                  homephone2="", notes="")] +[
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15), lastname=random_string("lastname", 15),
                  nickname=random_string("nickname", 15), title=random_string("title", 15), company=random_string("company", 15),
                  address=random_string("address", 15), homephone=random_string("123", 10), mobilephone=random_string("456", 10),
                  workphone=random_string("789", 10), fax=random_string("012", 10), email1=random_string("e1@", 10), email2=random_string("e2@", 10),
                  email3=random_string("e3@", 10), homepage=random_string("www.homepage", 15), bday="12", bmonth="February",
                  byear=random_string("1999", 5), aday="15", amonth="March", ayear=random_string("2000", 5), address2=random_string("address2", 15),
                  homephone2=random_string("345", 10), notes=random_string("notes", 25))
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))