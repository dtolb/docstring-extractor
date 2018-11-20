# Example: Search _and_ order a single number 
ordered_numbers = api.search_and_order_available_numbers(zip = '27606', quantity = 1)
print(ordered_number)
## [   {   'city'          : 'RALEIGH',
##         'id'            : 'n-abc',
##         'location'      : 'https://api.catapult.inetwork.com/v1/users/u-12/phoneNumbers/n-abc',
##         'nationalNumber': '(919) 222-4444',
##         'number'        : '+19192224444',
##         'price'         : '0.35',
##         'state'         : 'NC'}]
