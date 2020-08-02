from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Evans, Jack'
        expected = 'Jack Evans'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase ='SquarePants, SpongeBob S.'
        expected = 'SpongeBob S. SquarePants'
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase = 'Plankton'
        expected = 'Plankton'
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()