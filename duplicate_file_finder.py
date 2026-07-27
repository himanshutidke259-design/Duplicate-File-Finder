import os
file_path = "/storage/emulated/0/"
list = os.listdir(file_path)
Duplicate = []
seen = {}
for file in list:
    full_path = os.path.join(file_path,file)
    
    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)
        
        if size in seen:
            Duplicate.append(full_path)
        else:
            seen[size] = full_path 
            
for d in Duplicate:
    print(d)          