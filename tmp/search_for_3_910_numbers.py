# Example: Search for 3 910 numbers 
numbers = api.search_available_local_numbers(area_code = '910', quantity = 3)
print(numbers)
## [   {   'city'          : 'WILMINGTON',
##         'nationalNumber': '(910) 444-0230',
##         'number'        : '+19104440230',
##         'price'         : '0.35',
##         'rateCenter'    : 'WILMINGTON',
##         'state'         : 'NC'},
##     {   'city'          : 'WILMINGTON',
##         'nationalNumber': '(910) 444-0263',
##         'number'        : '+19104440263',
##         'price'         : '0.35',
##         'rateCenter'    : 'WILMINGTON',
##         'state'         : 'NC'},
##     {   'city'          : 'WILMINGTON',
##         'nationalNumber': '(910) 444-0268',
##         'number'        : '+19104440268',
##         'price'         : '0.35',
##         'rateCenter'    : 'WILMINGTON',
##         'state'         : 'NC'}
## ]
print(numbers[0]["number"])
## +19104440230
