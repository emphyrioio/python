from dataclasses import dataclass, field
import yaml


@dataclass
class Config:
    _config_file: str = "config.yml"

    config_parameters: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        with open(self.config_file, "r") as config_file:
            self.config_parameters = yaml.safe_load(config_file)

    def get_parameter(self, parameter_name=None) -> str | int | None:
        if parameter_name in self.config_parameters:
            return self.config_parameters[parameter_name]
        else:
            raise ValueError("Unknow parameter")

    @property
    def config_file(self):
        return self._config_file
