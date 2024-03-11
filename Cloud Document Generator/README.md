# Elasticsearch Document Generator Script

## Overview

This Python script is designed to generate and insert documents into an Elasticsearch index stored in a cloud deployment. Each document contains a predefined number of fields, including a unique timestamp field and various data types such as text, integer, float, boolean, and IP address. The primary purpose of this script is to facilitate testing and benchmarking for Elasticsearch deployments, allowing users to quickly populate an index with a large volume of structured data.

## Features

- **Dynamic Document Generation:** Generates documents with 30,000 fields of different data types, including a unique timestamp for each document.
- **Configurable Field Types:** Supports text, integer, float, boolean, and IP address data types.
- **Customizable Document Count:** Allows the user to specify the number of documents to generate and insert.
- **Index Preparation:** Automatically creates an Elasticsearch index with a configurable field limit and applies necessary settings before document insertion.
- **Input Parameter Flexibility:** Accepts Elasticsearch cloud configuration and authentication details as input parameters.

## Prerequisites

- Python 3.6 or later
- Elasticsearch 7.x or later
- The Elasticsearch Python client (`elasticsearch` package)

# Usage

## Installation

Before running the script, ensure that you have Python 3.6 (or later) installed on your system and the Elasticsearch Python client is installed. You can install the Elasticsearch client using pip:

```sh
pip install elasticsearch
```

## Setup:

Clone the repository or download the script multi_field.py:
```bash
git clone [repository_url]
```

## Usage:
Open your command line interface (CLI).
Command Syntax:

### For Python 3.x:
```bash
python3 multi_field.py [cloud_id] [username] [password] [number_of_documents]
```
### For Python 2.x:
```bash
python multi_field.py [cloud_id] [username] [password] [number_of_documents]
```
## Arguments:
- **cloud_id:** The cloud ID of the Elasticsearch instance.
- **username:** Username for authentication.
- **password:** Password for authentication.
- **number_of_documents:** Number of documents to generate and ingest.

## Examples:
To execute the script and ingest 100 documents into an Elasticsearch instance with the provided credentials:

```bash
python multi_field.py your_cloud_id your_username your_password 100
```
If you're unsure of the cloud ID, username, and password, refer to your Elasticsearch instance documentation or contact your administrator.

Note:
Ensure the Elasticsearch instance is reachable and properly configured.
Adjust the number of documents and field types as per your requirements.
The script may take some time to execute depending on the number of documents specified.