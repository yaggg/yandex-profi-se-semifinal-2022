import pytest

from app.storage.data_loader import DataLoader

data_loader = DataLoader()


def test_csv():
    path = 'test.csv'
    df = data_loader.file_upload(path)
    assert df is not None


def test_wrong():
    with pytest.raises(Exception):
        data_loader.file_upload('wrong')
