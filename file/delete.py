import os

from win32comext import shell
from win32comext.shell import shell, shellcon

debug = False


def del2bin(filename):
#https://blog.csdn.net/zonghua521/article/details/127541357
    print('delete file', filename)
    # os.remove(filename) #直接删除文件，不经过回收站
    if not debug:
        res = shell.SHFileOperation((0,shellcon.FO_DELETE, filename, None,
                                    shellcon.FOF_SILENT |shellcon.FOF_ALLOWUNDO |shellcon.FOF_NOCONFIRMATION, None,
                                     None))  # 删除文件到回收站
        if not res[1]:
            os.system('del ' + filename)