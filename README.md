# Auditbeat Installation Script

This script automates the installation and configuration of Auditbeat on a macOS system. Auditbeat is a lightweight shipper that sends audit events to an Elasticsearch or Logstash instance for analysis and monitoring.

## Usage

1. Clone this repository or download the `audit.sh` file.

2. Make the script executable:
   ```bash
   chmod +x audit.sh

3. Run the script with the following command:
   
    ./audit.sh <download_url> [cloud_params] [localhost]

        <download_url>: The URL to download the Auditbeat package. Example: https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.9.0-darwin-x86_64.tar.gz

        [cloud_params] (optional): Cloud ID and authentication credentials for connecting to Elasticsearch or Logstash in cloud mode. Use the format cloud_id,cloud_auth. Example: My_deployment:ZXVyb3BlLXdlc3QxLmdjcC5jbG91ZC5lcy5pbzo0NDMkMjNkN2FmYTE0MjI1NGYzNmE1NWE4OWYyZTc2ZmI1YWEkNTI2ZTYzNTRkOTkwNGM1OGE2NmY3NGZiMzNhODMyYmM=,elastic:PaSsPaSsPaSsPaSsPaSsPaSs.

        [localhost] (optional): Specify localhost to run Auditbeat in local mode without cloud configuration.

## Examples

### Install Auditbeat in cloud mode:
It will configure the Elastic cloud credentials and will start audit beat. Useful when you need to ingest auditbeat data into a cloud instance

    ./script.sh https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.9.0-darwin-x86_64.tar.gz "My_deployment:ZXVyb3BlLXdlc3QxLmdjcC5jbG91ZC5lcy5pbzo0NDMkMjNkN2FmYTE0MjI1NGYzNmE1NWE4OWYyZTc2ZmI1YWEkNTI2ZTYzNTRkOTkwNGM1OGE2NmY3NGZiMzNhODMyYmM=,elastic:PaSsPaSsPaSsPaSsPaSsPaSs."

### Install Auditbeat in local mode:
It will start auditbeat with default localhost configuration(http://localhost:5601/). Useful when you need to ingest auditbeat data into a local instance

    ./audit.sh https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.9.0-darwin-x86_64.tar.gz localhost

### Install Auditbeat with default configuration:

    ./audit.sh https://artifacts.elastic.co/downloads/beats/auditbeat/auditbeat-8.9.0-darwin-x86_64.tar.gz


