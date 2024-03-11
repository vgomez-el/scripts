import json
import random
import sys
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

# Read arguments from the command line
if len(sys.argv) != 5:
    print("Usage: script.py cloud_id username password number_of_documents")
    sys.exit(1)

cloud_id = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
number_of_documents_str = sys.argv[4]
number_of_documents = int(number_of_documents_str)

# Define names for the 30000 fields and their types
field_types = {}
for i in range(1, 30001):
    if i % 4 == 0:
        field_types[f'field_{i}'] = 'bool'
    elif i % 4 == 1:
        field_types[f'field_{i}'] = 'int'
    elif i % 4 == 2:
        field_types[f'field_{i}'] = 'float'
    else:
        field_types[f'field_{i}'] = 'text'

# Functions to generate random values
def random_text(length=10):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

def random_int():
    return random.randint(1, 10000)

def random_float():
    return random.uniform(1.0, 10000.0)

def random_bool():
    return random.choice([True, False])

def generate_document():
    # Add a unique timestamp field to each document in milliseconds
    timestamp_in_millis = int(datetime.now().timestamp() * 1000)
    document = {"timestamp": timestamp_in_millis}
    for field_name, field_type in field_types.items():
        if field_type == 'text':
            document[field_name] = random_text()
        elif field_type == 'int':
            document[field_name] = random_int()
        elif field_type == 'float':
            document[field_name] = random_float()
        elif field_type == 'bool':
            document[field_name] = random_bool()
    return document

# Connect to Elasticsearch cloud instance using basic authentication
es = Elasticsearch(
    cloud_id=cloud_id,
    basic_auth=(username, password)
)

def ensure_index(index_name):
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body={"settings": {"index.mapping.total_fields.limit": 40000}})
        print(f"Index {index_name} created.")
    else:
        print(f"Index {index_name} already exists.")

# Index name
index_name = "generated_index_big_docs"

# Ensure the index is ready
ensure_index(index_name)

# Ingest multiple documents
for i in range(number_of_documents):
    doc = generate_document()
    document_id = f"test-document-{i+1}"
    print(f"Attempting to insert document {i+1} with {len(doc)} fields.")
    response = es.index(index=index_name, id=document_id, document=doc)
    print(f"Document {i+1} response:", response)
