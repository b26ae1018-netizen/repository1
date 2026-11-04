import matplotlib.pyplot as plt
print("Enter velocity:")
velocity = float(input())
max_height = (velocity ** 2) / (2 * 9.81)
print("Maximum height reached:", max_height)
time_to_max_height = velocity / 9.81
print("Time to reach maximum height:", time_to_max_height)
total_time = 2 * time_to_max_height
print("Total time of flight:", total_time)
t = [i for i in range(int(total_time) + 1)]
y = [velocity * ti - 0.5 * 9.81 * ti ** 2 for ti in t]
plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("1D Motion of a Projectile")
plt.grid(True)
plt.show()
