import unittest
import solution
import data1
import data2
import data3


class TestPerson(unittest.TestCase):
    def test_affiliated_teams1(self):
        self.assertEqual([t.displayname for t in solution.exercise1(data1.alice, data1.people)], ['The A-Team', 'The C-Team'])
    
    def test_affiliated_teams2(self):
        self.assertEqual([t.displayname for t in solution.exercise1(data2.alice, data2.people)], ['The A-Team', 'The C-Team'])
    
    def test_affiliated_teams3(self):
        self.assertEqual([t.displayname for t in solution.exercise1(data2.bob, data2.people)], ['The A-Team','The B-Team', 'The C-Team'])

    def test_affiliated_members1(self):
        self.assertEqual(sorted(p.displayname for p in solution.get_members(data2.c_team)), ['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve'])
    
    def test_affiliated_members2(self):
        self.assertEqual(sorted(p.displayname for p in solution.get_members(data3.c_team)), ['Alice', 'Bob', 'Carlos', 'Charlie', 'Eve', 'Peggy', 'Trent', 'Victor'])


if __name__ == '__main__':
    unittest.main()
