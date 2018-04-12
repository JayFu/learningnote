# 尝试用决策树模型对于鸢尾花数据集进行预测

from __future__ import print_function
import sklearn
import numpy
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import tree

iris = datasets.load_iris()
# 导入鸢尾花数据集
iris_X = iris.data
iris_y = iris.target

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
# 将数据集划分成训练集和测试集，测试集占30%

knn = KNeighborsClassifier()
# 使用这个模型
knn.fit(X_train, y_train)
# 训练
print(knn.predict(X_test))
# 预测并打印
print(y_test)
# 预期结果