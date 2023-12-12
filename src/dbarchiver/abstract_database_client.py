from abc import ABC, abstractmethod
import subprocess


class AbstractDatabseClient(ABC):
    def __init__(self, dump_tool: str, restore_tool: str):
        self.tools = {
            "dump": dump_tool,
            "restore": restore_tool
        }

        self.__check_tools()

    def __check_tools(self):
        for tool in self.tools.values():
            try:
                subprocess.run([tool, "--version"], check=True)
            except subprocess.CalledProcessError as exc:
                raise Exception(f"{tool} not installed!") from exc

    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def restore(self):
        pass
