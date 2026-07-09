import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("student_data.csv")

# Calculate Average
df["Average"] = (df["Maths"] + df["Science"] + df["English"]) / 3

# Assign Grade
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Pass or Fail
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Display Output
print("----- Student Performance Report -----")
print(df)

# Top Performer
topper = df.loc[df["Average"].idxmax()]
print("\nTop Performer:")
print(topper)

# Bar Chart
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.show()