# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_modify_some_group(app):
    group = Group(name = "TOST")
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_first_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name = "TOST"))
#    app.group.modify_first_group(Group(header="Test222"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


# def test_modify_first_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name = "TOST"))
#    app.group.modify_first_group(Group(footer="Test222"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)