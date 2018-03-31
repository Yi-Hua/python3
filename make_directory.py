#<Make a New Directory> 

# https://docs.python.org/3.0/library/os.path.html#module-os.path

import os   #os:刪除、重命名、切換路徑、遍歷目錄
#os.rename(sourece, dest) - 更改資料夾或檔案的名稱(從source改成dest)
#os.listdir(dir_path) - 回傳一個list包涵dir_path資料夾中的所有檔案名稱

dir_name = "Catbox"
if not os.path.exists(dir_name):    #先確認資料夾是否存在
    os.makedirs(dir_name)

open(dir_name + "/" + dir_name + ".txt", "w")
#要寫入什麼而開對應的mode，這邊假設是純文字而開w

#   'r' open for reading (default)
#   'w' open for writing, truncating the file first
#   'x' open for exclusive creation, failing if the file already exists
#   'a' open for writing, appending to the end of the file if it exists
#   'b' binary mode
#   't' text mode (default)
#   '+' open a disk file for updating (reading and writing)
#   'U' universal newlines mode (deprecated)
