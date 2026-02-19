import unittest
import kvstore_pb2
from server.server import InMemoryKV
from types import SimpleNamespace


class gRPCTestSetup(unittest.TestCase):
    def setup(self):
        self.service = InMemoryKV()
        # Clear dictionaries to undo load from disk--start fresh
        self.service.textbook_chunks = {}
        self.service.embeddings = {}

class TestPut(gRPCTestSetup):
    def test_put_overwrite(self):        
        # Put in a textbook chunk and embedding for test_key
        request = kvstore_pb2.PutRequest(key="test_key", 
                                         textbook_chunk="original_value", 
                                         embedding=bytes([1, 1, 1, 1]))
        response = self.service.Put(request, 0)    # Context parameter not used, set to 0
        self.assertFalse(response.overwritten)
        self.assertEqual(self.service.textbook_chunks["test_key"], "original_value")
        self.assertEqual(self.service.embedding["test_key"], bytes([1, 1, 1, 1]))

        # Overwrite textbook chunk and embedding for test_key
        request = kvstore_pb2.PutRequest(key="test_key", 
                                         textbook_chunk="new_value", 
                                         embedding=bytes([2, 2, 2, 2]))
        response = self.service.Put(request, 0)    # Context parameter not used--set to 0

        self.assertTrue(response.overwritten)
        self.assertEqual(self.service.textbook_chunks["test_key"], "new_value")
        self.assertEqual(self.service.embedding["test_key"], bytes([2, 2, 2, 2]))


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
    def test_list(self):
            list_request = kvstore_pb2.ListRequest()
            
            # Test List() on an empty key-value store
            response = self.service.List(list_request)
            self.assertEqual(len(response.keys), 0)

            # Test List() after adding 3 entries
            put_request1 = kvstore_pb2.PutRequest(key="key1", 
                                         textbook_chunk="val1", 
                                         embedding=bytes([1, 1, 1, 1]))
            put_request2 = kvstore_pb2.PutRequest(key="key2", 
                                         textbook_chunk="val2", 
                                         embedding=bytes([2, 2, 2, 2]))
            put_request3 = kvstore_pb2.PutRequest(key="key3", 
                                         textbook_chunk="val3", 
                                         embedding=bytes([3, 3, 3, 3]))
            self.service.Put(put_request1, 0)
            self.service.Put(put_request2, 0)
            self.service.Put(put_request3, 0)
            response = self.service.List(list_request)
            self.assertEqual(len(response.keys), 3)
            self.assertEqual(set(response.keys), set(["key1", "key2", "key3"]))

            # Test List() after removing one of the entries
            del_request = kvstore_pb2.DeleteRequest(key="key2")
            response = self.service.Delete(del_request)
            self.assertTrue(response.deleted)
            response = self.service.List(list_request)
            self.assertEqual(len(response.keys), 2)
            self.assertEqual(set(response.keys), set(["key1", "key3"]))


class TestHealth(gRPCTestSetup):
    pass


if __name__ == "__main__":
    unittest.main()
