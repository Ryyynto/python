import matplotlib.pyplot as plt
import numpy as np

xinput = list(map(int, input("Enter x points: ").split()))
yinput = list(map(int, input("Enter y points: ").split()))

if len(xinput) == len(yinput):
    plt.plot(xinput, yinput)
    plt.show()

else:
    print("Error, The number of x points and y points must be equal")