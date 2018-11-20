# Example: Create Endpoint on Domain 'rd-domainId' then fetch the endpoint 
endpoint_id = api.create_domain_endpoint('rd-domainId',
                                         endpoint_name='User3_endpoint',
                                         password='AtLeast6Chars')
print(endpoint_id)
# re-endpointId3
my_endpoint = api.get_domain_endpoint(endpoint_id)
print(my_endpoint)
## {
##     'credentials' :{
##         'realm'   :'qwerty.bwapp.bwsip.io',
##         'username':'User3_endpoint'
##     },
##     'domainId'    :'rd-domainId',
##     'enabled'     :True,
##     'id'          :'re-endpointId3',
##     'name'        :'User3_endpoint',
##     'sipUri'      :'sip:user5@qwerty.bwapp.bwsip.io'
## }
