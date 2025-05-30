from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
print("Some changes made on github")
print("Model accuracy:", clf.score(X_test, y_test))
