# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fn500", bday="10", bmonth="February", byear="1000", aday="20", amonth="March", ayear="2000"))
    app.contact.delete_first_contact()