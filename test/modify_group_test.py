import random
from model.group import Group


def test_modify_some_group(app, db):
    group = Group(name = "TOST")
    if db.get_group_list() == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    rgroup = random.choice(old_groups)
    app.group.modify_group_by_id(rgroup.id, group)
    new_groups = db.get_group_list()
    old_groups[rgroup.id] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
