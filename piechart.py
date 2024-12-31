import matplotlib.pyplot as plt
import numpy as np

input = np.array([0, 6, 3, 4, 2])
mylabel = ("A", "B", "C", "D", "E")

plt.pie(input, labels = mylabel)

plt.title("Pie Chart")
plt.grid()
plt.show()

