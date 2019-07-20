# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="fn500", bday="10", bmonth="February", byear="1000", aday="20", amonth="March", ayear="2000"))