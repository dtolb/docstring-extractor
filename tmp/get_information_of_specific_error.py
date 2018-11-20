# Example: Get information of specific error 
error = api.get_error('ue-errorId')
print(error)
## {
##     'category':'unavailable',
##     'code'    :'number-allocator-unavailable',
##     'details' :[
##         {
##            'id'      :'ued-kntvyotalci',
##            'name'    :'requestPath',
##            'value'   :'availableNumbers/local'
##         },
##         {
##            'id'      :'ued-b2dq',
##            'name'    :'remoteAddress',
##            'value'   :'216.82.234.65'
##         },
##         {
##            'id'      :'ued-wzm2ydi',
##            'name'    :'requestMethod',
##            'value'   :'GET'
##         }
##     ],
##     'id'      :'ue-errorId',
##     'message' :'Cannot connect to the number allocator',
##     'time'    :'2016-03-28T18:31:33Z'
## }
