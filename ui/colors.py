"""ANSI color constants and helpers for terminal rendering."""

import re

# Reset
RESET = "\033[0m"

# Styles
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Foreground colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GRAY = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

_ANSI_RE = re.compile(r"\033\[[0-9;]*m")


def colored(text, *styles):
    """Wrap text with ANSI styles and append RESET."""
    prefix = "".join(styles)
    return f"{prefix}{text}{RESET}"


def strip_ansi(text):
    """Remove all ANSI escape codes from text."""
    return _ANSI_RE.sub("", text)
