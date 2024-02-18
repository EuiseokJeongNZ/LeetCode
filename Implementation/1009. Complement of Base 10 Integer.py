import os
import datetime as dt

if __name__ == "__main__":
    print("hello")
    source_directory = input()
    try:
        for file in os.listdir(source_directory):
            file_path = os.path.join(source_directory, file)
            file_creation_time = dt.datetime.fromtimestamp(os.path.getctime(file_path))
            print(file + "   " + str(file_creation_time))
    except OSError as error:
        print(error)