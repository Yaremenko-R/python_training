# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="fn500", bday="10", bmonth="February", byear="1000", aday="20", amonth="March", ayear="2000"))
    app.contact.modify_first_contact(Contact(firstname="fn501", bday="11", bmonth="February", byear="1001", aday="21", amonth="March", ayear="2001"))