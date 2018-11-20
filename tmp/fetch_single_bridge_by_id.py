# Example: Fetch single bridge by ID 
my_bridge = api.get_bridge('brg-bridgeId')
print(my_bridge)
## {   'bridgeAudio': True,
##     'calls'      : 'https://api.catapult.inetwork.com/v1/users/u-123/bridges/brg-bridgeId/calls',
##     'createdTime': '2017-01-26T01:15:09Z',
##     'id'         : 'brg-bridgeId',
##     'state'      : 'created'}
print(my_bridge["state"])
## created
