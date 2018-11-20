# Example: Fetch single application 
my_app = api.get_application(my_app_id)
print(my_app)
## {   'autoAnswer': True,
##     'callbackHttpMethod': 'get',
##     'id': 'a-1232asf123',
##     'incomingCallUrl': 'http://callback.com/calls',
##     'incomingMessageUrl': 'http://callback.com/messages',
##     'incomingSmsUrl': 'http://callback.com/messages',
##     'name': 'MyFirstApp2'
## }
print(my_app["id"])
## a-1232asf123
