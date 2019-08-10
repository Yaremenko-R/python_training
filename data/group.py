from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [Group(name="", header="", footer="")] +[
    Group(name=random_string("name", 15), header=random_string("header", 15), footer=random_string("footer", 15))
    for i in range(3)]