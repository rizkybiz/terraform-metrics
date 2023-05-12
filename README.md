# Terraform-Metrics

# Install Instructions
- Clone this repo: `git clone git@github.com:rizkybiz/terraform-metrics.git`
- Install python3 requirements: `pip install -r requirements.txt`

## Usage
```
usage: python3 tf-metrics.py [-h] -t TOKEN -o ORGANIZATION [-u URL]

Get the total number of runs of all Terraform Workspaces in the provider
Organization

required arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        TFE/TFC User Token
  -o ORGANIZATION, --organization ORGANIZATION
                        TFE/TFC Organization to target
optional arguments:
  -u URL, --url URL     URL of TFE instance without scheme (https://).
                        Defaults to TFC
```