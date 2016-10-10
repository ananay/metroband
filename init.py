import artikcloud
from artikcloud.rest import ApiException
import sys, getopt
import time, random, json
from pprint import pprint


def main(argv):

	DEFAULT_CONFIG_PATH = 'config.json'
  idnum = 100035  #unique band id
  destination_code = 73  #station code of the destination station
	with open(DEFAULT_CONFIG_PATH, 'r') as config_file:
		config = json.load(config_file)['metroBeaconSensor']
	print(config)
	
	artikcloud.configuration = artikcloud.Configuration();
	artikcloud.configuration.access_token = config['deviceToken']
	
	api_instance = artikcloud.MessagesApi()

	device_message = {}

	device_message['band_id'] = idnum
	device_message['dest'] = destination_code

	device_sdid = config['deviceId']

	ts = time.time()

	data = artikcloud.Message(device_message, device_sdid, ts)

	try:
	    pprint(artikcloud.configuration.auth_settings())

	    api_response = api_instance.send_message(data)
	    pprint(api_response)
	except ApiException as e:
	    print "Exception when calling MessagesApi->send_message: %s\n" % e


if __name__ == "__main__":
   main(sys.argv[1:])
