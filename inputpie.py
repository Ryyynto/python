import matplotlib.pyplot as plt
import numpy as np

value = list(map(int, input("Enter value: ").split()))
simbol = list(map(str, input("Enter label: ").split()))

if len(value) == len(simbol):
    input = np.array(value)
    mylabel = np.array(simbol)

    plt.pie(input, labels = mylabel)

    plt.title("Pie Chart")
    plt.grid()
    plt.show()


else:
    print("Error, The number of value and label must be equal")

