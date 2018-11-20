# Example: Search, order, and fetch Number information 
available_numbers = api.search_available_local_numbers(city='Raleigh', state='NC')
number_id = api.order_phone_number(available_numbers[0]['number'])
print(number_id)
# n-123
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
