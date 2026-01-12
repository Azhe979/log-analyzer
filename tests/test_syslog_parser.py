from log_analyzer.parser.syslog import parse_line


def test_parse_valid_syslog_line():
    line = (
        "Jan  8 10:01:02 host1 sshd[1234]: "
        "Failed password for invalid user test"
    )

    result = parse_line(line)

    assert result is not None
    assert result["program"] == "sshd"
    assert result["level"] == "ERROR"


def test_parse_invalid_line_returns_none():
    line = "this is not a syslog line"

    result = parse_line(line)

    assert result is None
