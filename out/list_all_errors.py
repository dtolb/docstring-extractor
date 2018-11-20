# Example: List all errors 
error_list = api.list_errors()
print(list(error_list))
# [{
#     'category':'unavailable',
#     'code'    :'number-allocator-unavailable',
#     'details':[
#         {
#             'id'   :'ued-eh3zn3dxgiin4y',
#             'name' :'requestPath',
#             'value':'availableNumbers/local'
#         },
#         {
#             'id'   :'ued-3fsdqiq',
#             'name' :'remoteAddress',
#             'value':'216.82.234.65'
#         },
#         {
#             'id'   :'ued-2r4t47bwi',
#             'name' :'requestMethod',
#             'value':'GET'
#         }
#     ],
#     'id'     :'ue-upvfv53xzca',
#     'message':'Cannot connect to the number allocator',
#     'time'   :'2016-03-28T18:31:33Z'
# },
# {
#     'category':'unavailable',
#     'code':'number-allocator-unavailable',
#     'details':[
#         {
#             'id':'ued-kntwx7vyotalci',
#             'name':'requestPath',
#             'value':'availableNumbers/local'
#         },
#         {
#             'id':'ued-b24vxpfskldq',
#             'name':'remoteAddress',
#             'value':'216.82.234.65'
#         },
#         {
#             'id':'ued-ww5rcgl7zm2ydi',
#             'name':'requestMethod',
#             'value':'GET'
#         }
#     ],
#     'id':'ue-pok2vg7kyuzaqq',
#     'message':'Cannot connect to the number allocator',
#     'time':'2016-03-28T18:31:33Z'
# }]
