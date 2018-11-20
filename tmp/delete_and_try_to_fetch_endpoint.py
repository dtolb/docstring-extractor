# Example: Delete and try to fetch endpoint 
my_endpoint = api.get_domain_endpoint('rd-domainId', 're-endpointId')
print(my_endpoint)
## {
##     'credentials' :{
##         'realm'   :'qwerty.bwapp.bwsip.io',
##         'username':'user5'
##     },
##     'domainId'    :'rd-domainId',
##     'enabled'     :False,
##     'id'          :'re-endpointId3ndpointId',
##     'name'        :'user3',
##     'sipUri'      :'sip:user5@qwerty.bwapp.bwsip.io'
## }
api.delete_domain_endpoint(d, e)
try:
    my_endpoint = api.get_domain_endpoint(d, e)
except Exception as e:
    print(e)
## CatapultException(404, "The endpoint 're-endpointId' could not be found")
