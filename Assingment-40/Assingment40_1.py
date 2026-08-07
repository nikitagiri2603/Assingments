# ==========================================================
# Additional Decision Tree Assignment
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("student_performance_ml.csv")

X = df.drop("FinalResult", axis=1)
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)

# ==========================================================
# 1. Feature Importance
# ==========================================================

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

importance = model.feature_importances_

for feature, value in zip(X.columns, importance):
    print(feature, ":", round(value, 4))

max_index = importance.argmax()
min_index = importance.argmin()

print("\nMost Important Feature :", X.columns[max_index])
print("Least Important Feature :", X.columns[min_index])

# ==========================================================
# 2. Remove SleepHours
# ==========================================================

print("\n" + "=" * 60)
print("REMOVE SleepHours")
print("=" * 60)

X2 = df.drop(["SleepHours", "FinalResult"], axis=1)

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(
    X2, Y, test_size=0.3, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train2, Y_train2)

pred2 = model2.predict(X_test2)

acc2 = accuracy_score(Y_test2, pred2)

print("Original Accuracy :", round(accuracy * 100, 2), "%")
print("Without SleepHours :", round(acc2 * 100, 2), "%")

if acc2 >= accuracy:
    print("Removing SleepHours does not reduce performance.")
else:
    print("SleepHours contributes to prediction.")

# ==========================================================
# 3. Only StudyHours and Attendance
# ==========================================================

print("\n" + "=" * 60)
print("ONLY TWO FEATURES")
print("=" * 60)

X_small = df[["StudyHours", "Attendance"]]

X_train3, X_test3, Y_train3, Y_test3 = train_test_split(
    X_small, Y, test_size=0.3, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X_train3, Y_train3)

pred3 = model3.predict(X_test3)

acc3 = accuracy_score(Y_test3, pred3)

print("Full Feature Accuracy :", round(accuracy * 100, 2), "%")
print("Two Feature Accuracy :", round(acc3 * 100, 2), "%")

# ==========================================================
# 4. Predict 5 New Students
# ==========================================================

print("\n" + "=" * 60)
print("NEW STUDENTS")
print("=" * 60)

new_students = pd.DataFrame({
    "StudyHours":[2,4,6,7,8],
    "Attendance":[60,75,85,90,95],
    "PreviousScore":[45,58,67,75,80],
    "AssignmentsCompleted":[2,4,7,8,9],
    "SleepHours":[5,6,7,8,8]
})

prediction = model.predict(new_students)

new_students["Prediction"] = prediction
new_students["Prediction"] = new_students["Prediction"].map(
    {1:"Pass",0:"Fail"}
)

print(new_students)

# ==========================================================
# 5. Manual Accuracy
# ==========================================================

print("\n" + "=" * 60)
print("MANUAL ACCURACY")
print("=" * 60)

correct = (Y_test == Y_pred).sum()

manual_accuracy = correct / len(Y_test)

print("Manual Accuracy :", round(manual_accuracy * 100, 2), "%")
print("Sklearn Accuracy :", round(accuracy * 100, 2), "%")

# ==========================================================
# 6. Misclassified Students
# ==========================================================

print("\n" + "=" * 60)
print("MISCLASSIFIED STUDENTS")
print("=" * 60)

wrong = X_test[Y_test != Y_pred]

print(wrong)

print("\nTotal Misclassified :", len(wrong))

# ==========================================================
# 7. Different Random States
# ==========================================================

print("\n" + "=" * 60)
print("RANDOM STATE COMPARISON")
print("=" * 60)

states = [0, 10, 42]

for state in states:

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=state
    )

    tree = DecisionTreeClassifier(random_state=state)

    tree.fit(X_train, Y_train)

    pred = tree.predict(X_test)

    acc = accuracy_score(Y_test, pred)

    print("Random State =", state,
          "Accuracy =", round(acc * 100, 2), "%")

# ==========================================================
# 8. Decision Tree Visualization
# ==========================================================

print("\n" + "=" * 60)
print("DECISION TREE")
print("=" * 60)

plt.figure(figsize=(15,8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Fail","Pass"],
    filled=True
)

plt.show()

print("Root Node :", X.columns[importance.argmax()])
print("Reason : It provides the highest information gain.")

# ==========================================================
# 9. Performance Index
# ==========================================================

print("\n" + "=" * 60)
print("PERFORMANCE INDEX")
print("=" * 60)

df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]

X_new = df.drop("FinalResult", axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(
    X_new, Y, test_size=0.3, random_state=42
)

tree = DecisionTreeClassifier(random_state=42)

tree.fit(X_train, Y_train)

pred = tree.predict(X_test)

acc_new = accuracy_score(Y_test, pred)

print("Old Accuracy :", round(accuracy * 100, 2), "%")
print("New Accuracy :", round(acc_new * 100, 2), "%")

# ==========================================================
# 10. max_depth=None
# ==========================================================

print("\n" + "=" * 60)
print("MAX DEPTH NONE")
print("=" * 60)

tree = DecisionTreeClassifier(max_depth=None,
                              random_state=42)

tree.fit(X_train, Y_train)

train_pred = tree.predict(X_train)
test_pred = tree.predict(X_test)

train_acc = accuracy_score(Y_train, train_pred)
test_acc = accuracy_score(Y_test, test_pred)

print("Training Accuracy :", round(train_acc * 100, 2), "%")
print("Testing Accuracy :", round(test_acc * 100, 2), "%")

if train_acc == 1 and test_acc < train_acc:
    print("\nExplanation:")
    print("The model has memorized the training data.")
    print("This is called Overfitting.")
    print("It performs perfectly on training data")
    print("but slightly worse on unseen testing data.")
else:
    print("\nModel is performing well.")