import glob
import os.path, fnmatch


def input_function(files,input_string):
  file_list = []
  for file in files:
    if input_string in file:
      file_list.append(file)
  return file_list

def main():
 migrations = 'Migrations'
 i = 1
 files = []
 while i == 1:
   print('Введите слово')
   input_string = input()
   input_string = input_string
   if len(files) == 0:
    files = glob.glob(os.path.join(migrations, input_string))
    print('Cписок файлов, найденных по файл маске ',input_string, ' \n',files)
   else:
    files = input_function(files,input_string)
    print('Cписок файлов, найденных по файл маске ', input_string, ' \n', files)
main()