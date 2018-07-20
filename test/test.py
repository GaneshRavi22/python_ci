import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import unittest
import xmlrunner
import main

class Case2Test(unittest.TestCase):

    def setUp(self):
        self.seq = main.Main()

    def test_buzz(self):
        self.assertTrue(' '.join([self.seq.getString().split()[0], self.seq.getString().split()[1]]) in main.buzz)

    def test_adjectives(self):
        self.assertTrue(self.seq.getString().split()[2] in main.adjectives)

    def test_adverbs(self):
        self.assertTrue(self.seq.getString().split()[3] in main.adverbs)

    def test_verbs(self):
        self.assertTrue(self.seq.getString().split()[4] in main.verbs)

if __name__ == '__main__':
    with open('test_results1.xml', 'w') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
