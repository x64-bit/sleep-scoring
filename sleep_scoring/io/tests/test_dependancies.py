"""Test functions in dependancies.py."""
from sleep_scoring.io.dependencies import (is_mne_installed, is_nibabel_installed,
                                      is_opengl_installed, is_pandas_installed,
                                      is_lspopt_installed,
                                      is_tensorpac_installed)


class TestDependencies(object):
    """Test installed dependancies."""

    def test_dependencies(self):
        """Test function dependencies."""
        for k in (is_mne_installed, is_nibabel_installed, is_opengl_installed,
                  is_pandas_installed, is_lspopt_installed,
                  is_tensorpac_installed):
            assert isinstance(k(), bool)
