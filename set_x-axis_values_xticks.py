import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 7]
y = [2, 1, 6, 4, 8, 5]

values = ['A', 'B', 'C', 'D', 'E', 'F']

plt.plot(x, y, marker="o")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Set X labels in Matplotlib Plot")
plt.xticks(x, values)
plt.show()