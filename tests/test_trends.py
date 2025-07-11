import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from trends import extract_tags, score_query, nlp_filter


def test_extract_tags():
    query = "best camera vs phone"
    tags = extract_tags(query)
    assert set(tags) == {"best", "vs"}


def test_nlp_filter_accepts_nouns():
    assert nlp_filter("cool gadgets")


def test_nlp_filter_rejects_no_nouns():
    assert not nlp_filter("the and or")


def test_score_query_rising():
    score = score_query("buy shoes", 50, True)
    assert score == 80  # 50 base + 20 trend boost + 10 for 'buy'


def test_score_query_non_rising():
    score = score_query("cheap deals", 30, False)
    assert score == 40  # 30 base + 0 trend boost + 10 for 'cheap'
