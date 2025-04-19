import shutil
import os
import sys
from datetime import datetime

print("This script is to take back of directories")

def backup_files(source , destination):
    print ("Source Dir: " , source)
    print("Destination Dir: ",destination)
    try:      
         if os.path.exists(destination):
            print ("Destination Dir Present")
            for file in os.listdir(source):
               source_file = os.path.join(source,file)
               destination_file = os.path.join(destination,file)
               if os.path.isfile(destination_file):
                  print(f"File{destination_file} exists, amneding timestamp")
                  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                  base, ext = os.path.splitext(destination_file)
                  destination_file = f"{base}_{timestamp}{ext}"
                  shutil.copy2(source_file,destination_file)
               else:
                  print(f"Copied File {destination_file}")
                  shutil.copy2(source_file,destination_file)
             
         else:
            shutil.copytree(source,destination)
    except FileNotFoundError:
      print (f"Dir/File {source} not found") 
    

if __name__ == "__main__":
   if len(sys.argv) != 3:
        print("Format: python backup.py /path/to/source /path/to/destination")
   else:
      source = sys.argv[1]
      destination = sys.argv[2]
      backup_files(source, destination)

