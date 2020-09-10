import requests
import json
import pprint

#Disable annoying warnings
import urllib3
urllib3.disable_warnings()

# Import Webex Teams Bot Token
import CRED

BOT_TOKEN = CRED.TOKEN


#Start of functions
def list_people_email():
	''' List people by email '''

	# <Add your code here>



def list_people_displayname():
	''' List people by display name '''

	# <Add your code here>



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

	# <Add your code here>



def create_room():
	''' Create a Webex Teams room '''

	# <Add your code here>



def get_rooms():
	''' List the rooms the Webex Teams bot is in '''

	# <Add your code here>



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
	print("Testing pull requests")