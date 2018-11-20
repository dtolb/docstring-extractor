# Example: Delete single application 
api.delete_application('a-appId')
try :
    api.get_application('a-appId')
except CatapultException as err:
    print(err.message)
## The application a-appId could not be found
