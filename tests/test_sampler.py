"""Unit tests for synthetic_data_sampler."""
import unittest
from synthetic_data_sampler.sampler import generate_synthetic_records

class TestSampler(unittest.TestCase):
    def test_generation(self):
        records = generate_synthetic_records(5)
        self.assertEqual(len(records), 5)
        for r in records:
            self.assertIn("@example.com", r["email"])
            self.assertTrue(0 <= r["score"] <= 100)

if __name__ == "__main__":
    unittest.main()
