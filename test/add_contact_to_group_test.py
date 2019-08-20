from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_some_contact_to_some_group(app, db, orm):
    contact = Contact(firstname="fn500", lastname="ln")
    group = Group(name="TEST")
    if orm.get_contact_list() == 0:
        app.contact.create(contact)
    elif orm.get_group_list() == 0:
        app.group.create(group)
    else:
        contacts = orm.get_contact_list()
        cindex = randrange(len(contacts))
        groups = orm.get_group_list()
        gindex = randrange(len(groups))
        group = groups[gindex]
        app.contact.add_contact_by_index_to_group(cindex, gindex)
        contacts_in_group_by_db = orm.get_contacts_in_group(group)

