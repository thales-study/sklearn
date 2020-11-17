# dice.py
from sklearn.svm import SVC

X_train = [# 训练集，输入参数，注意这里的X是大写
  [1,2],
  [5,6]
]
y_train = [0, 1] # y值，结果

ai = SVC() # 定义一个人工智能模型
ai.fit(X_train, y_train) # 让人工智能通过参数和结果找关系

test = [ # 测试
  [1,1],
  [2,3],
  [3,3],
  [2,5],
  [4,3],
  [6,6]
]
res = ai.predict(test) # 预测测试结果
print(res)