# All written by Gemini
import os
import datetime as dt
import pytest
from scripts.common.logger import write_log, file_path

test_file = 'test'
today = dt.datetime.now().strftime("%Y-%m-%d")
test_path = f"{file_path}/{test_file}-{today}.log"

# 🔹 Fixture: setup + teardown
@pytest.fixture
def clean_log():
    if os.path.exists(test_path):
        os.remove(test_path)
    yield
    if os.path.exists(test_path):
        os.remove(test_path)

def read_log():
    with open(test_path, "r") as f:
        return f.read()

def test_write_log_message_none(clean_log):
    write_log(message=None, file_name=test_file, job='test')

    content = read_log()
    assert "| test |" in content
    assert "| INFO |" in content
    assert "None" in content

def test_write_log_empty_message(clean_log):
    write_log(message='', file_name=test_file, job='test')

    content = read_log()
    assert "| test |" in content
    assert "| INFO |" in content

def test_write_log_invalid_level(clean_log):
    write_log(message='mes', file_name=test_file, job='test', level='BUG')

    content = read_log()
    assert 'Invalid level' in content
    assert "| test |" in content
    assert "| ERROR |" in content

def test_write_log_lowercase_level(clean_log):
    write_log(message='mes', file_name=test_file, job='test', level='info')

    content = read_log()
    assert "| test |" in content
    assert "| INFO |" in content

def test_write_log_none_job(clean_log):
    write_log(message='mes', file_name=test_file, level='INFO')

    content = read_log()
    assert "| INFO |" in content

def test_write_log_special_message(clean_log):
    write_log(message='!@#$%^&**(())', file_name=test_file, job='test')

    content = read_log()
    assert "| test |" in content
    assert "| INFO |" in content

def test_write_log_long_message(clean_log):
    write_log(message='abcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghiabcdefghi', file_name=test_file, job='test')

    content = read_log()
    assert "| test |" in content
    assert "| INFO |" in content

def test_write_log_happy_path(clean_log):
    write_log(message='Happy happy happy', file_name=test_file, job='test')

    content = read_log()
    assert "| test |" in content
    assert "| INFO |" in content
