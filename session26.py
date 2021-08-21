import matplotlib.pyplot as plt
#data = [0, 1, 2, 3, 4, 5]
#plt.plot(data)
#plt.show()

X = list(range(1, 11))
y1 = [n for n in X]
y2 = [n*n for n in X]
y3 =[n*n*n for n in X]

plt.plot(X, y1, label = "y1")
plt.plot(X, y2, label = "y2")
plt.plot(X, y3, label = "y3")
plt.legend()
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Polynomial graphs")
plt.savefig("Polynomial graphs")

plt.show()