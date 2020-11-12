import matplotlib.pyplot as plt
import csv

years = [1950, 1970, 1990, 2010]

population = [2.519, 3.692, 5.263, 6.972]

deaths = [0.519, 1.692, 10.263, 2.972]

# The graphic's title
plt.title("Población Anual")

plt.xlabel("Año")
plt.ylabel("Población")

# Plot (with scattering) of the rise of population(y) over the years (x)
plt.plot(years, population, 'r')
plt.scatter(years, population, color = 'r')

# Plot (with scattering) of the rise of deaths(y) over the years (x)
plt.plot(years, deaths, 'g')
plt.scatter(years, deaths, color = 'g')

# Function to add legends to each of the plots
plt.legend(['Crecimiento', 'Muertes'])

# Functon to show the graphic
plt.show()