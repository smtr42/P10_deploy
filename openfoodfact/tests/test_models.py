from django.test import TestCase


class CategoryModeltest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_false_is_false(self):
        self.assertFalse(False)

    def test_false_is_true(self):
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 2)
