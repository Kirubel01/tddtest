import pytest
from io import StringIO
from file_reader import read_file

def test_read_file(capfd):
    # Create a temporary file with known content
    temp_file_content = "This is a test file."
    with open("temp_test_file.txt", "w") as file:
        file.write(temp_file_content)

    # Call the function
    read_file("temp_test_file.txt")

    # Capture the standard output (STDOUT)
    out, err = capfd.readouterr()

    assert out.strip() == temp_file_content

def test_read_nonexistent_file(capfd):
    # Call the function with a non-existent file
    read_file("non_existent_file.txt")

    # Capture the standard output (STDOUT)
    out, err = capfd.readouterr()

    assert out.strip() == f"File 'non_existent_file.txt' not found"
