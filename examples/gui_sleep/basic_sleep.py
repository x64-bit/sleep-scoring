"""
Basic configuration
===================

This example demonstrate how to open Sleep.

Two windows will then appear :

* The first one ask a proper dataset (required)
* The second one ask for an hypnogram (optional). If None, an empty one is used

.. image:: ../../picture/picsleep/ex_basic_sleep.png
"""
import sys
sys.path.append('/Users/anjopagdanganan/visbrain-testing/port-visbrain-0.4.3')

from visbrain_sleep_port.gui import Sleep

Sleep().show()
