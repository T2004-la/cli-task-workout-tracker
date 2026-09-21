import pytest

from project import format_log_entry, parse_duration, validate_date





def test_validate_date():

    assert validate_date("2026-08-31") is True

    assert validate_date("2025-01-01") is True

    assert validate_date("2026-02-30") is False

    assert validate_date("31-08-2026") is False  

    assert validate_date("invalid") is False





def test_parse_duration():

    assert parse_duration("30") == 30

    assert parse_duration("  120 ") == 120



    with pytest.raises(ValueError):

        parse_duration("-5")

    with pytest.raises(ValueError):

        parse_duration("0")

    with pytest.raises(ValueError):

        parse_duration("abc")





def test_format_log_entry():

    assert format_log_entry("  running ", 45, "2026-08-31") == {

        "date": "2026-08-31",

        "task": "Running",

        "duration_min": 45,

    }

    assert format_log_entry("", 30, "2026-08-31") == {

        "date": "2026-08-31",

        "task": "Untitled Activity",

        "duration_min": 30,

    } 

