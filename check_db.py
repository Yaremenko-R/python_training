from fixture.orm import ORMFixture
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact

database = ORMFixture(host="localhost", name="addressbook", user="root", password="")

try:
    l = database.get_contacts_in_group(Group(id="174"))
#    l = sorted(database.get_groups_contact_added(Contact(id="1")), key=Group.id_or_max)
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
