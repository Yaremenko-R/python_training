from random import randrange
from model.contact import Contact


def test_some_contact_on_home_page_check_info(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_edit_page)


def test_all_contact_on_home_page_check_info(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)
