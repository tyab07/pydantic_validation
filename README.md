# pydantic-validation

Professional, well-documented utilities and examples for data validation using Pydantic.

This repository contains Pydantic models, validation helpers, configuration patterns, and example usages designed to make robust data validation straightforward in Python applications.

Badges

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![Build Status](https://img.shields.io/badge/ci-pending-lightgrey)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-green)]()

Project status

Production-ready foundations. Core models and utilities are implemented; tests and CI are included to ensure reliability.

Table of contents

- Quickstart
- Installation
- Examples
- Project layout
- Usage
- Configuration
- Testing & CI
- Contributing
- Release & Changelog
- License
- Maintainers

Quickstart

Install the package (editable) and run basic examples:

```bash
pip install -e .
```

Example:

```python
from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    email: str

try:
    user = User(id=1, name="Alice", email="alice@example.com")
    print(user.json(indent=2))
except ValidationError as e:
    print(e.json())
```

## Installation

Recommended (development):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

Or install from PyPI (when published):

```bash
pip install pydantic-validation
```

## Usage

- Import models from `pydantic_validation.models` and use them for request/response validation.
- Use `Model.parse_obj(...)` to coerce dictionaries into typed models.
- Use model `.dict()` / `.json()` for serialization.

## Examples

See the `examples/` directory for small, focused demonstrations showing common patterns:

- examples/api_validation.py — request/response validation
- examples/settings_example.py — BaseSettings usage for application configuration
- examples/coercion_examples.py — parsing and coercing untrusted input

## API Reference & Project Structure

- `models/` — Pydantic models and validators
- `utils/` — helper functions for coercion and common validators
- `settings/` — typed application settings using BaseSettings

Provide detailed docstrings for exported models and functions.

## Testing

Run the test suite locally:

```bash
pytest -q
```

## Continuous Integration

- A GitHub Actions workflow runs tests on push and PRs.
- Ensure linting and type checks pass before merging.

## Contributing

Contributions are welcome. Please follow these steps:

1. Open an issue to discuss larger changes before implementing.
2. Create a branch per change: `git checkout -b feat/short-description`.
3. Follow conventional commits for messages: `feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`.
4. Add or update tests and documentation for any change that affects behavior.
5. Open a pull request referencing the issue and describing the change.

## Release & Changelog

- Follow semantic versioning.
- Keep `CHANGELOG.md` updated with notable changes for each release.

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Maintainers

- Maintainer Name <maintainer@example.com>
