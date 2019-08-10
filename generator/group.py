from model.group import Group
import random
import string
import os.path
import json

# Fixed data
# from data.group import constant as test_data добавить в файл add_group_test.py
constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]


# Random data
# from data.group import test_data добавить в файл add_group_test.py
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] +[
    Group(name=random_string("name", 15), header=random_string("header", 15), footer=random_string("footer", 15))
    for i in range(3)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))