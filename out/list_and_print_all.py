# Example: List and print all 
endpoint_list = api.list_domain_endpoints('rd-domainId', size=1000)
print(list(endpoint_list))
## [
##     {
##         'applicationId':'a-appId',
##         'credentials'  :{
##             'realm'    :'creds.bwapp.bwsip.io',
##             'username' :'user1'
##         },
##         'description'  :"Your SIP Account",
##         'domainId'     :'rd-domainId',
##         'enabled'      :True,
##         'id'           :'re-endpointId1',
##         'name'         :'User1_endpoint',
##         'sipUri'       :'sip:user1@creds.bwapp.bwsip.io'
##     },
##     {
##         'applicationId':'a-appId',
##         'credentials'  :{
##             'realm'    :'creds1.bwapp.bwsip.io',
##             'username' :'user2'
##         },
##         'description'  :"Your SIP Account",
##         'domainId'     :'rd-domainId',
##         'enabled'      :True,
##         'id'           :'re-endpointId2',
##         'name'         :'User2_endpoint',
##         'sipUri'       :'sip:user2@creds.bwapp.bwsip.io'
##     }
## ]
