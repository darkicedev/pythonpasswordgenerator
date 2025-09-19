"""Password generator CLI.

This script lets the user generate random passwords with customizable
options such as length, uppercase letters, digits, and symbols.
"""

from __future__ import annotations

import argparse
import random
import string
import sys
from typing import Sequence

# Default password length when the user does not specify one.
DEFAULT_LENGTH = 12

# Character set used when the user opts in to symbols.
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"


def generate_password(
    length: int = DEFAULT_LENGTH,
    use_uppercase: bool = False,
    use_digits: bool = False,
    use_symbols: bool = False,
) -> str:
    """Return a random password string based on the provided options."""
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    # Lowercase letters are always included to ensure a non-empty pool.
    character_pool: list[str] = list(string.ascii_lowercase)

    if use_uppercase:
        character_pool.extend(string.ascii_uppercase)
    if use_digits:
        character_pool.extend(string.digits)
    if use_symbols:
        character_pool.extend(SYMBOLS)

    random_generator = random.SystemRandom()
    return "".join(random_generator.choice(character_pool) for _ in range(length))


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Configure and parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument(
        "--length",
        type=int,
        default=DEFAULT_LENGTH,
        help=f"Password length (default: {DEFAULT_LENGTH}).",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="Include uppercase letters in the password.",
    )
    parser.add_argument(
        "--digits",
        action="store_true",
        help="Include digits in the password.",
    )
    parser.add_argument(
        "--symbols",
        action="store_true",
        help="Include special symbols in the password.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """Program entry point for the command-line interface."""
    args = parse_arguments(argv)

    if not any((args.uppercase, args.digits, args.symbols)):
        print(
            "Warning: Generating password using only lowercase letters.",
            file=sys.stderr,
        )

    try:
        password = generate_password(
            length=args.length,
            use_uppercase=args.uppercase,
            use_digits=args.digits,
            use_symbols=args.symbols,
        )
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
