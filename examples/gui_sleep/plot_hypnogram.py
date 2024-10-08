"""
Matplotlib plot of an hypnogram
===============================

Plot a hypnogram using matplotlib.
"""
from sleep_scoring.io import write_fig_hyp, read_hypno, download_file

###############################################################################
# Plotting properties
###############################################################################
# Define plotting properties

grid = True     # display the grid
ascolor = True  # plt as color or in black and white
file = None     # Name of the file to be saved example : 'myfile.png'

###############################################################################
# Hypnogram data
###############################################################################
# For the illustration, a hypnogram is downloaded

path_to_hypno = download_file("s101_jbe.hyp", astype='example_data')
data, sf = read_hypno(path_to_hypno)

###############################################################################
# Plot the hypnogram
###############################################################################
# Plot the hypnogram. If file is None, the window is displayed otherwise the
# figure is saved

write_fig_hyp(data, sf, grid=grid, ascolor=ascolor, file=file)
