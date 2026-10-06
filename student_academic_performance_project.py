import pandas as pd
import matplotlib.pyplot as plt

# Read Excel
df = pd.read_excel("C:/Users/Hp/Desktop/student_academic_performance.xlsx")

# Calculate percentage
df["percentage"] = (df["marks"] / df["total"]) * 100

# Calculate grade
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

df["grade"] = df["percentage"].apply(get_grade)

# Pass/Fail
df["result"] = df["percentage"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Basic calculations
average = df["percentage"].mean()
highest = df["percentage"].max()
lowest = df["percentage"].min()
total_subjects = len(df)
passed = (df["result"] == "Pass").sum()
failed = (df["result"] == "Fail").sum()

# Create dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Subject-wise Marks
ax[0, 0].bar(df["sub"], df["marks"])
ax[0, 0].set_title("Subject-wise Marks")
ax[0, 0].set_xlabel("Subjects")
ax[0, 0].set_ylabel("Marks")
ax[0, 0].tick_params(axis="x", rotation=30)

# 2. Academic Performance Trend
ax[0, 1].plot(
    df["sub"],
    df["percentage"],
    marker="o"
)
ax[0, 1].set_title("Academic Performance Trend")
ax[0, 1].set_xlabel("Subjects")
ax[0, 1].set_ylabel("Percentage")
ax[0, 1].set_ylim(0, 100)
ax[0, 1].tick_params(axis="x", rotation=30)

# 3. Grade Distribution
grade_count = df["grade"].value_counts()

ax[1, 0].pie(
    grade_count.values,
    labels=grade_count.index,
    autopct="%1.1f%%"
)
ax[1, 0].set_title("Grade Distribution")

# 4. Academic Summary
ax[1, 1].axis("off")

summary = f"""
ACADEMIC PERFORMANCE SUMMARY

Average Percentage : {average:.2f}%
Highest Percentage : {highest:.2f}%
Lowest Percentage  : {lowest:.2f}%

Total Subjects : {total_subjects}
Subjects Passed : {passed}
Subjects Failed : {failed}
"""

ax[1, 1].text(
    0.05,
    0.5,
    summary,
    fontsize=13,
    verticalalignment="center"
)

# Dashboard title
plt.suptitle(
    "Student Academic Performance Analysis Dashboard",
    fontsize=18
)

plt.tight_layout()

plt.show()
