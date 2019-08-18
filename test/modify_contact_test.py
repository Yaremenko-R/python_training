from random import randrange
from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    contact = Contact(firstname="fn500", lastname="ln")
    if db.get_contact_list() == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
