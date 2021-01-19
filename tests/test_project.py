import pytest
from unittest.mock import Mock
from modules.project import Project_class

mock = Mock()
project = Project_class()

@pytest.fixture
def records():
    pid = 201
    pname = "InSync"
    status = "Active"
    lead_id = 5
    records = [pid, pname, status, lead_id]
    return records


def test_insert_project(records):
    assert project.insert_table_values(records[0], records[1], records[2], records[3]) == records[1]


def test_update_project():
    assert project.update_record(201, "Closed") == 1


def test_delete_project():
    assert project.delete_record(201) == 1


