# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="Test222"))


def test_modify_first_header(app):
    app.group.modify_first_group(Group(header="Test222"))


def test_modify_first_footer(app):
    app.group.modify_first_group(Group(footer="Test222"))