import unittest
import solution
import data1
import data2
import data3

class TestPerson(unittest.TestCase):
    def test_affiliation_1(self):
        self.assertEqual([t.displayname for t in solution.exercise1(data1.alice, data1.people)], ['The A-Team', 'The C-Team'])
    
    def test_affiliation_2(self):
        self.assertEqual([t.displayname for t in solution.exercise1(data1.alice, data1.people)], ['The A-Team', 'The C-Team'])
    
    def test_affiliation_3(self):
        self.assertEqual([t.displayname for t in solution.exercise1(data2.bob, data2.people)], ['The A-Team', 'The C-Team'])