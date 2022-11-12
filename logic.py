from io import StringIO
import sys
import os


class Interpreture:
    def create_file(self, file_name):
        try:
            if '%s.py' % file_name not in os.listdir():
                with open('%s.py' % file_name, "w"):
                    return "Успешно создан"
            else:
                return "Файл существует"
        except Exception as e:
            return print(e)
    
    def edit_file(self, txt, file_name):
        try:
            with open('%s.py' % file_name, "a") as file:
                file.write(str(txt))
                return print("Файл успешно изменен")
        except Exception as e:
            return print(e)

    def run_file(self, file_name):
        try:
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            exec(self.read_file(file_name))
            sys.stdout = old_stdout
            return redirected_output.getvalue().strip()
        except Exception as e:
            return e

    def read_file(self, file_name):
        try:
            if '%s.py' % file_name in os.listdir():
                file = open('%s.py' % file_name, "r").readlines()
                text = ""
                for i in file:
                    text += i
                return text
            else:
                return "Файл не найдено"
        except Exception as e:
            return e
    
    def del_file(self, file_name):
        try:
            if '%s.py' % file_name in os.listdir():
                os.remove("%s.py" % file_name)
                return "Файл успешно удален"
            else:
                return "Файл не существует"
        except Exception as e:
            return print(e)


i = Interpreture()
