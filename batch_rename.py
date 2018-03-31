# <Batch ReName> 批量重新命名


import os   #os:刪除、重新命名、切換路徑、遍歷目錄
#os.rename(sourece, dest) - 更改資料夾或檔案的名稱(從source改成dest)
#os.listdir(dir_path) - 回傳一個list包涵dir_path資料夾中的所有檔案名稱


pic_name = "catbox"
file_name = "Catbox"  


def batch_rename(path):
    count = 0
    for fname in os.listdir(path):
        new_fname = "{}{}.jpg".format(pic_name,str(count))
        print(os.path.join(path, fname))
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        count = count + 1

file_path = ('C:/Users/yi-hua/Desktop/ImageNet/{}'.format(file_name))
batch_rename(file_path)
