import unittest
from src.aganitha_papers.papers import filter_non_academic_authors

class TestFilterNonAcademicAuthors(unittest.TestCase):

    def test_only_academic(self):
        papers = [
            {"Affiliations": "Harvard University, MIT"},
            {"Affiliations": "Stanford University, Department of Biology"}
        ]
        result = filter_non_academic_authors(papers)
        self.assertEqual(len(result), 2)

    def test_only_non_academic(self):
        papers = [
            {"Affiliations": "Pfizer Inc, Johnson & Johnson"},
            {"Affiliations": "Google LLC, Microsoft Research"}
        ]
        result = filter_non_academic_authors(papers)
        self.assertEqual(len(result), 0)

    def test_mixed_affiliations(self):
        # Updated mixed affiliations test data
        papers = [
            {"Affiliations": "Harvard University, Pfizer Inc"},    # Mixed → should be included
            {"Affiliations": "Stanford University, Google LLC"},   # Mixed → should be included
            {"Affiliations": "Pfizer Inc, Google LLC"}             # Non-academic → should be excluded
        ]
        result = filter_non_academic_authors(papers)
        self.assertEqual(len(result), 2)  # ✅ Expecting 2 mixed papers included

    def test_no_affiliations(self):
        papers = [
            {"Affiliations": ""},
            {"Affiliations": None}
        ]
        result = filter_non_academic_authors(papers)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
