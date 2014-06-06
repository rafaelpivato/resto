import unittest
import resto

from pkg_resources import parse_version


class VersionTestCase(unittest.TestCase):
    """Checks package `__version__` access."""

    def test_version_access(self):
        """Resto package version access."""
        this = parse_version(resto.__version__)
        dev = parse_version('dev')
        self.assertTrue(this >= dev)
