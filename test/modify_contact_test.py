# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="fn2", middlename="mn2", lastname="ln2", nickname="nn2", title="title2", company="company2", address="address2", homephone="home2", mobilephone="mobile2", workphone="work2", fax="fax2",
                                             email1="e12", email2="e22", email3="e32", homepage="homepage2", bday="13", bmonth="February", byear="1999", aday="17", amonth="March", ayear="1990", address2="address2",
                                             homephone2="home2", notes="notes2"))
    app.session.logout()