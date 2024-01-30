from sklearn.ensemble import RandomForestRegressor

# Load your data and split it into features and target variables
# X_train, X_test, y_train, y_test = ...

# Create a random forest regressor object
rf = RandomForestRegressor()

# Train the model
rf.fit(X_train, y_train)

# Make predictions
predictions = rf.predict(X_test)

# Evaluate the model
score = rf.score(X_test, y_test)

# Print the score
print("R^2 score:", score)
