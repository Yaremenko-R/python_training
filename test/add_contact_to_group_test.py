from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_some_contact_to_some_group(app, orm):
    contact = Contact(firstname="Python", lastname="Testing")
    group = Group(name="Course")
    if orm.get_group_list() == 0 or orm.get_contact_list() == 0:
        app.group.create(group)
        app.contact.create(contact)
    contacts = orm.get_contact_list()
    cindex = randrange(len(contacts))
    contact_to_add = contacts[cindex]
    groups = orm.get_group_list()
    gindex = randrange(len(groups))
    group_to_add = groups[gindex]
    if orm.get_group_list() == sorted(orm.get_groups_contact_added(contact_to_add), key=Group.id_or_max):
        app.contact.create(contact)
        contact_to_add = contact
        contacts.append(contact)
        cindex = -1
    app.contact.add_contact_by_index_to_group(cindex, gindex)
    target_contact_groups = sorted(orm.get_groups_contact_added(contact_to_add), key=Group.id_or_max)
    contacts_in_target_group = sorted(orm.get_contacts_in_group(group_to_add), key=Group.id_or_max)
    assert contacts_in_target_group in target_contact_groups