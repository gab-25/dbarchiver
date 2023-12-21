from abc import ABC, abstractmethod
import datetime
import os
import subprocess


class AbstractDatabseClient(ABC):
    def __init__(self, dump_tool: str, restore_tool: str):
        self.tools = {"dump": dump_tool, "restore": restore_tool}
        self.out_directory = os.path.expanduser("~").join("dumps")

        self.__check_tools()
        self.__check_out_directory()

    def __check_tools(self):
        for tool in self.tools.values():
            try:
                subprocess.run([tool, "--version"], check=True)
            except subprocess.CalledProcessError as exc:
                raise Exception(f"{tool} not installed!") from exc

    def __check_out_directory(self):
        if not os.path.exists(self.out_directory):
            os.mkdir(self.out_directory)

    def get_dump_tool(self) -> str:
        return self.tools.get("dump")

    def get_restore_tool(self) -> str:
        return self.tools.get("restore")

    def generate_file_archive(self, dbname: str):
        return f"{self.out_directory}/{dbname}_{datetime.datetime.today().strftime('%Y%m%d%H%M')}.dbarchive"

    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def restore(self):
        pass
