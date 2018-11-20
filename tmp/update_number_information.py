# Example: Update number information 
my_number = api.get_phone_number(number_id)
print(my_number)
## {
##     'city'          :'RALEIGH',
##     'createdTime'   :'2017-02-06T18:27:14Z',
##     'id'            :'n-123',
##     'nationalNumber':'(919) 561-5039',
##     'number'        :'+19195615039',
##     'numberState'   :'enabled',
##     'price'         :'0.35',
##     'state'         :'NC'
## }
api.update_phone_number(number_id, name='demo name')
my_number = api.get_phone_number(number_id)
print(my_number)
## {
##     'id'            :'n-123',
##     'number'        :'+19195615039',
##     'nationalNumber':'(919) 561-5039',
##     'name'          :'demo name',
##     'createdTime'   :'2017-02-06T18:41:56Z',
##     'city'          :'RALEIGH',
##     'state'         :'NC',
##     'price'         :'0.35',
##     'numberState'   :'enabled'
## }
