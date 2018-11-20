# Example: Search then order a single toll-free number 
numbers = api.search_and_order_toll_free_numbers(quantity = 1)
print(numbers)
## [   {   'location'      : 'https://api.catapult.inetwork.com/v1/users/u-123/phoneNumbers/n-abc',
##         'nationalNumber': '(844) 484-1048',
##         'number'        : '+18444841048',
##         'price'         : '0.75'}]
print(numbers[0]["number"])
## +18444841048
