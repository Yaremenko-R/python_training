from random import randrange


def test_del_some_contact_from_group(app, orm):
    contacts = orm.get_contact_list()
    cindex = randrange(len(contacts))
    contact_to_del = contacts[cindex]
    groups = orm.get_group_list()
    gindex = randrange(2,len(groups))
    group_to_del_from = groups[gindex]
    if not orm.get_contacts_in_group(group_to_del_from):
        app.contact.add_contact_by_index_to_group(cindex, gindex)
    app.contact.del_contact_by_index_from_group(cindex, gindex)
    contacts_in_group_after_del = orm.get_contacts_in_group(group_to_del_from)
    assert contact_to_del not in contacts_in_group_after_del

