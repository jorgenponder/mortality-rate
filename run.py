import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import mplcursors

def mortality_rate(odds_factor, x, B, C, A=0):
    return odds_factor * (A + B * np.exp(C * x))

def probability_of_dying(odds_factor, x, B, C, A=0):
    mu_x = mortality_rate(odds_factor, x, B, C, A)
    return 1 - np.exp(-mu_x)

def survival_function(odds_factor, x, B, C, A=0):
    result, _ = quad(lambda t: mortality_rate(odds_factor, t, B, C, A), 0, x)
    return np.exp(-result)

def life_expectancy(odds_factor, B, C, A=0, max_age=120):
    result, _ = quad(lambda x: survival_function(odds_factor, x, B, C, A), 0, max_age)
    return result

ages = np.arange(0, 121, 1)
color_list = ['blue', 'green', 'red', 'purple', 'brown', 'black']

def colors(ordinal):
    """inexhaustible color picker"""
    return color_list[ordinal % (len(color_list))]

initial_mortality_rate = 0.00001
mortality_increase_with_age = 0.13
constant_mortality_factors = 0.0002
scaling_factor = 0.15
mortality_odds_factors = [1, 1.5, 2, 3, 4, 5]

plt.figure(figsize=(10, 8))

# Calculate survival percentages
for color_index, covid_penalty in enumerate(mortality_odds_factors):
    survival_percentages = [survival_function(covid_penalty * scaling_factor, age, initial_mortality_rate, mortality_increase_with_age, constant_mortality_factors) * 100 for age in ages]
    le_postcovid = life_expectancy(covid_penalty * scaling_factor, initial_mortality_rate, mortality_increase_with_age, constant_mortality_factors)
    
    plt.plot(ages, survival_percentages, label=f'{covid_penalty}x Mortality odds (Life Expectancy = {le_postcovid:.2f} years)', color=colors(color_index))

plt.xlabel('Age')
plt.ylabel('Percentage of Age Group Still Alive')
plt.title("""Percentage of Age Group Still Alive for Different Covid Mortality Amplifying Ratios (odds).
Assuming Covid at Birth. Uses Gompertz-Makeham Law with an additional mortality rate scaling odds_factor of %s.
Multiplies Mortality Rate for Any Given Year by Factor from  %s up to %s.
Assumptions: Initial Mortality Rate: %s, Mortality Increase with Age: %s, Constant Mortality Factors: %s Note: This Model May Not Be Accurate.
""" 
          % (scaling_factor, mortality_odds_factors[1], mortality_odds_factors[-1], initial_mortality_rate, mortality_increase_with_age, constant_mortality_factors))
plt.legend()
plt.grid(True)

# Add interactive cursor
mplcursors.cursor(hover=True)

plt.show()
