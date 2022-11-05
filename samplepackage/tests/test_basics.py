import unittest

from samplepackage.sub_package import hello_world


class TestBasics(unittest.TestCase):

    def test_helloworld(self):
        self.assertEqual(hello_world.say_hi(), 'hi')
