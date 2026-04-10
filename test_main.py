from unittest.mock import mock_open, patch
import main


def test_read_file():
    mock_data = "fsferwewe \n  fsadq2312312"

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = main.read_file("fake.txt")

    assert result == mock_data


def test_input_keyword():
    assert main.input_keyword("ab") == "ab"
