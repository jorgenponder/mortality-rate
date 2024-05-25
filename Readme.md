# Survival rate visualizer

![diagram](https://github.com/jorgenponder/mortality-rate/assets/67808946/942bc184-b803-4c41-89a2-d7f209e7ff93)


## Disclaimer

I'm not really sure if this is doing what it is supposed to do.

## Usage

Use python, pip install what is in dependencies.txt. Run the run.py file with python, and a window with a diagram should pop up

## Question and behavior

If the odds of dying every year increased with a constant factor, would people notice?
Code has a model with different odds and their effect on life expectancy.

Computes and displays percentage of age group still alive for different covid mortality amplifying ratios (odds).
Assuming covid at birth. Uses the Gompertz-Makeham law with an additional mortality rate scaling odds_factor of 0.15.
Multiplies mortality rate for any given year by factor from  1.5 up to 5.

## Inspiration

Tried to make its make curves similar to the charts of Swedish women's life expectancy 1950-2010 from this paper:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3394084/

Diagram from that paper:

![from_paper](https://github.com/jorgenponder/mortality-rate/assets/67808946/da9de47f-9451-4745-9a1f-20f88d6de8ab)
