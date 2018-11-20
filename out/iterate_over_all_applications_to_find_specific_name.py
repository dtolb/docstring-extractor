# Example: Iterate over all applications to find specific name 
apps = api.list_applications(size=20)
app_name = ""
while app_name != "MyAppName":
    my_app = next(apps)
    app_name = my_app["name"]
print(my_app)
## {   'autoAnswer': True,
##     'callbackHttpMethod': 'get',
##     'id': 'a-asdf',
##     'incomingCallUrl': 'https://test.com/callcallback/',
##     'incomingMessageUrl': 'https://test.com/msgcallback/',
##     'name': 'MyAppName'
## }
