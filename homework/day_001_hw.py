# -*- coding: utf-8 -*-
"""Day_001_HW.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EiFVBd_uIAhVgqEVxRSuJwR5VWQhSYAE

## 練習時間
#### 請寫一個函式用來計算 Mean Square Error
$ MSE = \frac{1}{n}\sum_{i=1}^{n}{(Y_i - \hat{Y}_i)^2} $

### Hint: [如何取平方](https://googoodesign.gitbooks.io/-ezpython/unit-1.html)

# [作業目標]
- 仿造範例的MAE函數, 自己寫一個MSE函數(參考上面公式)

# [作業重點]
- 注意程式的縮排
- 是否能將數學公式, 轉換為 Python 的函式組合? (In[2], Out[2])
"""

# 載入基礎套件與代稱
import numpy as np
import matplotlib.pyplot as plt

def mean_absolute_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

# 定義 mean_squared_error 這個函數, 計算並傳回 MSE
def mean_squared_error(y, yp):
    """
    計算 MSE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mse: MSE
    """
    mse = MSE = sum((y - yp)**2) / len(y)
    return mse

# 與範例相同, 不另外解說
w = 3
b = 0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()

# 與範例相同, 不另外解說
y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()

# 執行 Function, 確認有沒有正常執行
MSE = mean_squared_error(y, y_hat)
MAE = mean_absolute_error(y, y_hat)
print("The Mean squared error is %.3f" % (MSE))
print("The Mean absolute error is %.3f" % (MAE))

"""# [作業2]

請上 Kaggle, 在 Competitions 或 Dataset 中找一組競賽或資料並寫下：

1. 你選的這組資料為何重要
> 我選擇的是House Prices: Advanced Regression Techniques
> 這數據集是個貼近實際的案例，透過與房屋價格相關的資料，來預測房屋的價格，這是回歸的問題，剛好也是上述ＭＳＥ與ＭＡＥ的評估標的：回歸模型

2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
> The Ames Housing dataset was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset. 

3. 蒐集而來的資料型態為何
> 這資料有訓練集也有測試集，資料型態大多數為類別型資料，也有數字型資料，最終預測的是SalePrice

4. 這組資料想解決的問題如何評估
> 這是有關於房價預測的操作思路，在最一開始，先針對整個資料集提供的資訊進行研究，再者將資料型態記錄下來，並思考每個欄位如果有空值時，要如何做補值，如果資料內的數值有空值，模型便沒辦法針對我們的資料集做預測，接著，做特徵工程最重要的目的在於，能否找到更多更好的方式，去描述我們想要預測的標的，例如：取對數的好處最主要在於：可以減少極端值對模型的影響，也可以讓偏態的參數分布更接近一般常態分佈的樣子，這些好處則可以提升模型預測的表現，在做完特徵工程之後，就可以正式的使用模型進行預測了。

# [作業3]

想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：

1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
> 利潤最大化

2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
> 是否能搜集到相關的乘車資訊，甚至可以搜集到乘客資訊

3. 蒐集而來的資料型態為何
> 資料型態為車隊車輛數，載客數，載客時間，等待時間，區域，路線類型（高速或平面），距離，車資，油耗等類別與數值資料

4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
> 利潤=收入-成本，成本來至於油錢與維護，收入來自於總車資，所以透過資料收集，看看哪些因素會影響油錢，維護費與總車資，透過歷史數據建立預測模型，並持續收集資料來調整模型，最終使車隊利潤最大化
"""