from sklearn.tree import DecisionTreeClassifier

# Training data
# Weather: 0 = Sunny, 1 = Overcast, 2 = Rain
# Temperature: 0 = Hot, 1 = Mild, 2 = Cool

X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [2, 1],
    [2, 2],
    [2, 1],
    [0, 2]
]

# Play: 0 = No, 1 = Yes
y = [0, 0, 1, 1, 1, 0, 1, 1]

# Create Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)

# User input
weather = int(input("Enter weather (0-Sunny, 1-Overcast, 2-Rain): "))
temperature = int(input("Enter temperature (0-Hot, 1-Mild, 2-Cool): "))

# Prediction
result = model.predict([[weather, temperature]])

if result[0] == 1:
    print("Prediction: YES, You can play")
else:
    print("Prediction: NO, You cannot play")
