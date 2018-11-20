# Example: Update password and disable the endpoint 
my_endpoint = api.get_domain_endpoint('rd-domainId', 're-endpointId')
print(my_endpoint)
## {
##     'credentials' :{
##         'realm'   :'qwerty.bwapp.bwsip.io',
##         'username':'user5'
##     },
##     'domainId'    :'rd-domainId',
##     'enabled'     :True,
##     'id'          :'re-endpointId',
##     'name'        :'user3',
##     'sipUri'      :'sip:user5@qwerty.bwapp.bwsip.io'
## }
api.update_domain_endpoint('rd-domainId', 're-endpointId', enabled=False, password='abc123')
my_endpoint = api.get_domain_endpoint('rd-domainId', 're-endpointId')
print(my_endpoint)
## {
##     'credentials' :{
##         'realm'   :'qwerty.bwapp.bwsip.io',
##         'username':'user5'
##     },
##     'domainId'    :'rd-domainId',
##     'enabled'     :False,
##     'id'          :'re-endpointId',
##     'name'        :'user3',
##     'sipUri'      :'sip:user5@qwerty.bwapp.bwsip.io'
## }
