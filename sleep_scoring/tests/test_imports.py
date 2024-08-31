"""Test modules importation."""


def test_import_matplotlib():
    """Import matplotlib."""
    import matplotlib  # noqa


def test_import_numpy():
    """Import NumPy."""
    import numpy  # noqa


def test_import_scipy():
    """Import scipy."""
    import scipy  # noqa


def test_import_pyqt():
    """Import PyQt."""
    import PyQt5  # noqa


def test_import_brain():
    """Import the Brain module.."""
    from sleep_scoring.gui import Brain  # noqa


def test_import_sleep():
    """Import the Sleep module.."""
    from sleep_scoring.gui import Sleep  # noqa


def test_import_signal():
    """Import the Signal module.."""
    from sleep_scoring.gui import Signal  # noqa


def test_import_figure():
    """Import the Figure module.."""
    from sleep_scoring.gui import Figure  # noqa
