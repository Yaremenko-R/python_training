# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="fnn", middlename="mn", lastname="ln", nickname="nn", title="title", company="company", address="address", homephone="home", mobilephone="mobile", workphone="work", fax="fax",
                               email1="e1", email2="e2", email3="e3", homepage="homepage", bday="12", bmonth="February", byear="1990", aday="15", amonth="March", ayear="1995", address2="address",
                               homephone2="home", notes="notes"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="",
                               email1="", email2="", email3="", homepage="", bday="12", bmonth="February", byear="", aday="15", amonth="March", ayear="", address2="",
                               homephone2="", notes=""))

