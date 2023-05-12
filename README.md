# Terraform-Metrics
```
usage: tf-metrics.py [-h] -t TOKEN -o ORGANIZATION [-u URL]

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