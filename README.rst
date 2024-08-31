sleep-scoring
#################

**!! Under construction !!**

This is a standalone version of Sleep from the Visbrain suite.

A copy of the relevant documentation is provided [in this repo](https://github.com/x64-bit/sleep-scoring/blob/main/docs/sleep.rst), but can also be found at the [original Visbrain repo](https://github.com/EtienneCmb/visbrain/blob/master/docs/sleep.rst).

Example code can be found under [examples/gui_sleep](https://github.com/x64-bit/sleep-scoring/tree/main/examples/gui_sleep)

Installation
=================

It is recommended to install this in a virtual environment using conda. This package was developed on Python 3.12 but has been shown to work with Python >= 3.9.::

    python -m pip install sleep-scoring 

It is recommended to preface `pip` with `python -m` to ensure it uses the virtual environment's installation of python*

Deployment
=================

Sleep can be deployed using this python script (see `examples/basic_sleep.py`)::

    from sleep_scoring.gui import Sleep

    Sleep().show()


You can either start Python in the terminal with the `python` command and write the commands there, or you can create a python script and run it.

Credits
=========
Original authors:
Etienne Combrisson, Raphael Vallat, and Christian O Reilly.

Combrisson E, Vallat R, Eichenlaub J-B, O'Reilly C, Lajnef T, Guillot A, Ruby PM and Jerbi K (2017) Sleep: An Open-Source Python Software for Visualization, Analysis, and Staging of Sleep Data. Front. Neuroinform. 11:60. doi: 10.3389/fninf.2017.00060
