from io import StringIO

import sys
import os


class Interpreture:
    """ Logic interpreture for interface """

    def __init__(self) -> None:
        """
        When creating an instance,
        we check if our folder exists and if not,
        we create a working folder 'files'
        """

        if 'files' not in os.listdir():
            os.mkdir("files")

    def create_file(self, file_name: str) -> str:
        """
        Create file in folder 'files'

        :param file_name: File name without python extension
        """

        try:
            if '%s.py' % file_name not in os.listdir(path="files"):
                with open('files/%s.py' % file_name, "w"):
                    return "Успешно создан"
            else:
                return "Файл не существует"
        except Exception as e:
            print(e)
    
    def edit_file(self, txt: str, file_name: str) -> str:
        """
        Editing a file in folder 'files'

        :param txt: Сommands example 'print("Hello")'
        :param file_name: File name without python extension
        """

        try:
            with open('files/%s.py' % file_name, "a") as file:
                file.write(str(txt))
                return "Файл успешно изменен"
        except Exception as e:
            print(e)

    def run_file(self, file_name: str) -> str:
        """
        Run commands and return this

        :param file_name: File name without python extension
        """

        try:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            exec(self.read_file(file_name))
            sys.stdout = old_stdout
            return redirected_output.getvalue().strip()
        except Exception as e:
            print(e)

    def read_file(self, file_name: str) -> str:
        """
        Read file and return this

        :param file_name: File name without python extension
        """

        try:
            if '%s.py' % file_name in os.listdir(path="files"):
                file = open('files/%s.py' % file_name, "r").readlines()
                text = ""
                for i in file:
                    text += i
                return text
            else:
                return "Файл не найдено"
        except Exception as e:
            print(e)
    
    def del_file(self, file_name: str) -> str:
        """
        Delete file

        :param file_name: File name without python extension
        """

        try:
            if '%s.py' % file_name in os.listdir(path="files"):
                os.remove("files/%s.py" % file_name)
                return "Файл успешно удален"
            else:
                return "Файл не существует"
        except Exception as e:
            print(e)
