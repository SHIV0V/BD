import matplotlib.pyplot as plt

subjects = ['Python','Java','C','PHP']
marks = [80,70,90,60]

plt.bar(subjects,marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Bar Plot")
plt.show()
