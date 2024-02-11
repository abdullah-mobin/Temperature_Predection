from src.preprocessing import *
from src.dependencies import *

# split

X = temperature_dataset[['date','time']]
Y = temperature_dataset.drop(columns = ['date','time'])

# print (X)
# print (Y)


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)

# print(Y_train.shape , Y_test.shape)

# model train

tree_regressor = DecisionTreeRegressor(random_state=42)
tree_regressor.fit(X_train, Y_train)

y_pred_tree = tree_regressor.predict(X_test)
mse = mean_squared_error(Y_test, y_pred_tree)

# print(mse)  --> 4.088401113013699
