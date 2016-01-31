# plot-helpers-thesis

`poly_fit.py` takes some power measurements and produces a second degree
least squares fit curve, according to the expected power measurements.
It accepts input (currently a value between 2.6-42W, the lowest and
highest power measured), and also produces a static plot.

`power_estimate.py` was used to determine which dimmer value gives
which power consumption.

`dimmer_auto.py` is an interactive graph that uses matplotlib, and
helps understand how a modern dimmer works.
