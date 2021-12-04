import pytest
@pytest.fixture(autouse=True)

def clean_text_file():
    with open("../testfile.txt", "w"):
        pass  # затирает файл