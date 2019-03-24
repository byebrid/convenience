import unittest
import convenience


class TestConvenience(unittest.TestCase):
    def setUp(self):
        self.test_d = {
            "Hello": {
                "There": {
                    "Youngling": 22
                },
                "Stop": None
            },
            None: True
        }

        self.test_d_simple = {
            "Hello": {
                None
            }
        }


    def test_get_from_dict(self):
        # Return int
        result = convenience.get_from_dict(keys=["Hello", "There", "Youngling"], dict=self.test_d)
        self.assertEqual(result, 22)

        # Return sub-dict
        result = convenience.get_from_dict(keys=["Hello", "There"], dict=self.test_d)
        self.assertEqual(result, {"Youngling": 22})

        # Encounters a key that is just None
        result = convenience.get_from_dict(keys=[None], dict=self.test_d)
        self.assertEqual(result, True)
        
        with self.assertRaises(KeyError):
            convenience.get_from_dict(keys=["Invalid key!"], dict=self.test_d)


    def test_set_in_dict(self):
        # No dict provided - returns new dict
        result = convenience.set_in_dict(keys=["Hello", "Stop"], value=44)
        self.assertEqual(result, {"Hello": {"Stop": 44}})

        # One missing key; where "Stop" should be, we get None
        result = convenience.set_in_dict(keys=["Hello", "Stop"],
            value=55, dict=self.test_d_simple)
        self.assertEqual(result, {"Hello": {"Stop": 55}})


if __name__ == '__main__':
    unittest.main()
