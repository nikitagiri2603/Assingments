# =====================================================
# Student Performance Prediction using Decision Tree
# =====================================================

# Import required libraries

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# =====================================================
# 1. Load Dataset
# =====================================================

df = pd.read_csv("student_performance_ml.csv")

print("="*60)
print("FIRST 5 RECORDS")
print("="*60)
print(df.head())

print("\nLAST 5 RECORDS")
print(df.tail())

print("\nDataset Shape :", df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# =====================================================
# 2. Data Analysis
# =====================================================

print("\n","="*60)
print("DATA ANALYSIS")
print("="*60)

print("Total Students :", len(df))

passed = (df["FinalResult"]==1).sum()
failed = (df["FinalResult"]==0).sum()

print("Passed :",passed)
print("Failed :",failed)

print("\nAverage Study Hours :",df["StudyHours"].mean())
print("Average Attendance :",df["Attendance"].mean())
print("Maximum Previous Score :",df["PreviousScore"].max())
print("Minimum Sleep Hours :",df["SleepHours"].min())

print("\nFinal Result Distribution")
print(df["FinalResult"].value_counts())

pass_percentage = passed/len(df)*100
fail_percentage = failed/len(df)*100

print("\nPass Percentage : {:.2f}%".format(pass_percentage))
print("Fail Percentage : {:.2f}%".format(fail_percentage))

# =====================================================
# 3. Visualization
# =====================================================

# Histogram

plt.figure(figsize=(6,4))
plt.hist(df["StudyHours"],bins=6,edgecolor="black")
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Students")
plt.show()

# Scatter Plot

colors=df["FinalResult"].map({1:"green",0:"red"})

plt.figure(figsize=(6,4))
plt.scatter(df["StudyHours"],
            df["PreviousScore"],
            c=colors)

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()

# Box Plot

plt.figure(figsize=(5,5))
plt.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.ylabel("Attendance")
plt.show()

# Assignments vs Final Result

plt.figure(figsize=(6,4))
plt.scatter(df["AssignmentsCompleted"],
            df["FinalResult"])

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.show()

# Sleep Hours vs Final Result

plt.figure(figsize=(6,4))
plt.scatter(df["SleepHours"],
            df["FinalResult"])

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.show()

# =====================================================
# 4. Prepare Data
# =====================================================

X = df.drop("FinalResult",axis=1)

Y = df["FinalResult"]

# =====================================================
# 5. Train Test Split
# =====================================================

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

# =====================================================
# 6. Train Decision Tree Model
# =====================================================

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train,Y_train)

# =====================================================
# 7. Prediction
# =====================================================

Y_pred = model.predict(X_test)

print("\n","="*60)
print("ACTUAL VS PREDICTED")
print("="*60)

for actual,predicted in zip(Y_test,Y_pred):
    print("Actual :",actual," Predicted :",predicted)

# =====================================================
# 8. Accuracy
# =====================================================

accuracy = accuracy_score(Y_test,Y_pred)

print("\nTesting Accuracy = {:.2f}%".format(accuracy*100))

# =====================================================
# 9. Confusion Matrix
# =====================================================

cm = confusion_matrix(Y_test,Y_pred)

print("\nConfusion Matrix")
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)

disp.plot()

plt.show()

print("\nMeaning of Confusion Matrix")

print("True Positive  : Student Passed and model predicted Pass.")
print("True Negative  : Student Failed and model predicted Fail.")
print("False Positive : Student Failed but model predicted Pass.")
print("False Negative : Student Passed but model predicted Fail.")

# =====================================================
# 10. Training and Testing Accuracy
# =====================================================

train_pred = model.predict(X_train)

train_accuracy = accuracy_score(Y_train,train_pred)

test_accuracy = accuracy_score(Y_test,Y_pred)

print("\nTraining Accuracy : {:.2f}%".format(train_accuracy*100))
print("Testing Accuracy  : {:.2f}%".format(test_accuracy*100))

if train_accuracy > test_accuracy + 0.10:
    print("\nModel is Overfitting")
elif train_accuracy < test_accuracy:
    print("\nModel is Underfitting")
else:
    print("\nModel is Well Fitted")

# =====================================================
# 11. Compare Different max_depth Values
# =====================================================

print("\n","="*60)
print("MAX DEPTH COMPARISON")
print("="*60)

depths=[1,3,None]

for depth in depths:

    tree=DecisionTreeClassifier(max_depth=depth,
                                random_state=42)

    tree.fit(X_train,Y_train)

    pred=tree.predict(X_test)

    acc=accuracy_score(Y_test,pred)

    print("max_depth =",depth," Accuracy = {:.2f}%".format(acc*100))

# =====================================================
# 12. Predict New Student
# =====================================================

student = [[6,85,66,7,7]]

prediction = model.predict(student)

print("\n","="*60)
print("NEW STUDENT PREDICTION")
print("="*60)

if prediction[0]==1:
    print("Student will PASS")
else:
    print("Student will FAIL")

# =====================================================
# 13. Final Conclusion
# =====================================================

print("\n","="*60)
print("FINAL CONCLUSION")
print("="*60)

print("1. Dataset loaded successfully.")
print("2. Data analysis completed.")
print("3. Graphs plotted successfully.")
print("4. Decision Tree model trained.")
print("5. Predictions generated.")
print("6. Accuracy calculated.")
print("7. Confusion Matrix displayed.")
print("8. Model evaluated using train and test accuracy.")
print("9. Different max_depth values compared.")
print("10. New student's result predicted successfully.")