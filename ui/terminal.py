"""Terminal rendering primitives: menus, headers, pagination, bars."""

import shutil
import textwrap
import sys

from ui.colors import (
    RESET, BOLD, DIM, ITALIC, UNDERLINE,
    RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, GRAY,
    BRIGHT_CYAN, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE,
    BRIGHT_WHITE, BRIGHT_MAGENTA,
    BG_BLUE, BG_MAGENTA, BG_CYAN,
    colored, strip_ansi,
)


def get_width():
    return shutil.get_terminal_size().columns


def get_height():
    return shutil.get_terminal_size().lines


def clear_screen():
    print("\033[2J\033[H", end="")


def print_header(title):
    """Print a centered boxed header."""
    w = min(get_width(), 80)
    title_clean = strip_ansi(title)
    padding = max(0, w - len(title_clean) - 4)
    left_pad = padding // 2
    right_pad = padding - left_pad

    print()
    print(colored("  " + "━" * (w - 2), CYAN))
    print(colored("  ┃", CYAN) + " " * left_pad + colored(title, BOLD, BRIGHT_WHITE) + " " * right_pad + colored("┃", CYAN))
    print(colored("  " + "━" * (w - 2), CYAN))
    print()


def print_section(title, content=""):
    """Print a section title with optional content."""
    print(colored(f"  {title}", BOLD, BRIGHT_CYAN))
    print(colored("  " + "─" * min(len(strip_ansi(title)) + 4, get_width() - 4), DIM))
    if content:
        for line in content.strip().split("\n"):
            print(f"    {line}")
    print()


def print_menu(title, options, prompt="Choix", allow_back=False, allow_quit=False):
    """Display numbered options and return the chosen index (1-based) or special values."""
    print_section(title)
    for i, opt in enumerate(options, 1):
        num_style = colored(f"  [{i}]", BRIGHT_YELLOW)
        print(f"  {num_style} {opt}")
    print()

    extras = []
    if allow_back:
        extras.append(colored("[b]", DIM) + colored(" Retour", DIM))
    if allow_quit:
        extras.append(colored("[q]", DIM) + colored(" Quitter", DIM))
    if extras:
        print("  " + "  ".join(extras))
        print()

    while True:
        try:
            raw = input(colored(f"  {prompt} > ", BRIGHT_GREEN)).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            sys.exit(0)

        if allow_back and raw == "b":
            return "back"
        if allow_quit and raw == "q":
            return "quit"

        try:
            choice = int(raw)
            if 1 <= choice <= len(options):
                return choice
        except ValueError:
            pass

        print(colored(f"    Entree invalide. Choisis entre 1 et {len(options)}.", RED))


def print_bar(label, value, max_value=10, width=30):
    """Render a horizontal bar chart row."""
    if max_value <= 0:
        max_value = 1
    filled = int((value / max_value) * width)
    empty = width - filled
    pct = int((value / max_value) * 100)

    bar = colored("█" * filled, BRIGHT_GREEN) + colored("░" * empty, DIM)
    label_fmt = colored(f"  {label:<22}", BOLD)
    score_fmt = colored(f" {pct}%", BRIGHT_YELLOW)
    print(f"{label_fmt} [{bar}]{score_fmt}")


def print_bar_simple(label, value, max_value=100, width=30):
    """Render a bar with raw value display."""
    filled = int((value / max_value) * width) if max_value > 0 else 0
    filled = min(filled, width)
    empty = width - filled
    bar = colored("█" * filled, BRIGHT_CYAN) + colored("░" * empty, DIM)
    label_fmt = colored(f"  {label:<22}", BOLD)
    score_fmt = colored(f" {value:.0f}/{max_value:.0f}", BRIGHT_YELLOW)
    print(f"{label_fmt} [{bar}]{score_fmt}")


def print_paginated(title, text, lines_per_page=None):
    """Display long text page by page."""
    w = min(get_width() - 8, 76)
    h = get_height()
    if lines_per_page is None:
        lines_per_page = max(h - 8, 10)

    # Wrap text
    raw_lines = text.strip().split("\n")
    wrapped = []
    in_code = False
    for line in raw_lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            wrapped.append(line)
            continue
        if in_code or stripped.startswith("    ") or stripped.startswith("\t"):
            wrapped.append(line)
        else:
            if len(line) > w:
                wrapped.extend(textwrap.wrap(line, width=w))
            else:
                wrapped.append(line)

    pages = []
    for i in range(0, len(wrapped), lines_per_page):
        pages.append(wrapped[i:i + lines_per_page])

    if not pages:
        return

    page_idx = 0
    while True:
        clear_screen()
        print_header(title)

        for line in pages[page_idx]:
            print(f"    {line}")

        print()
        page_info = colored(f"  Page {page_idx + 1}/{len(pages)}", DIM)
        print(page_info)

        if len(pages) == 1:
            nav = colored("  [Entree] Retour", DIM)
        elif page_idx == 0:
            nav = colored("  [Entree] Page suivante  [q] Retour", DIM)
        elif page_idx == len(pages) - 1:
            nav = colored("  [b] Page precedente  [q] Retour", DIM)
        else:
            nav = colored("  [Entree] Suivante  [b] Precedente  [q] Retour", DIM)
        print(nav)

        try:
            raw = input("  > ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            break

        if raw == "q" or (len(pages) == 1 and raw == ""):
            break
        elif raw == "b" and page_idx > 0:
            page_idx -= 1
        elif raw == "" and page_idx < len(pages) - 1:
            page_idx += 1


def print_pros_cons(pros, cons):
    """Display a formatted pros/cons list."""
    print(colored("  Avantages", BOLD, BRIGHT_GREEN))
    for p in pros:
        print(colored("    + ", GREEN) + p)
    print()
    print(colored("  Inconvenients", BOLD, BRIGHT_RED))
    for c in cons:
        print(colored("    - ", RED) + c)
    print()


def press_enter():
    """Wait for Enter."""
    try:
        input(colored("\n  [Entree] Continuer...", DIM))
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)


BANNER = r"""
   _____ __             __      ___       __       _
  / ___// /_____ ______/ /__   /   | ____/ /   __ (_)________  _____
  \__ \/ __/ __ `/ ___/ //_/  / /| |/ __  / | / / / ___/ __ \/ ___/
 ___/ / /_/ /_/ / /__/ ,<    / ___ / /_/ /| |/ / (__  ) /_/ / /
/____/\__/\__,_/\___/_/|_|  /_/  |_\__,_/ |___/_/____/\____/_/
"""


def print_banner():
    """Display the welcome banner."""
    clear_screen()
    print(colored(BANNER, BOLD, BRIGHT_CYAN))
    print(colored("  Guide interactif pour choisir ta stack technologique", BOLD, WHITE))
    print(colored("  ─────────────────────────────────────────────────────", DIM))
    print()
