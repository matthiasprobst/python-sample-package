import unittest

from sampleproject import __version__


class TestBasics(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, '0.1.0')
