from .insertion_sort import insertion_sort


def test_exists():
    assert insertion_sort


def test_insertion_sort1():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_insertion_sort2():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_insertion_sort3():
    actual = insertion_sort([2, 3, 5, 7, 13, 11])
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected


def test_insertion_sort_empty_list():
    actual = insertion_sort([])
    expected = []
    assert actual == expected


def test_insertion_sort_non_integers():
    actual = insertion_sort([2, "3", 1])
    expected = "Input list contains non-integers"
    assert actual == expected


def test_insertion_sort_one():
    actual = insertion_sort([2])
    expected = [2]
    assert actual == expected
