import yaml
from typing import Any

def create_connection_string(user: str, password: str, host: str, port: int, database: str) -> str:
    """Create connection string for a postgres database."""
    return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

def read_config(path: str) -> dict[str,Any]:
    """Read safely config file."""
    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)