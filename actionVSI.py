import os
from ibm_vpc import VpcV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Get environment variables

API_KEY = os.environ['api_key']
REGION = os.environ['region']
VSI_ACTION = os.environ['action']
INSTANCES_ID = os.environ['instances_id']

#Authenticate user on IBM Cloud to do VPC VSI commands
authenticator = IAMAuthenticator(apikey=API_KEY,disable_ssl_verification=True)
service = VpcV1(authenticator=authenticator)
service.set_disable_ssl_verification(True)

#Set API endpoints
service.set_service_url('https://' + REGION + '.iaas.cloud.ibm.com/v1')
# Perform action on list
for instance_id in INSTANCES_ID.split(','):
    print('--------- Performing action on instance: ' + instance_id + ' | Type: ' + VSI_ACTION + ' ---------')
    response = service.create_instance_action(
        instance_id,
        type = VSI_ACTION,
    )