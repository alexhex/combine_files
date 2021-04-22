# -*-coding:utf-8-*-

import os
import re
import shutil

# 1. Ask for address of dir A;
# 2. Ask for address of dir B;
# 3. Scan the whole A dir and get a list of pdf files.
# 4. Go thru the list and search for the replacement file in the B folder;
# 5. List the changes to the user and ask for confirmation;
# 6. If confirmed, start copying and replacing the files;
# 7. List the changes to a txt file for check;


# Reference: https://zhuanlan.zhihu.com/p/56909212

# 1&2;
def ask_for_folders():
    dest_folder = input("请输入准备寄送的文件夹： ")
    res_folder = input("请输入含有所需文件的文件夹：")
    return [dest_folder, res_folder]

# 3. Scan the whole A dir and get a list of pdf files.


def list_pdf_files_to_be_rpl(address_a):
    pdf_files_to_be_rpl = []
    for rootpath, dirs, files in os.walk(address_a):
        for name in files:
            # match_obj = re.search(r"pdf$", name)
            match_obj = re.search(r"_Smith.pdf$", name, re.I)
            if match_obj:
                # print(os.path.join(rootpath, name))
                # name = re.sub(r"_Smith", '', name)
                pdf_files_to_be_rpl.append(os.path.join(rootpath, name))
    return (pdf_files_to_be_rpl)


# for lmnt in list_pdf_files_to_be_rpl(dest_folder):
#     print(lmnt)
#     print(os.path.basename(lmnt))


# 4. Go thru the list and search for the replacement file in the B folder;
def find_rpl_files(lst, address_b):
    # pass
    file_pair = {}
    pdf_files_resource = []
    for rootpath, dirs, files in os.walk(address_b):
        for name in files:
            match_obj = re.search(r".pdf$", name)
            if match_obj:
                # print(os.path.join(rootpath, name))
                # name = re.sub(r"_Smith", '', name)
                pdf_files_resource.append(os.path.join(rootpath, name))
    for file_a in lst:
        for file_b in pdf_files_resource:
            if os.path.basename(re.sub(r'_Smith', '', file_a)).lower() == os.path.basename(file_b).lower():
                file_pair[file_a] = file_b
    return (file_pair)


# for lmnt in list_pdf_files_to_be_rpl(dest_folder):
#     print(lmnt)
#     print(os.path.basename(lmnt))


# 5. List the changes to the user and ask for confirmation;


def generate_log(files_to_be_rpl, file_pair):
    log = ''
    for lmnt in files_to_be_rpl:
        if lmnt in file_pair.keys():
            log += f'{os.path.basename(lmnt)} would be replaced;\r\n'
        else:
            log += f'{os.path.basename(lmnt)} is NOT found;\r\n'
    return (log)


# 6. If confirmed, start copying and replacing the files;

def replace_files(file_pair):
    for key in file_pair.keys():
        # shutil.copy(file_pair[key], key)
        shutil.copy(file_pair[key], os.path.dirname(key))
        try:
            os.remove(key)
        except OSError as e:
            print(f'Error: {key} : {e.strerror}')


[a, b] = ask_for_folders()
file_tb_rpl = list_pdf_files_to_be_rpl(a)
file_pair_inst = find_rpl_files(file_tb_rpl, b)
print(generate_log(file_tb_rpl, file_pair_inst))
ans = input('do you wanna proceed? y/n')
if ans.lower() == 'y':
    replace_files(file_pair_inst)
else:
    pass
