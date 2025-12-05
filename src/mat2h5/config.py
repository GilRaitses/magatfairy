"""
Configuration management for mat2h5.
Saves user preferences to ~/.mat2h5/config.json
"""

import json
import os
from pathlib import Path
from typing import Optional, Dict


CONFIG_DIR = Path.home() / ".mat2h5"
CONFIG_FILE = CONFIG_DIR / "config.json"


def ensure_config_dir():
    """Ensure config directory exists"""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> Dict:
    """Load configuration from file"""
    ensure_config_dir()
    
    if not CONFIG_FILE.exists():
        return {}
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def save_config(config: Dict):
    """Save configuration to file"""
    ensure_config_dir()
    
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)


def get_config(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get a configuration value"""
    config = load_config()
    return config.get(key, default)


def set_config(key: str, value: str):
    """Set a configuration value"""
    config = load_config()
    config[key] = value
    save_config(config)


def get_magat_codebase() -> Optional[Path]:
    """Get MAGAT codebase path from config or environment"""
    path = get_config('magat_codebase') or os.environ.get('MAGAT_CODEBASE')
    if path:
        return Path(path)
    return None


def set_magat_codebase(path: Path):
    """Set MAGAT codebase path in config"""
    set_config('magat_codebase', str(path))


def get_default_output() -> Optional[Path]:
    """Get default output directory from config"""
    path = get_config('default_output')
    if path:
        return Path(path)
    return None


def set_default_output(path: Path):
    """Set default output directory in config"""
    set_config('default_output', str(path))

