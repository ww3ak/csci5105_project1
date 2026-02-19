import unittest
from server.server import InMemoryKV
from types import SimpleNamespace


class gRPCTestSetup(unittest.TestCase):
    def setup(self):
        self.service = InMemoryKV()
        # Clear dictionaries to undo load from disk--start fresh
        self.service.textbook_chunks = {}
        self.service.embeddings = {}

class TestPut(gRPCTestSetup):
    def test_put_existing_key(self):        
        pass

    def test_put_new_key(self):
        pass


class TestGetText(gRPCTestSetup):

    def test_existing_key(self):
        self.service.textbook_chunks["test_key"] = "test_value"

        #fake request key
        request = SimpleNamespace(key="test_key")
        #get GetText response 
        response = self.service.GetText(request)
        # response should be true and return test_value
        self.assertTrue(response.found)
        self.assertEqual(response.textbook_chunk, "test_value")

    def test_missing_key(self):
        #fake request key
        request = SimpleNamespace(key="missing_key")

        #get GetText response 
        response = self.service.GetText(request)

        # respose should be false and return empty string
        self.assertFalse(response.found)
        self.assertEqual(response.textbook_chunk, "")


class TestDelete(gRPCTestSetup):
    def test_delete_existing_key(self):
        pass

    def test_delete_missing_key(self):
        pass


class TestList(gRPCTestSetup):
    #add some, list. then delete some, list
    pass


class TestHealth(gRPCTestSetup):
    pass


if __name__ == "__main__":
    unittest.main()
