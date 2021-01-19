import pytest
from datetime import datetime
from unittest.mock import Mock

from modules.Employee import Employee

mock = Mock()
employee = Employee()

@pytest.fixture
def records():
    id = 101
    name = "Rahul"
    lastname = "Kumar"
    join_date = datetime(2020, 9, 8)
    experience_years = 5
    records = [id, name, lastname, join_date, experience_years]
    return records


def test_insert_employee(records):
    assert employee.insert_table_values(records[0], records[1], records[2], records[3], records[4]) == records[1]


def test_update_employee():
    assert employee.update_record(101, 5) == 1


def test_delete_employee():
    assert employee.delete_record(101) == 1


