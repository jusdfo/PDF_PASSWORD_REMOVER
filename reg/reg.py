import winreg

def getDownloadLoaction():
    DownloadLibraryRegProperty="{374DE290-123F-4565-9164-39C4925E467B}"
    string = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    handle = winreg.OpenKey(winreg.HKEY_CURRENT_USER, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
    location, _type = winreg.QueryValueEx(handle, DownloadLibraryRegProperty)
    return location

