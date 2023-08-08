import matplotlib.pyplot as plt

values = [100000, 124999, 156248, 195310.1, 244137.5]
time = [1, 2, 3, 4, 5] 

# Plotting the graph
plt.plot(time, values, marker='o', linestyle='-', color='b')
plt.xlabel('Time (t)')
plt.ylabel('Money ($)')
plt.title('Money ($) vs. Time (t)')

for i in range(len(values)):
    plt.annotate(f"${values[i]:,.2f}", (time[i], values[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.grid(True)
plt.show()
