# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "TOST"))
    app.group.modify_first_group(Group(name="Test222"))


def test_modify_first_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "TOST"))
    app.group.modify_first_group(Group(header="Test222"))


def test_modify_first_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "TOST"))
    app.group.modify_first_group(Group(footer="Test222"))