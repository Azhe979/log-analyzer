import re
from typing import Optional

_PATTERN = re.compile(
    r'^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\S+\s+'
    r'(\w+)(?:\[\d+\])?:\s*(.*)$'
)

def parse_line(line: str) -> Optional[dict]:
    """
    Parse a single line of syslog format.

    :param line: A line of syslog-formatted text.
    :return: A dictionary with parsed components or None if the line doesn't match the format.
    """
    match = _PATTERN.match(line)
    
    if not match:
        return None
    
    program = match.group(1)
    message = match.group(2)
    level = _infer_level(message)
    
    return {
        'program': program,
        'message': message,
        'level': level
    }


def _infer_level(message: str) -> str:
    message_lower = message.lower()
    
    if re.search(r'failed|error|fatal|denied', message_lower):
        return 'ERROR'
    if re.search(r'warning|warn', message_lower):
        return 'WARNING'
    return 'INFO'
