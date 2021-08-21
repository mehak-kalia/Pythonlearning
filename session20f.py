import os

print(os.name)

print(os.getlogin())
print(os.getppid())
print("current working directory",os.getcwd())

path_to_directory = r"C:\Users\Lenovo\Downloads"
path_to_file = r"C:\Users\Lenovo\Downloads\certificate"

print(os.path.isdir(path_to_directory))
print(os.path.isfile(path_to_file))

files = os.walk(path_to_directory)
all_files = list(files)

for file in all_files:
    print(file)
