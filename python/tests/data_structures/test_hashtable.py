import pytest
from data_structures.hash_table.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_apple_collision():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("paple", "PAPLE")
    actual = hashtable.get("paple")
    expected = "PAPLE"
    assert actual == expected


def test_get_non_existent():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("paple")
    expected = "Key is not found"
    assert actual == expected


def test_contains_collision():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("paple", "Used for apple sauce")
    actual = hashtable.contains("paple")
    expected = True
    assert actual == expected


def test_contains_non_existent():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.contains("paple")
    expected = False
    assert actual == expected


def test_keys_with_collision():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.keys()
    expected = ["ahmad", "silent", "listen"]
    assert actual == expected


def test_hash_wrong_data_type():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    actual = hashtable.hash([1])
    expected = "Only strings or integers are allowed as keys"
    assert actual == expected
