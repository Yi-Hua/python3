#<Numpy> 陣列
#Numpy 的重點在於陣列的操作，其所有功能特色都建築在同質且多重維度的 ndarray（N-dimensional array）上。ndarray 的關鍵屬性是維度（ndim）、形狀（shape）和數值類型（dtype）。 一般我們稱一維陣列為 vector 而二維陣列為 matrix。一開始我們會引入 numpy 模組，透過傳入 list 到 numpy.array() 創建陣列。

# 引入 numpy 模組
import numpy as np
np1 = np.array([1, 2, 3])
np2 = np.array([3, 4, 5])
np3 = np.array([1, 2, 3, 4, 5, 6])

# 陣列相加
print(np1 + np2) # [4 6 8]

# 顯示相關資訊
print(np1.ndim, np1.shape, np1.dtype) # 1 (3,) int64 => 一維陣列, 三個元素, 資料型別


#從檔案取資料：
npd = np.genfromtxt('data.csv', delimiter =',')

#改變陣列維度：
np3 = np3.reshape([2, 3])
print(np3.ndim, np3.shape, np3.dtype) # 2 (2, 3) int64

#改變陣列型別（bool、int、float、string）：
#bool 可以包含 True、False，int 可以包含 int16、int32、int64。其中數字是指 bits。float 可以包含 16、32、64 表示小數點後幾位。string 可以是 string、unicode。nan 則表示遺失值。
np3 = np3.astype('int64')
np3.dtype
# dtype('int64')