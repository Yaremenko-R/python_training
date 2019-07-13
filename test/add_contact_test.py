# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="title", company="company", address="address", homephone="home", mobilephone="mobile", workphone="work", fax="fax",
                               email1="e1", email2="e2", email3="e3", homepage="homepage", bday="12", bmonth="February", byear="1990", aday="15", amonth="March", ayear="1995", address2="address",
                               homephone2="home", notes="notes"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homephone="", mobilephone="", workphone="", fax="",
                               email1="", email2="", email3="", homepage="", bday="12", bmonth="February", byear="1990", aday="15", amonth="March", ayear="1995", address2="",
                               homephone2="", notes=""))
    app.session.logout()

