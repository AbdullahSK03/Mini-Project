from cx_Freeze import setup, Executable

setup(name='your_file_name',
      version='0.1',
      description='Description of your file',
      executables=[Executable('app.py')])
