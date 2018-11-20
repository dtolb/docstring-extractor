# Example: List all phone numbers 
number_list = api.list_phone_numbers(size=1000)
print(list(number_list))
## [
##     {
##         'city'          :'RALEIGH',
##         'createdTime'   :'2017-02-06T18:41:37Z',
##         'id'            :'n-n123',
##         'name'          :'demo name',
##         'nationalNumber':'(919) 555-5346',
##         'number'        :'+19195555346',
##         'numberState'   :'enabled',
##         'price'         :'0.35',
##         'state'         :'NC'
##     },
##     {
##         'city'          :'RALEIGH',
##         'createdTime'   :'2017-02-06T18:41:56Z',
##         'id'            :'n-n1234',
##         'name'          :'demo name',
##         'nationalNumber':'(919) 555-5378',
##         'number'        :'+19195555378',
##         'numberState'   :'enabled',
##         'price'         :'0.35',
##         'state'         :'NC'
##     }
## ]
