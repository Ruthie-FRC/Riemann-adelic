# Contributing

Contributions to this research project are welcome. Please read these guidelines before submitting a pull request.

## Before Contributing

- Open an issue to discuss significant changes before starting work.
- Search existing issues and pull requests to avoid duplicates.
- All mathematical claims should be precise and verifiable.

## Code Standards

- Python: follow PEP 8, use type hints where appropriate.
- Run `pytest tests/` before submitting — all existing tests should pass.
- Run `flake8` to check style.

## Mathematical Content

- New validation scripts go in `scripts/validation/`.
- New formal proofs go in `formalization/lean/`.
- If you add or modify a Lean proof, document which lemmas use `sorry` and why.
- Numerical results should specify precision and method.

## Commit Messages

Use clear, descriptive commit messages. Describe what changed and why.

## Pull Request Template

When opening a PR, describe:
1. What mathematical property or claim is being tested or proved.
2. How the change was validated.
3. Any known limitations.
