from dataclasses import dataclass, field
import yaml
import os


@dataclass
class Config:
    __config_file: str = "config.yml"
    config_parameters: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        with open(self.config_file, "r") as config_file:
            self.config_parameters = yaml.safe_load(config_file)

    def get_parameter(self, parameter_name: str = None) -> str | int:
        if parameter_name in self.config_parameters:
            return self.config_parameters[parameter_name]
        else:
            raise ValueError("Unknow parameter")

    @property
    def config_file(self) -> str:
        if os.path.exists(self.__config_file):
            return self.__config_file
        else:
            raise FileExistsError("Configuration file does not exist")

    @config_file.setter
    def config_file(self, config_file: str) -> str:
        if os.path.exists(config_file):
            self.__config_file = config_file
            return self.__config_file
        else:
            raise FileExistsError("Configuration file does not exist")
