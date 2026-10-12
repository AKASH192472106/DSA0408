import numpy as np

student_scores = np.array([
    [80, 75, 85, 70],
    [90, 85, 80, 75],
    [70, 80, 90, 85],
    [85, 90, 75, 80]
])

avg = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]

print("Average marks:", avg)

for i in range(4):
    print(subjects[i], ":", avg[i])

print("Highest average subject:", subjects[np.argmax(avg)])
