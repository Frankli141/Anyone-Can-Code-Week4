import requests
import json
import pprint

#------------------------------------
# PJ Version - pajohns3@cisco.com
# for Anyone Can Code Week 4
#------------------------------------

#Disable annoying warnings
import urllib3
urllib3.disable_warnings()

# Import Webex Teams Bot Token
import CRED

BOT_TOKEN = CRED.TOKEN


#Start of functions
def list_people_email(emailaddr):
	''' List people by email '''

# PJ

	url = 'https://webexapis.com/' + '/v1/people'

	headers = {'Authorization': 'Bearer ' + BOT_TOKEN}

	payload = {'email' : emailaddr}
	
	response = requests.get(url, headers=headers, params=payload, verify=False)

	pprint.pprint(response.json())




def list_people_displayname(dispname):
	''' List people by display name '''

# PJ

	url = 'https://webexapis.com/' + '/v1/people'

	headers = {'Authorization': 'Bearer ' + BOT_TOKEN}

	payload = {'displayName' : dispname}
	
	response = requests.get(url, headers=headers, params=payload, verify=False)

	pprint.pprint(response.json())


def get_person_detail_ID():
	''' Get a person's detail by their unique ID '''

	# <Add your code here>



def me():
	''' Get the Webex Teams bot's details '''

	url = 'https://webexapis.com/' + '/v1/people/me'

	headers = {'Authorization': 'Bearer ' + BOT_TOKEN}
	
	response = requests.get(url, headers=headers, verify=False)

	pprint.pprint(response.json())

	return response

def list_room():
	''' List the rooms the Webex Teams bot is in '''

	# PJ

	url = 'https://webexapis.com/' + '/v1/rooms'

	headers = {'Authorization': 'Bearer ' + BOT_TOKEN}
	
	response = requests.get(url, headers=headers, verify=False)

	pprint.pprint(response.json())

	return response



def create_room():
	''' Create a Webex Teams room '''

	# <Add your code here>



def get_rooms():
	''' List the rooms the Webex Teams bot is in '''
	# PJ

	url = 'https://webexapis.com/' + '/v1/rooms'

	headers = {'Authorization': 'Bearer ' + BOT_TOKEN}
	
	response = requests.get(url, headers=headers, verify=False)

	pprint.pprint(response.json())

	return response



def get_room_detail():
	''' Get the details of a room '''

	# <Add your code here>

def delete_room():
	''' Delete a room by ID '''

	# <Add your code here>



def list_message():
	''' List messages in a room '''

	# <Add your code here>



def create_message():
	''' Create a message for a room '''

	# <Add your code here>



def get_message_detail():
	''' Get the details of a message '''

	# <Add your code here>



def delete_message():
	''' Delete a meessage '''

	# <Add your code here>



if __name__ == '__main__':

	#me()
	#get_rooms()

	#PJ - Get People info by email address
	#mail_input = input("Search user by email, enter email address: ")
	#ist_people_email(email_input)

	#PJ - Get People info by email address
	dispname = input("Search user by name, enter name: ")
	list_people_displayname(dispname)
	