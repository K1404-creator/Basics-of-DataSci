import matplotlib.pyplot as plt

hours_studies = [1, 2, 3, 4, 5, 6, 7]
scores = [50, 55, 60, 65, 70, 75, 80]

plt.scatter(hours_studies,  scores, color = 'pink')
plt.title('Study Hours vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.show()
