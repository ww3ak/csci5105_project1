import unittest

#one thing i am unsure of is do we need to spin up  channel and stub
#for each test? or can we just fake it by doing something like this: 
        # self.service.textbook_chunks = {
        #     "k1": "hello world"
        # }

class TestGetText(unittest.TestCase):
    def test_existing_key(self):
        # should return key value
        pass

    def test_missing_key(self):
        # should return not found
        pass


class TestDeleteKey(unittest.TestCase):
    def test_delete_existing_key(self):
        pass

    def test_delete_missing_key(self):
        pass


class TestListKey(unittest.TestCase):
    pass


class TestHealth(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
