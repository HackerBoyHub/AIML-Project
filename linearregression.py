from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
iris = load_iris()
X = iris.data[:, [0, 1, 3]]   
y = iris.data[:, 2]           
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print("Linear Regression (Predicting Petal Length):")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
new_instance = [[1.2, 2.2, 3.3]]
predicted_petal_length = lr.predict(new_instance)
print("Predicted Petal Length for New Instance:", predicted_petal_length)
