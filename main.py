import os.path
import time
from os import listdir

mypath = "C:\\Users\\WorkSpace\\Downloads"


class FileManager:
    def __init__(self, path: str):
        self.mypath = path
        self.file_list = []

    def get_files_list(self):
        try:
            if os.path.isdir(self.mypath):
                for file_name in listdir(self.mypath):
                    file_size = os.path.getsize(self.mypath + "\\" + file_name)
                    file_extension = os.path.splitext(file_name)
                    self.file_list.append(
                        {
                            "file_name": file_extension[0],
                            "file_extension": file_extension[1][1:],
                            "file_size": file_size
                        }
                    )
                return self.file_list
        except Exception as error:
            print(error)

    def file_list_loop(self, timecheck, callback):
        while True:
            callback(self.get_files_list())
            time.sleep(timecheck)


def getcflowfiles(fileslist: list):
    for file in fileslist:
        # From kb to mb
        if file['file_size'] / (1024 * 1024) > 30:
            print("file higher then 30 mb")
            print(f"file size: {file['file_size'] / (1024*1024)}")
            print(f"file name: {file['file_name']}")

file = FileManager(mypath)
print(file.file_list_loop(20, getcflowfiles))
