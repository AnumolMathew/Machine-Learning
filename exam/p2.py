import pandas as pd

data=pd.read_csv("iris.csv")
x=data.iloc[ : ,:-1].values
y=data.iloc[ : ,4].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print("predicted values are : \n",y_pred)

from sklearn.metrics import accuracy_score,confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print("\n confusion matrix is :\n {}".format(cm))
print("\n Accuracy is : {}".format(accuracy_score(y_test,y_pred)))
df=pd.DataFrame({'actual values :':y_test, "predicted values: ":y_pred})
print("\n{}".format(df))



