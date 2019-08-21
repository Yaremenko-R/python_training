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
    delim = "\n"
    contacts_from_db = db.get_contact_list()
    contact_from_db_sorted = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contact_from_hp_sorted = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for c in range(len(contacts_from_db)):
        contact_from_db = contact_from_db_sorted[c]
        contact_from_hp = contact_from_hp_sorted[c]
        phones_from_db = delim.join([contact_from_db.homephone, contact_from_db.mobilephone, contact_from_db.workphone,
                                     contact_from_db.homephone2])
        emails_from_db = delim.join([contact_from_db.email1, contact_from_db.email2, contact_from_db.email3])
        assert contact_from_hp.firstname == contact_from_db.firstname
        assert contact_from_hp.lastname == contact_from_db.lastname
        assert contact_from_hp.address == contact_from_db.address
        assert contact_from_hp.all_phones_from_home_page == phones_from_db
        assert contact_from_hp.all_emails_from_home_page == emails_from_db
