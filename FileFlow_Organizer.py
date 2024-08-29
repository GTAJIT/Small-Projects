import os
import time
class FileRenamer:
    def __init__(self, dict, format): #data input
        self.dict = dict
        self.format = format
        
    def Get_Files(self): 
        try:
            info = os.listdir(self.dict)
            files = [f for f in info if f.endswith(self.format)]
            file_creation_times = {} #getting the set
            for file in files:
                file_path = os.path.join(self.dict , file)
                if os.path.isfile(file_path):
                    creation_time = os.path.getctime(file_path) #getting the last metadata change time
                    readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(creation_time))
                    file_creation_times[file] = readable_time #changing the format of ctime to readable format
                    sorted_array = {k: v for k, v in sorted(file_creation_times.items(), key=lambda item: item[1])} #sorting the set
                    file_list = [] #making the sortd set to list with the files only
                    for i in sorted_array:
                        file_list.append(i)
            return file_list #returning the list to Get_Files
        
        except FileNotFoundError:
            return (f"The directory {self.dict} does not exist.")
        except Exception as e:
            return (f"Unexpected Error {e}")
        
    def Rename_Files(self):
        file_creation_list = self.Get_Files() #getting the data from Get_files to Rename_Files
        
        if isinstance(file_creation_list, list):
            for index, file in enumerate(file_creation_list, start=1):
                original_path = os.path.join(self.dict, file)
                new_name = f"{index}{self.format}"
                new_path = os.path.join(self.dict, new_name)
                try:
                    os.rename(original_path, new_path)
                    print(f"Renamed: {file} --> {new_name}")
                except Exception as e:
                    print(f"Error renaming {file}: {e}")
        else:
            print(file_creation_list)
a = input("Paste The Direcory: ")
b = input("Give The Format: ")
r = FileRenamer(a,b)
r.Rename_Files()