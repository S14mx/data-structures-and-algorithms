from .merge_sort import merge_sort


def test_exists():
    assert merge_sort


def test_merge_sort1():
    list = [8, 4, 23, 42, 16, 15]
    merge_sort(list)
    assert list == [4, 8, 15, 16, 23, 42]


def test_merge_sort2():

    list = [20, 18, 12, 8, 5, -2]
    merge_sort(list)
    assert list == [-2, 5, 8, 12, 18, 20]


def test_merge_sort3():

    list = [2, 3, 5, 7, 13, 11]
    merge_sort(list)
    assert list == [2, 3, 5, 7, 11, 13]


def test_merge_sort4():

    list = [5, 12, 7, 5, 5, 7]
    merge_sort(list)
    assert list == [5, 5, 5, 7, 7, 12]


def test_merge_sort_empty_list():
    actual = merge_sort([])
    expected = []
    assert actual == expected


def test_merge_sort_non_integers():
    actual = merge_sort([2, "3", 1])
    expected = "Input list contains non-integers"
    assert actual == expected


def test_merge_sort_one():
    actual = merge_sort([2])
    expected = [2]
    assert actual == expected
