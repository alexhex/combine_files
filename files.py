# -*-coding:utf-8-*-

import os
import re

# 1. Ask for address of dir A;
# 2. Ask for address of dir B;
# 3. Scan the whole A dir and get a list of pdf files.
# 4. Go thru the list and search for the replacement file in the B folder;
# 5. List the changes to the user and ask for confirmation;
# 6. If confirmed, start copying and replacing the files;
# 7. List the changes to a txt file for check;


# Reference: https://zhuanlan.zhihu.com/p/56909212
# 1&2;
dest_folder = input("请输入准备寄送的文件夹")

res_folder = input("请输入含有所需文件的文件夹")

# 3


def list_pdf_files(address_a):
    for rootpath, dirs, files in os.walk(address_a):
        for name in files:
            match_obj = re.search(r"pdf$", name)
            if match_obj:
                print(os.path.join(rootpath, name))


list_pdf_files(dest_folder)
