#!/usr/bin/env bash
set -e

if [ $# -lt 1 ]; then
  echo "Usage: $0 <download_url> [cloud_params] [localhost]"
  exit 1
fi

download_url="$1"
package_name=$(basename "$download_url")
cloud_params="$2"
localhost="$3"

# Download the Auditbeat package
curl -L -O "$download_url"

# Extract the package
tar -xzf "$package_name"

# Get the extracted directory name
extracted_dir=$(tar -tzf "$package_name" | head -n 1 | awk -F/ '{print $1}')

# Change into the extracted directory
cd "$extracted_dir"

# Configure cloud.id and cloud.auth if provided and localhost is not provided
if [ -n "$cloud_params" ] && [ -z "$localhost" ]; then

  # Split cloud_params into cloud_id and cloud_auth using comma as separator
  IFS=',' read -ra cloud_array <<< "$cloud_params"
  cloud_id="${cloud_array[0]}"
  cloud_auth="${cloud_array[1]}"

# Update the values of cloud.id and cloud.auth
  sudo sed -i".bak" -e "s|^#cloud.id:.*|cloud.id: \"$cloud_id\"|" -e "s|^#cloud.auth:.*|cloud.auth: \"$cloud_auth\"|" auditbeat.yml
else
  # Comment out the lines of cloud.id and cloud.auth if uncommented
  sudo sed -i'.bak' -e 's/cloud.id:/#cloud.id:/' -e 's/cloud.auth:/#cloud.auth:/' auditbeat.yml
fi

# Uncomment line 82 if localhost is specified as parameter
if [ -n "$localhost" ]; then
  sudo sed -i'.bak' '82s/^#//' auditbeat.yml
fi

# Add execute permissions to the necessary files
sudo chmod +x auditbeat*

# Make the auditbeat.yml file owned by root
sudo chown -R "$(whoami)" .

# Configure Auditbeat
sudo ./auditbeat setup

# Start Auditbeat as a background process
sudo ./auditbeat -e
