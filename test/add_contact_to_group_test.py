from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_some_contact_to_some_group(app, orm):
    contact = Contact(firstname="fn500", lastname="ln")
    contacts = orm.get_contact_list()
    cindex = randrange(len(contacts))
    contact_to_add = contacts[cindex]
    groups = orm.get_group_list()
    gindex = randrange(len(groups))
    group_to_add = groups[gindex]
    if orm.get_group_list() == sorted(orm.get_groups_contact_added(contact_to_add), key=Group.id_or_max):
        app.contact.create(contact)
        app.contact.add_contact_by_index_to_group(0, gindex)
        contacts_in_group_by_db = orm.get_contacts_in_group(group_to_add)
        if contact in contacts_in_group_by_db:
            print(f"Contact {contact} was added to group {group_to_add} successfully!")
        else:
            print("Something is wrong...")
    else:
        app.contact.add_contact_by_index_to_group(cindex, gindex)
        contacts_in_group_by_db = orm.get_contacts_in_group(group_to_add)
        if contact_to_add in contacts_in_group_by_db:
            print(f"Contact {contact_to_add} was added to group {group_to_add} successfully!")
        else:
            print("Something is wrong...")
