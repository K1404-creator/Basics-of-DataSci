import matplotlib.pyplot as plt

#line plot

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

sales = [200, 400, 600, 800, 1000, 1200, 1400]


plt.plot(years,sales,marker='o',linestyle='-',color = 'blue')
plt.title('Annual sales over the years')
plt.xlabel('Year')
plt.ylabel('Sales in millions')
plt.show()