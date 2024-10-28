import yaml
import os

def read_config():
    """
    Reads a .yml configuration file and returns its contents as a dictionary.

    Returns:
    - dict: The contents of the .yml file as a dictionary.
    """
    
    file_path=os.path.join(os.path.dirname(__file__),'configs.yml')
    
    with open(file_path, 'r') as file:
        try:
            config = yaml.safe_load(file)
            return config
        except yaml.YAMLError as e:
            raise ValueError(f"Error reading the YAML configuration file: {e}")
