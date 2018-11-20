# Example: Fetch information about single message 
my_message = api.get_message('m-na6cpyjf2qcpz6l3drhcx7y')
print(my_message)
## {
##     'callbackUrl'             :'https://yoursite.com/message',
##     'direction'               :'in',
##     'from'                    :'+19193047864',
##     'id'                      :'m-messageId',
##     'media'                   :[],
##     'messageId'               :'m-messageId',
##     'skipMMSCarrierValidation':True,
##     'state'                   :'received',
##     'text'                    :'Hey there',
##     'time'                    :'2017-02-01T21:10:32Z',
##     'to'                      :'+19191234567'
## }
