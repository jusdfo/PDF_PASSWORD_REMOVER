import datetime
import os
import shutil
import subprocess
from pathlib import Path
from time import sleep
import PyPDF2  # 导入PyPDF2，注意区分大小写
from pip._internal.operations.prepare import File

import reg.reg
from file.delete import del2bin


def isEncrypt(pdf_file):
    pdf = open(pdf_file, 'rb')
    try:
        rd = PyPDF2.PdfReader(pdf)
        if rd.is_encrypted:
            print(pdf_file + "被加密")
            return 1
        else:
            return 0
    except:
        print("   Error    ")
        print(" PyPDF2.errors.DependencyError: PyCryptodome is required for AES algorithm  ")
        print(" 已跳过，默认开始解密 ")
        return 1


Download_Dir = reg.reg.getDownloadLoaction()
Path_List = [
    # r"C:\Users\lvjinwei\参考文献",
    #          Download_Dir
            r"C:\Users\lvjinwei\参考文献\大论文"
             # r"C:\Users\lvjinwei\googledrive\lvjinwei97\大论文"
             ]
for path in Path_List:
    if (os.path.exists(path)==False) : continue
    print(path)
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)  # 原始文件全路径
            if file_name.endswith(".pdf") and isEncrypt(file_path):  # 以pdf结尾时处理
                (filename, ext) = os.path.splitext(file_name)
                new_path = file_path + ".tmp"  # 新文件全路径
                print(file_path)
                print(new_path)
                if os.path.exists(new_path):
                    os.remove(new_path)
                starttime = datetime.datetime.now()
                result=os.system('qpdf --decrypt "%s" "%s"' % (file_path, new_path))
                # cmd='qpdf --decrypt '+file_path+" "+new_path;
                # res = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) # 使用管道
                # result = res.stdout.read()  # 获取输出结果
                # res.wait()  # 等待命令执行完成
                # res.stdout.close() # 关闭标准输出
                # print(result)
                # while(os.path.exists(new_path)==False):
                #     sleep(5)
                endtime = datetime.datetime.now()
                print (endtime - starttime)

                del2bin(file_path)
                shutil.move(new_path, file_path)
        # os.remove(file_path)  # 删掉原始文件，如果怕误删，注释掉这一行
