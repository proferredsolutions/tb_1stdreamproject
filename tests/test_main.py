import pytest
from src.main import load_config
import os

def test_load_config():
    # Test loading the existing config.yaml
    config = load_config('config.yaml')
    assert 'name' in config
    assert config['name'] == '1stdreamproject'
    assert 'notification' in config
    assert 'email' in config['notification']
