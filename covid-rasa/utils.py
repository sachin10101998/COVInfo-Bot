import urls
import requests
import json
def get_confirmed_cases_by_state(state_name):
	url = urls.uri+"/covidapp/states/"+state_name+"/confirmedcases"  # base url
	headers = {'content-type': 'application/json'}
	response = requests.request("GET",url, headers=headers)
	response = json.loads(response.text)
	return response 

def get_active_cases_by_state(state_name):
	url = urls.uri+"/covidapp/states/"+state_name+"/activecases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text) 
	return response  

def get_dead_cases_by_state(state_name):
	url = urls.uri+"/covidapp/states/"+state_name+"/deadcases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text)  
	return response  

def get_recovered_cases_by_state(state_name):
	url = urls.uri+"/covidapp/states/"+state_name+"/recoveredcases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text)  
	return response  

def get_confirmed_cases_by_district(district_name):
	url = urls.uri+"/covidapp/districts"+district_name+"/confirmedcases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text)  
	return response  

def get_active_cases_by_district(district_name):
	url = urls.uri+"/covidapp/districts"+district_name+"/activecases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text)  
	return response  

def get_dead_cases_by_district(district_name):
	url = urls.uri+"/covidapp/districts"+district_name+"/deadcases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text) 
	return response  

def get_recovered_cases_by_district(district_name):
	url = urls.uri+"/covidapp/districts"+district_name+"/recoveredcases"  # base url

	headers = {'content-type': 'application/json'}

	response = requests.request("GET",url, headers=headers)

	response = json.loads(response.text)  
	return response  
