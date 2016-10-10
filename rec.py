import artikcloud
from artikcloud.rest import ApiException
import sys, getopt
import time, random, json
from pprint import pprint

def main(argv):

	DEFAULT_CONFIG_PATH = 'config.json'

	with open(DEFAULT_CONFIG_PATH, 'r') as config_file:
		config = json.load(config_file)['metroBeaconSensor']
	print(config)

	artikcloud.configuration = artikcloud.Configuration();
	artikcloud.configuration.access_token = config['deviceToken']

	api_instance = artikcloud.MessagesApi()

	sdids = config['band_id'] 
	try:
	    pprint(artikcloud.configuration.auth_settings())
	    api_response = api_instance.get_last_normalized_messages(sdids=sdids)
	    pprint(api_response)
	except ApiException as e:
	    print "Exception when calling MessagesApi->get_last_normalized_messages: %s\n" % e


if __name__ == "__main__":
   main(sys.argv[1:])
