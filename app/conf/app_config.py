from dataclasses import dataclass
from pathlib import Path

from omegaconf import OmegaConf


@dataclass
class File:
    enable: bool
    level: str
    path: str
    rotation: str
    retention: str

@dataclass
class Console:
    enable: bool
    level: str

@dataclass
class LoggingConfig:
    file: File
    console: Console

@dataclass
class AppConfig:
    logging: LoggingConfig

config_file = Path(__file__).parents[2] / "conf" / "app_config.yaml"
context = OmegaConf.load(config_file)
schema = OmegaConf.structured(AppConfig)
merged = OmegaConf.merge(schema, context)
cfg = OmegaConf.to_object(merged)

if __name__ == "__main__":
    print(context)
    print("aaa")
    print(schema)
    print("aaa")
    print(merged)
    print("aaa")
    print((cfg), cfg.logging.file.path)
