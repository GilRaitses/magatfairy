# Contributing to mat2h5

Thank you for your interest in contributing to mat2h5!

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/GilRaitses/mat2h5.git
cd mat2h5
```

2. Install dependencies:
```bash
python install.py
```

3. Ensure MATLAB Engine for Python is installed (see README.md)

## Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to all functions and classes
- Keep functions focused and modular

## Testing

Run the validation framework to ensure conversions work correctly:
```bash
cd validation
python run_full_validation.py
```

## Submitting Changes

1. Create a feature branch from `main`
2. Make your changes
3. Test thoroughly
4. Submit a pull request with a clear description of changes

## Reporting Issues

Please use GitHub Issues to report bugs or request features. Include:
- Description of the issue
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version, MATLAB version)

