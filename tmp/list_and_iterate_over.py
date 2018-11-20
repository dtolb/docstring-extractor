# Example: List and iterate over 
endpoint_list = api.list_domain_endpoints('rd-domainId', size=1000)
for endpoint in endpoint_list:
    print(endpoint['id'])
##re-endpointId1
##re-endpointId2
