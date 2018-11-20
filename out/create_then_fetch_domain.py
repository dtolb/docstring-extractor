# Example: Create then fetch domain 
domain_id = api.create_domain(name='qwerty', description='Python Docs Example')
print(domain_id)
# rd-domainId
my_domain = api.get_domain(domain_id)
print(my_domain)
## {   'description' : 'Python Docs Example',
##     'endpointsUrl': 'https://api.catapult.inetwork.com/v1/users/u-abc123/domains/rd-domainId/endpoints',
##     'id'          : 'rd-domainId',
##     'name'        : 'qwerty'}
