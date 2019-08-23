from model.contact import Contact
from model.group import Group
from random import randrange


def test_del_some_contact_from_group(app, orm):
    contacts = orm.get_contact_list()
    cindex = randrange(len(contacts))
    contact_to_del = contacts[cindex]
    groups = orm.get_group_list()
    gindex = randrange(len(groups))
    if gindex <= 1:
        gindex = gindex + 1
        return gindex
    group_to_del_from = groups[gindex]
    if not orm.get_groups_contact_added(contact_to_del):
        app.contact.add_contact_by_index_to_group(contact_to_del, group_to_del_from)
    app.contact.del_contact_by_index_from_group(cindex, gindex)
    contacts_in_group_del_from = orm.get_contacts_in_group(group_to_del_from)
    if contact_to_del not in contacts_in_group_del_from:
        print(f"Contact {contact_to_del} was removed from group {group_to_del_from} successfully!")
    else:
        print("Something is wrong...")

