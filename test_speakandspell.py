from speakandspell import get_sentence, get_clue, convert_code


def test_get_sentence():
    assert get_sentence("EIGHT") == "Eight. As in eight reindeer"
    assert get_sentence("FOR") == "For. As in for someone."
    assert get_sentence("HELLO") == "HELLO"
    assert get_sentence("GOODBYE") == "GOODBYE"


def test_get_clue():
    assert get_clue("ALREADY", "_LRE_DY") == "A"
    assert get_clue("ALREADY", "ALR_A__") in ("E", "D", "Y")
    assert get_clue("LAUGHTER", "________") in ("L", "A", "U", "G", "H", "T", "E", "R")
    assert get_clue("LAUGHTER", "LAUGH_ER") == "T"


def test_convert_code():
    assert convert_code("HELLO") == "YBUUR"
    assert convert_code("YBUUR") == "HELLO"
    assert convert_code("PYTHON") == "QHMYRS"
    assert convert_code("QHMYRS") == "PYTHON"
