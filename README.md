# Python Password Generator

A simple command-line tool that creates random passwords using Python's standard library.

## Features
- Configurable password length (defaults to 12 characters).
- Optional uppercase letters, digits, and special symbols.
- Warning when only lowercase letters are selected.
- Uses `random.SystemRandom` for cryptographically stronger randomness.

## Requirements
- Python 3.8 or newer.

## Usage
```bash
python password_generator.py --length 16 --uppercase --digits --symbols
```

### Arguments
- `--length`: Password length (defaults to 12).
- `--uppercase`: Include uppercase characters `A-Z`.
- `--digits`: Include numeric characters `0-9`.
- `--symbols`: Include punctuation characters such as `!@#$%^&*`.

If you omit `--uppercase`, `--digits`, and `--symbols`, the script will generate a password using only lowercase letters and display a warning.

## Example
```bash
$ python password_generator.py --digits
Warning: Generating password using only lowercase letters.
gpxtrfnrghkc
```

## License
This project is licensed under the MIT License.
