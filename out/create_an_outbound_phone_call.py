# Example: Create an outbound phone call 
call_id = api.create_call(from_='+1234567890',
                          to='+1234567891',
                          callback_url='http://yoursite.com/calls')
print(call_id)
## c-abc123
my_call = api.get_call(call_id)
print(my_call)
## {   'callbackUrl'         : 'http://yoursite.com/calls',
##     'direction'           : 'out',
##     'events'              : 'https://api.catapult.inetwork.com/v1/users/u-abc/calls/c-abc123/events',
##     'from'                : '+1234567890',
##     'id'                  : 'c-abc123',
##     'recordingEnabled'    : False,
##     'recordingFileFormat' : 'wav',
##     'recordings'          : 'https://api.catapult.inetwork.com/v1/users/u-abc/calls/c-abc123/recordings',
##     'startTime'           : '2017-01-26T16:10:11Z',
##     'state'               : 'started',
##     'to'                  : '+1234567891',
##     'transcriptionEnabled': False,
##     'transcriptions'      : 'https://api.../v1/users/u-abc/calls/c-abc123/transcriptions'}
