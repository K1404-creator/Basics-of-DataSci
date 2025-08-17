import matplotlib.pyplot as plt

categories = ['electronics', 'furniture', 'clothing', 'toys', 'books']

sales = [1500, 1200, 800, 600, 400]

plt.bar(categories, sales, color='skyblue',edgecolor = 'orange', width = 0.6)

plt.title('Sales by Category', fontsize=14, color='navy')

plt.xlabel('Categories', fontsize=12, color='darkblue')
plt.ylabel('Sales in USD', fontsize=12, color='darkblue')

plt.grid(True, axis = 'y', linestyle='--', alpha=0.7)
plt.show()