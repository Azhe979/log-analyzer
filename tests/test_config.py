from pathlib import Path
import yaml

from log_analyzer.config import load_config


def test_load_valid_config(tmp_path: Path):
    config_data = {
        "log": {"level": "INFO"},
        "input": {"paths": ["a.log"]},
    }

    config_file = tmp_path / "config.yaml"
    config_file.write_text(yaml.dump(config_data), encoding="utf-8")

    config = load_config(str(config_file))

    assert config["log"]["level"] == "INFO"
    assert config["input"]["paths"] == ["a.log"]


def test_load_missing_config_file():
    try:
        load_config("not_exist.yaml")
    except FileNotFoundError:
        assert True
    else:
        assert False
