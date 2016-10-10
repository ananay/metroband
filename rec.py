# @Author: ananayarora
# @Date:   2016-10-10T11:25:39+05:30
# @Last modified by:   ananayarora
# @Last modified time: 2016-10-10T11:26:07+05:30



import artikcloud
from artikcloud.rest import ApiException
import sys, getopt
import time, random, json
from pprint import pprint


# SDK reference for more details
# https://github.com/artikcloud/artikcloud-python
def main(argv):

	DEFAULT_CONFIG_PATH = 'config.json'

	with open(DEFAULT_CONFIG_PATH, 'r') as config_file:
		config = json.load(config_file)['metroBeaconSensor']
	print(config)

	# Configure Oauth2 access_token for the client application.  Here we have used
	# the device token for the configuration
	artikcloud.configuration = artikcloud.Configuration();
	artikcloud.configuration.access_token = config['deviceToken']

	# We create an instance of the Message API class which provides
	# the send_message() and get_last_normalized_messages() api call
	# for our example
	api_instance = artikcloud.MessagesApi()

	# parameters for our request
	sdids = config['deviceId'] # str | Comma separated list of source device IDs (minimum: 1). (required)
	#count = 10 # int | Number of items to return per query. (optional)
	#field_presence = None # str | String representing a field from the specified device ID. (optional)

	try:
		 # Debug Print oauth settings
	    pprint(artikcloud.configuration.auth_settings())

	    # Get Last Normalized Message
	    api_response = api_instance.get_last_normalized_messages(sdids=sdids)
	    pprint(api_response)
	except ApiException as e:
	    print "Exception when calling MessagesApi->get_last_normalized_messages: %s\n" % e


if __name__ == "__main__":
   main(sys.argv[1:])
