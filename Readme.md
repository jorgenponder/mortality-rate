# Mortality rate visualizer

![A diagram](diagram.jpg)

## Disclaimer

I'm not really sure if this is doing what it is supposed to do.

## Usage

Use python, pip install what is in dependencies.txt. Run the run.py file with python, and a window with a diagram should pop up

## Question and behavior

If the odds of dying every year increased with a constant factor, would people notice?
Code has a model with different odds and their effect on life expectancy. If ppl would choose not to trust or care about future stats, chances are they will not notice?

Computes and displays percentage of age group still alive for different covid mortality amplifying ratios (odds).
Assuming covid at birth. Uses gompertz-makeham law with an additional mortality rate scaling odds_factor of 0.15.
Multiplies mortality rate for any given year by factor from  1.5 up to 5.

## Inspiration

Tried it make curves similar to the charts of Swedish women's life expectancy 1950-210 from this paper:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3394084/

Diagram from that paper:

![A diagram from paper PMC3394084](from_paper.jpg)
