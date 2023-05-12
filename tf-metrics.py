import requests
import argparse

# set up argparse
parser = argparse.ArgumentParser(description="Get the total number of runs of all Terraform Workspaces in the provider Organization")
parser.add_argument('-t', '--token', help="TFE/TFC User Token", required=True)
parser.add_argument('-o', '--organization', help="TFE/TFC Organization to target", required=True)
parser.add_argument('-u', '--url', help="URL of TFE instance without scheme (https://). Defaults to TFC")
args = vars(parser.parse_args())

# handle args
if args['url'] != None:
    tf_api_url = 'https://'+args['url']+'/api/v2'
else:
  tf_api_url = 'https://app.terraform.io/api/v2/'
token = args['token']
org_name = args['organization']

# set up http request
request_headers = {"Authorization": "Bearer "+token}
url = tf_api_url + 'organizations/'+org_name+'/workspaces'

# fetch workspaces
flag = False
workspaces = []
while flag == False:
    r = requests.get(url, headers=request_headers)
    json_response = r.json()
    for workspace in json_response['data']:
        workspaces.append(workspace)
    url = json_response['links']['next']
    if url == None:
        flag = True

url = tf_api_url + 'workspaces'
total_runs = 0

# iterate through individual workspaces and get applies
for workspace in workspaces:
    r = requests.get(url+"/"+workspace['id'], headers=request_headers)
    json_response = r.json()
    if json_response['data']['attributes']['workspace-kpis-runs-count'] != None:
      total_runs += json_response['data']['attributes']['workspace-kpis-runs-count']

print("Total runs for the " + org_name + " organization: " + str(total_runs))