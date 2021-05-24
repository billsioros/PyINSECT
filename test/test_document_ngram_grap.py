import unittest

from pyinsect.documentModel.comparators import SimilarityNVS, Union
from pyinsect.documentModel.representations import DocumentNGramGraph


class DocumentNGramGraphTestCase(unittest.TestCase):
    def setUp(self):
        self.ngg1 = DocumentNGramGraph(3, 2, "abcdef")
        self.ngg2 = DocumentNGramGraph(3, 2, "abcdeff")

        self.gs = SimilarityNVS()

        self.bop = Union(lf=0.5, commutative=True, distributional=True)

    def test_similarity(self):
        sc = self.gs.getSimilarityComponents(self.ngg1, self.ngg2)

        self.assertAlmostEqual(sc["SS"], 0.80, 2)
        self.assertAlmostEqual(sc["VS"], 0.67, 2)

        self.assertAlmostEqual(self.gs.getSimilarityFromComponents(sc), 0.83, 2)

        self.assertAlmostEqual(self.gs.apply(self.ngg1, self.ngg2), 0.83, 2)

    def test_union(self):
        self.bop.apply(self.ngg1, self.ngg2)
