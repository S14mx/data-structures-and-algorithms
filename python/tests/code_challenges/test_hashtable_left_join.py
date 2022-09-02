import pytest
from code_challenges.hashtable_left_join.hashtable_left_join import left_join
from data_structures.hash_table.hashtable import Hashtable


def test_exists():
    assert left_join


def test_example():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")

    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")

    expected = [
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['outfit', 'garb', None],
        ['guide', 'usher', 'follow'],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual == expected


def test_fail():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")

    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")

    expected = [
        ['outfit', 'garb', None],
        ['fond', 'enamored', 'averse'],
        ['guide', 'usher', 'follow'],
        ['diligent', 'employed', 'idle'],
        ['wrath', 'anger', 'delight'],
    ]
    actual = left_join(synonyms, antonyms)
    assert actual != expected


def test_uneven_buckets():
    synonyms = Hashtable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")

    antonyms = Hashtable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")

    expected = [
        ['wrath', 'anger', None],
        ['diligent', 'employed', 'idle'],
        ['fond', 'enamored', 'averse'],
        ['outfit', 'garb', None],
        ['guide', 'usher', None],
    ]

    actual = left_join(synonyms, antonyms)
    assert actual == expected
