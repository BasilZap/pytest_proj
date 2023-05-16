import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_get__empty_list():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, 1) == [1]
    assert arrs.my_slice([1, 2, 3, 4, 5], -2, -1) == [4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, -1) == [3, 4]
    assert arrs.my_slice([], 1, -1) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -6) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, -7) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 0, 7) == [1, 2, 3, 4, 5]