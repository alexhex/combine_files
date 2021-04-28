# -*-coding:utf-8-*-

import os
import re
import shutil
import os

# 1. Ask for address of dir A;
# 2. Ask for address of dir B;
# 3. Go thru the 2 folders and get a list of the files in each folder;
# 4. Compare the files and set up a pair;
# 5. List the changes to the user and ask for confirmation;
# 6. If confirmed, start copying and replacing the files;
# 7. List the changes to a txt file for check;


# Reference: https://zhuanlan.zhihu.com/p/56909212


class File_Checker():
    def __init__(self):
        self.dest_folder = ''
        self.res_folder = ''
        self.pdf_files_to_be_rpl = []
        self.pdf_files_resource = []
        self.file_pair = {}
        self.log = ''
        self.errorlog = ''

    def reset(self):
        self.dest_folder = ''
        self.res_folder = ''
        self.pdf_files_to_be_rpl = []
        self.pdf_files_resource = []
        self.file_pair = {}
        self.log = ''
        self.errorlog = ''

    # 1&2;
    def get_dest_fldr(self, fldr):
        # self.dest_folder = input("请输入准备寄送的文件夹： ")
        self.dest_folder = fldr

    def get_rsc_fldr(self, fldr):
        # self.res_folder = input("请输入含有所需文件的文件夹：")
        self.res_folder = fldr

    # 3. Go thru the 2 folders and get a list of the files in each folder;
    def list_pdf_files(self, folder, pttrn):
        file_lst = []
        for rootpath, dirs, files in os.walk(folder):
            for name in files:
                # match_obj = re.search(pttrn, name)
                # Case Insensitive
                match_obj = re.search(pttrn, name, re.I)
                if match_obj:
                    # print(os.path.join(rootpath, name))
                    # name = re.sub(r"_Smith", '', name)
                    file_lst.append(
                        os.path.join(rootpath, name))
        return file_lst

    def get_files_ready(self):
        self.pdf_files_to_be_rpl = self.list_pdf_files(
            self.dest_folder, r'_Smith.pdf$')
        self.pdf_files_resource = self.list_pdf_files(
            self.res_folder, r'.pdf$')

    # 4. Go thru the list and search for the replacement file in the B folder;

        for file_a in self.pdf_files_to_be_rpl:
            for file_b in self.pdf_files_resource:
                # if the filename without '_smith' is the same with the filename in resource pool, set up a pair
                if os.path.basename(re.sub(r'_Smith', '', file_a)).lower() == os.path.basename(file_b).lower():
                    self.file_pair[file_a] = file_b

    # 5. List the changes to the user and ask for confirmation;

    def generate_log(self):
        for lmnt in self.pdf_files_to_be_rpl:
            if lmnt in self.file_pair.keys():
                self.log += f'{os.path.basename(lmnt)} would be replaced;\r\n'
            else:
                self.log += f'{os.path.basename(lmnt)} is NOT found;\r\n'
        return (self.log)


# 6. If confirmed, start copying and replacing the files;


    def replace_files(self):
        for key in self.file_pair.keys():
            # Instead of covering the original files, we delete the "Smith" files and make copies of
            # the original files. This would be a hint to the user.
            # shutil.copy(file_pair[key], key)
            shutil.copy(self.file_pair[key], os.path.dirname(key))
            try:
                os.remove(key)
            except OSError as e:
                self.errorlog += f'Error: {key} : {e.strerror}'


# my_file_checker = File_Checker()
# my_file_checker.get_dest_fldr(
#     r'C:\Users\neil\OneDrive\文档\Desktop\Smith Folder')
# my_file_checker.get_rsc_fldr(
#     r'C:\Users\neil\OneDrive\文档\Desktop\Need Replace Folder')
# my_file_checker.get_files_ready()
# print(my_file_checker.generate_log())

# ans = input('do you wanna proceed? y/n')
# if ans.lower() == 'y':
#     my_file_checker.replace_files()
# else:
#     pass

# [a, b] = ask_for_folders()
# file_tb_rpl = list_pdf_files_to_be_rpl(a)
# file_pair_inst = find_rpl_files(file_tb_rpl, b)
# print(generate_log(file_tb_rpl, file_pair_inst))
# ans = input('do you wanna proceed? y/n')
# if ans.lower() == 'y':
#     replace_files(file_pair_inst)
# else:
#     pass
