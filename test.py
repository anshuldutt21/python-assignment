import unittest
from question1 import Person 
class TestStringMethods(unittest.TestCase):
 def test_1(self):
  t1=Person("ads","singing","delhi")
  self.assertEqual(t1.name,"ads")
  self.assertEqual(t1.city,"delhi")
  self.assertEqual(t1.work,["singing"])
 def test_2(self):
  t2=Person("ads")
  self.assertEqual(t2.name,"ads")
  self.assertEqual(t2.city,"Roorkee")
 def test_3(self):
  t3=Person("shaddygarg")
  self.assertEqual(t3.name,"shaddygarg")
  self.assertEqual(t3.work,[None])
 def test_4(self):
  t4=Person("shaddygarg","dance","Delhi")
  self.assertEqual(t4.name,"shaddygarg")
  self.assertEqual(t4.work,["dance"])
 def test_5(self):
  t5=Person("shaddygarg","dance",)
  self.assertEqual(t5.name,"shaddygarg")
  self.assertEqual(t5.work,["dance"])
  self.assertEqual(t5.city,"Roorkee")
if __name__ == '__main__':
    unittest.main()