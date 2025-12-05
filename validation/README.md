# Validation Scripts

This directory contains validation scripts for verifying H5 conversion correctness.

For documentation, see [docs/VALIDATION.md](../docs/VALIDATION.md).

## Quick Reference

- **Full validation**: `python run_full_validation.py --base-dir /path/to/data`
- **Schema check**: `python python/validate_h5_schema.py /path/to/file.h5`
- **Compare outputs**: `python compare_real_data.py`
