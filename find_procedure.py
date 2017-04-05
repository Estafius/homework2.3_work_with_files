import glob
import os.path


def input_function(files,input_string):
  file_list = []
  for file in files:
   file = file.replace("Migrations\\","")
   with open(file) as original_file:
    file_content = original_file.readlines()
    for line in file_content:
        if input_string in line:
         file_list.append(file)
  return list(dict.fromkeys(file_list))

def main():
 os.chdir('Migrations')
 files = glob.glob(os.path.join('', '*sql'))
 while True:
    print('Введите слово')
    input_string = input()
    files = input_function(files,input_string)
    print('Cписок файлов, найденных по файл маске ', input_string, ' \n', files)
main()