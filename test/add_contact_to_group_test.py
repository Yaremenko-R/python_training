from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_some_contact_to_some_group(app, db):
    contact = Contact(firstname="fn500", lastname="ln")
    group = Group(name="TEST")
    if db.get_contact_list() == 0:
        app.contact.create(contact)
    elif db.get_group_list() == 0:
        app.group.create(group)
    else:
        contacts = db.get_contact_list()
        cindex = randrange(len(contacts))
        groups = db.get_group_list()
        gindex = randrange(len(groups))
        app.contact.add_contact_by_index_to_group(cindex, gindex)
