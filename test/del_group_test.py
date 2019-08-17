import random
from model.group import Group


def test_delete_some_group(app, db):
    group = Group(name="TEST")
    if db.get_group_list() == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)