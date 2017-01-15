import unittest


def test(x):
	return x**3

class Classtest(unittest.TestCase):
	def test1(self):
		self.assertEqual(test(4),64)

if __name__ == '__main__':
	unittest.main()





