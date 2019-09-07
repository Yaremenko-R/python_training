from pytest_bdd import given, when, then
from model.contact import Contact
import random
from random import randrange


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a new contact with <firstname>, <lastname>, <address> and <homephone>')
def new_contact(firstname, lastname, address, homephone):
    return Contact(firstname=firstname, lastname=lastname, address=address, homephone=homephone)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="fn500", lastname="ln"))
    return db.get_contact_list()


@given('an index of random contact from the list')
def random_contact_index(non_empty_contact_list):
    return randrange(len(non_empty_contact_list))


@when('I delete the contact from the list')
def delete_contact(app, random_contact_index):
    app.contact.delete_contact_by_index(random_contact_index)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact_index, check_ui, app):
    new_contacts = db.get_contact_list()
    non_empty_contact_list[random_contact_index:random_contact_index+1] = []
    assert sorted(non_empty_contact_list, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)