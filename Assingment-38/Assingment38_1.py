import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("student_performance_ml.csv")

print("=" * 50)
print("1. DATASET INFORMATION")
print("=" * 50)

print("\nFirst 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Total Students, Pass, Fail
# -----------------------------
print("\n" + "=" * 50)
print("2. STUDENT COUNT")
print("=" * 50)

total = len(df)
passed = (df["FinalResult"] == 1).sum()
failed = (df["FinalResult"] == 0).sum()

print("Total Students :", total)
print("Passed Students :", passed)
print("Failed Students :", failed)

# -----------------------------
# Statistics
# -----------------------------
print("\n" + "=" * 50)
print("3. DATA ANALYSIS")
print("=" * 50)

print("Average Study Hours :", df["StudyHours"].mean())
print("Average Attendance :", df["Attendance"].mean())
print("Maximum Previous Score :", df["PreviousScore"].max())
print("Minimum Sleep Hours :", df["SleepHours"].min())

# -----------------------------
# Value Counts
# -----------------------------
print("\n" + "=" * 50)
print("4. FINAL RESULT DISTRIBUTION")
print("=" * 50)

result = df["FinalResult"].value_counts()

print(result)

pass_percentage = (passed / total) * 100
fail_percentage = (failed / total) * 100

print("\nPass Percentage : {:.2f}%".format(pass_percentage))
print("Fail Percentage : {:.2f}%".format(fail_percentage))

if abs(pass_percentage - fail_percentage) <= 20:
    print("\nDataset is Reasonably Balanced.")
else:
    print("\nDataset is Imbalanced.")

# -----------------------------
# Study Hours Analysis
# -----------------------------
print("\n" + "=" * 50)
print("5. OBSERVATION")
print("=" * 50)

avg_pass = df[df["FinalResult"] == 1]["StudyHours"].mean()
avg_fail = df[df["FinalResult"] == 0]["StudyHours"].mean()

print("Average Study Hours (Pass):", round(avg_pass, 2))
print("Average Study Hours (Fail):", round(avg_fail, 2))

att_pass = df[df["FinalResult"] == 1]["Attendance"].mean()
att_fail = df[df["FinalResult"] == 0]["Attendance"].mean()

print("Average Attendance (Pass):", round(att_pass, 2))
print("Average Attendance (Fail):", round(att_fail, 2))

print("\nObservation:")
print("- Students studying more hours are more likely to pass.")
print("- Higher attendance improves academic performance.")
print("- Students with low attendance mostly fail.")
print("- Study hours and attendance positively affect FinalResult.")

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(6,4))
plt.hist(df["StudyHours"], bins=6, edgecolor="black")
plt.title("Histogram of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
colors = df["FinalResult"].map({1: "green", 0: "red"})

plt.figure(figsize=(6,4))
plt.scatter(df["StudyHours"],
            df["PreviousScore"],
            c=colors)

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()

# -----------------------------
# Box Plot
# -----------------------------
plt.figure(figsize=(5,5))
plt.boxplot(df["Attendance"])
plt.title("Attendance Box Plot")
plt.ylabel("Attendance")
plt.show()

# -----------------------------
# Assignments vs Final Result
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["AssignmentsCompleted"],
            df["FinalResult"],
            color="blue")

plt.title("Assignments Completed vs Final Result")
plt.xlabel("Assignments Completed")
plt.ylabel("Final Result")
plt.show()

# -----------------------------
# Sleep Hours vs Final Result
# -----------------------------
plt.figure(figsize=(6,4))
plt.scatter(df["SleepHours"],
            df["FinalResult"],
            color="purple")

plt.title("Sleep Hours vs Final Result")
plt.xlabel("Sleep Hours")
plt.ylabel("Final Result")
plt.show()

print("\n" + "=" * 50)
print("10. FINAL OBSERVATION")
print("=" * 50)

print("Sleeping 7-8 hours helps maintain good health and concentration.")
print("However, sleep alone does not guarantee success.")
print("Study hours, attendance, previous score, and assignment completion")
print("also significantly influence the final result.")