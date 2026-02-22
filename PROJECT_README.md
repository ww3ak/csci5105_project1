# Project 1 CSCI 5105

**Distributed gRPC Key-Value Store with Textbook Chunks and Embeddings**

---
## Authors

- Sabrina Simkhovich (simkh005@umn.edu)
- 


## Project Structure
```text
├── PROJECT_README.md - Design document with HOW TO RUN instructions
├── README.md - Given project description and student instructions
├── example_questions.txt
├── gRPC_KVS
│   ├── proto
│   │   └── kvstore.proto - Completed gRPC proto file
│
├── ingestion
│   ├── RAG
│   │   ├── output - Vectorized textbook chunks (jsonl files produced offline)
│   └── ingestion_client.py - Client that reads vectorized chunks and ingests them into the KVS
│
├── mcp_server
│   └── mcp_server.py - Completed get_text_from_keys implementation
│
├── server
│   └── server.py - Completed RPC logic for the key-value store
│
└── testBench
    └── test_kv_service.py - Unit tests validating gRPC service functionality
```

## How to Run Project

1. **Start the key-value server:**
```bash
cd /workspaces/project_1/server
python server.py
```

2. **Run the ingestion client to populate the store:**

```bash
cd /workspaces/project_1/ingestion
python ingestion_client.py
```

3. **Start the MCP server**
* Open `/workspaces/project_1/.vscode/mcp.json` in VS Code
* Click `start` which should be located just above our pre-defined MCP server `csci5105-rag-poc`


## Running Tests

Unit tests for the gRPC handlers are located in the `testBench/` directory and use Python's built-in `unittest` framework.

These tests directly invoke the service implementation (InMemoryKV) without starting a live gRPC server.


## What the Tests Cover

The provided unit tests validate the following RPC functionalities:

### Put
- Inserting a new key
- Overwriting an existing key
- Correct storage of both textbook chunks and embeddings

### GetText
- Retrieving an existing textbook chunk
- Correctly reporting missing keys

### Delete
- Deleting an existing key
- Correctly reporting when a key does not exist
- Removing both the textbook chunk and its embedding

### List
- Returning an empty list when the store is empty
- Returning all keys after inserts
- Correctly updating the returned key set after deletions

### Health
- Reporting correct server name and version
- Reporting an accurate key count before and after inserts

### Notes on the Test Design
- The tests call the server implementation (`InMemoryKV`) directly rather than running a gRPC network server.
- The in-memory dictionaries are cleared before each test to ensure a clean test environment.
- The test bench focuses on functional correctness of the RPC handlers.


### Steps to Run Tests

1. **Navigate to the project root**
```bash
cd /workspaces/project_1
```

2. **Run tests using Python’s unittest module**

```bash
python -m unittest testBench.test_kv_service
```

3. **Expected Successful Test Output** 

```bash
root ➜ /workspaces/project_1 (main) $ python -m unittest testBench.test_kv_service
Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.Loaded textbook_chunks and embeddings from disk via [kvstore.pkl]
[599] key/values loaded
.
----------------------------------------------------------------------
Ran 7 tests in 1.076s

OK
```

