# Example: Search for 3 toll free numbers with pattern 456 
numbers = api.search_available_toll_free_numbers(pattern = '*456', quantity = 3)
print(numbers)
## [   {   'nationalNumber': '(844) 489-0456',
##         'number'        : '+18444890456',
##         'patternMatch'  : '           456',
##         'price'         : '0.75'},
##     {   'nationalNumber': '(844) 498-2456',
##         'number'        : '+18444982456',
##         'patternMatch'  : '           456',
##         'price'         : '0.75'},
##     {   'nationalNumber': '(844) 509-4566',
##         'number'        : '+18445094566',
##         'patternMatch'  : '          456 ',
##         'price'         : '0.75'}]
print(numbers[0]["number"])
## +18444890456
