import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

sales = [200, 300, 400, 500, 600, 700]

plt.plot(months, sales, color = 'red', linestyle='--', marker='o',linewidth=2, markersize=8)


plt.title('Monthly Sales Data', fontsize = 13, color = 'darkred')

plt.xlabel('Months')
plt.ylabel('Sales in USD')

plt.show()
