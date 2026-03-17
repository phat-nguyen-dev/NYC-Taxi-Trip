# All written by Gemini
import os
import pytest
import datetime as dt
from scripts.common.logger import write_log, file_path

def test_write_log_creates_file():
    # Setup: Use default "log" filename and clear old logs for testing
    test_file = "test"
    today = dt.datetime.now().strftime("%Y-%m-%d")
    expected_path = f"{file_path}/{test_file}-{today}.log"
    
    if os.path.exists(expected_path):
        os.remove(expected_path)

    # Action: Log a message using default parameters
    write_log("Test message", test_file, job="UnitTest", level="INFO")

    # Assert: Verify file creation and content
    assert os.path.exists(expected_path) is True
    
    with open(expected_path, "r") as f:
        content = f.read()
        assert "Test message" in content
        assert "INFO" in content
        assert "UnitTest" in content

def test_invalid_level_fallback():
    # Test unmatching level
    test_file = "test"
    write_log("Check invalid level", test_file, level="GIBBERISH")
    
    today = dt.datetime.now().strftime("%Y-%m-%d")
    path = f"{file_path}/{test_file}-{today}.log"
    
    with open(path, "r") as f:
        content = f.read()
        assert "ERROR" in content
        assert "Invalid level: (GIBBERISH)" in content