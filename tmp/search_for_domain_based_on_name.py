# Example: Search for domain based on name 
domain_list = api.list_domains(size=100)
domain_name = ''
while domain_name != 'My Prod Site':
    my_domain = next(domain_list)
    domain_name = my_domain['name']
print(my_domain)
## {   'description' : 'Python Docs Example',
##     'endpointsUrl': 'https://api.catapult.inetwork.com/v1/users/u-abc123/domains/rd-domainId/endpoints',
##     'id'          : 'rd-domainId',
##     'name'        : 'My Prod Site'}
