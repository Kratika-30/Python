import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aman", "Riya", "Rahul", "Sneha", "Karan"],
    "Math": [85, 78, 92, 70, 60],
    "Science": [88, 74, 90, 65, 70],
    "English": [75, 80, 85, 60, 65],
    "History": [70, 68, 80, 72, 75],
    "Computer": [90, 85, 95, 78, 80]
}

df = pd.DataFrame(data)

df["Total"] = df.iloc[:, 1:6].sum(axis=1)
df["Average"] = df["Total"] / 5

print("Student Data:\n")
print(df)

print("\nMean Marks:\n")
print(df.iloc[:, 1:6].mean())

print("\nMedian Marks:\n")
print(df.iloc[:, 1:6].median())

print("\nStandard Deviation:\n")
print(df.iloc[:, 1:6].std())

print("\nHigh Performers (Average > 80):")
print(df[df["Average"] > 80][["Student", "Average"]])

print("\nLow Performers (Average < 65):")
print(df[df["Average"] < 65][["Student", "Average"]])

df.iloc[:, 1:6].mean().plot(kind='bar', color='lightblue')
plt.title("Average Marks in Each Subject")
plt.ylabel("Marks")
plt.show()

plt.plot(df["Student"], df["Average"], marker='o')
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

plt.hist(df["Total"], bins=5, color='green')
plt.title("Distribution of Total Marks")
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.show()

df.iloc[:, 1:6].mean().plot(kind='pie', autopct='%1.1f%%')
plt.title("Subject Contribution")
plt.ylabel("")
plt.show()