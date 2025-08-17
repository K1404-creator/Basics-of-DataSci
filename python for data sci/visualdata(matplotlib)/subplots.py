import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, y1, label='Line 1', color='blue')
ax1.set_title('First Plot')


ax2.plot(x, y2, label='Line 2', color='red')
ax2.set_title('Second Plot')


plt.show()