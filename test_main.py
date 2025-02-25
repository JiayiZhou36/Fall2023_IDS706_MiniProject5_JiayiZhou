"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transfrom_load"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_update_record():
    """tests update_record"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update_record",
            "1",
            "Emma Watson",
            "1931",
            "BSN",
            "NL",
            "1",
            "0",
            "1",
            "0.769262",
            "99",
            "0.7342619",
            "0.1699602",
            "watse101",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_record():
    """tests delete_record"""
    result = subprocess.run(
        ["python", "main.py", "delete_record", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_create_record():
    """tests create_record"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_record",
            "Emma Watson",
            "1931",
            "BSN",
            "NL",
            "1",
            "0",
            "1",
            "0.678420",
            "99",
            "0.7942619",
            "0.1699602",
            "watse101",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_general_query():
    """tests general_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM Goose WHERE name = 'Emma Watson'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read_data():
    """tests read_data"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()
    test_general_query()
