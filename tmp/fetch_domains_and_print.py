# Example: Fetch domains and print 
domain_list = api.list_domains(size=10)
print(list(domain_list))
## [{   'endpointsUrl': 'https://api.catapult.inetwork.com/v1/users/u-abc123/domains/endpoints',
##     'id'           : 'rd-domainId',
##     'name'         : 'siplearn1'},
## {   'endpointsUrl' : 'https://api.catapult.inetwork.com/v1/users/u-abc123/domains/endpoints',
##     'id'           : 'rd-domainId2',
##     'name'         : 'siplearn2'}]
