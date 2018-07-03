import os, re
from time import sleep, ctime
import FILE_TRACKER_CONFIG # configuaration file 
# it lists file exentions and corresponding actions

path = "dir/" # "." to use dir of the location of File Tracker.py 

interval = 10 # pause time, in seconds

if not os.path.exists(path):
    os.mkdir(path)

files = os.listdir(path) # list elements in the folder

print("Files and dirs that were present at the beginning", files)

while 1:
    sleep(interval) # update every .. seconds
    
    files_update = os.listdir(path) # list the directory
    # check for new files 
    new_files_dirs = [f for f in files_update if f not in files]
    
    if new_files_dirs != []:
        files = files_update
        
        print("\nThere are changes in", path)
        print(new_files_dirs)
        
        file_generator = (elem for elem in new_files_dirs if os.path.isfile(path + elem)) # only new files, skip new dirs
        # walking through all the new files
        for f in file_generator:
            print("New file {} detected...".format(f))
            resolution = re.search('\.(.+)$', f).group(1) # (extension)
            try:
                instruction = FILE_TRACKER_CONFIG.INSTRUCTION[resolution].split(" ")
            except KeyError:
                print("Unexpected file resolution {}, " + 
                "nothing happens for file {}".format(resolution, f))
                continue
            action = instruction[0] # first part of the instruction
            # taking action
            print("Program does", instruction, "for file ", f)
            if action == "add-date-to-name":
                newname = ctime(os.path.getctime(path + f))+ " " + f
                os.rename(path + f, path + newname)
                files.append(newname) # otherwise program will consider it
                # as a new file, in fact it is old but renamed file
            elif action == "move-to-folder":
                folder = os.path.join(path,instruction[1])
                if not os.path.exists(folder):
                    os.mkdir(folder)
                os.rename(path + f, os.path.join(folder,f))
            elif action == "copy-to-folder":
                folder = os.path.join(path,instruction[1])
                if not os.path.exists(folder):
                    os.mkdir(folder)
                destination = os.path.join(folder,f)
                # not memory-time effective method, but platform independent
                ##   with open(f, 'r') as s, open(destination, 'w') as d:
                ##       d.write(s.read())
                # copy using console
                bash_copy = 'cp "{}" "{}"'.format(path + f, destination)
                os.system(bash_copy) # to run on windows replace cp with copy
            elif action == "trash":
                # moving to the hidden folder
                folder = os.path.join(path, ".Trash")
                if not os.path.exists(folder):
                    os.mkdir(folder)
                os.rename(path + f, os.path.join(folder,f))
            else:
                pass # doing nothing (as for .py files)
            
            print("\nNext check in {} seconds".format(interval))        
