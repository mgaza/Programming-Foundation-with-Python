import os

def rename_file():
    # Open files from a folder
    file_list = os.listdir("prank")
    os.chdir("prank")

    # rename each file
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print file_name+" has been changed into "+file_name.translate(None,"0123456789")

rename_file()
