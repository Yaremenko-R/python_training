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
    contacts_from_db = db.get_contact_list()
    contact_from_db_sorted = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_hp_sorted = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for c in range(len(contacts_from_db)):
        contact_from_db = contact_from_db_sorted[c]
        contact_from_hp = contact_from_hp_sorted[c]
        assert contact_from_hp.firstname == contact_from_db.firstname
        assert contact_from_hp.lastname == contact_from_db.lastname
        assert contact_from_hp.address == contact_from_db.address
        assert contact_from_hp.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_hp.all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contact_from_db)
