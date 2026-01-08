from pathlib import Path
import yaml

def load_config(config_path: str) -> dict:
    """
    Load configuration from a YAML file.

    :param config_path: Path to config file
    :return: config dict
    """
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
        
    with open(path, "r",encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        raise ValueError("Config file must contain a dictionary") 
    
    return config

            
