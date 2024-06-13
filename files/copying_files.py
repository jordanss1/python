import shutil
import os

scr = "files/new.txt"
dst = "files/new_copy.txt"
shutil.copy(scr, dst)

os.rename(dst, "./files/new_copy_renamed.txt")

os.remove("./files/new_copy_renamed.txt")

src = "files/new2.txt"
dest = "files/new2_copy.txt"

shutil.copy(src, dest)

os.rename(dest, "files/new2_copy_renamed.txt")

open("files/process/process.txt", "x").close()

with open("files/process/process.txt", "w") as myfile: 
    myfile.write("Process started:\n Begin Processing\n")
    myfile.close()
    shutil.copy("files/process/process.txt", "files/process/process_copy.txt")

with open("files/process/process_copy.txt", "a") as myfile:
    myfile.write("End Processing\n")



