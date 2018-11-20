# Example: List Calls 
call_list = api.list_calls(to = '+19192223333', size = 2)
print(list(call_list))
## [
##   {
##     'activeTime'          : '2017-01-26T16:10:23Z',
##     'callbackUrl'         : 'http://yoursite.com/calls',
##     'chargeableDuration'  : 60,
##     'direction'           : 'out',
##     'endTime'             : '2017-01-26T16:10:33Z',
##     'events'              : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-abc123/events',
##     'from'                : '+17079311113',
##     'id'                  : 'c-abc123',
##     'recordingEnabled'    : False,
##     'recordingFileFormat' : 'wav',
##     'recordings'          : 'https://api.../v1/users/u-abc123/calls/c-abc123/recordings',
##     'startTime'           : '2017-01-26T16:10:11Z',
##     'state'               : 'completed',
##     'to'                  : '+19192223333',
##     'transcriptionEnabled': False,
##     'transcriptions'      : 'https://api.../v1/users/u-abc123/calls/c-abc123/transcriptions'
##   },
##   {
##     'activeTime'          : '2016-12-29T23:50:35Z',
##     'chargeableDuration'  : 60,
##     'direction'           : 'out',
##     'endTime'             : '2016-12-29T23:50:41Z',
##     'events'              : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-xyz987/events',
##     'from'                : '+19194443333',
##     'id'                  : 'c-xyz987',
##     'recordingEnabled'    : False,
##     'recordingFileFormat' : 'wav',
##     'recordings'          : 'https://api.../v1/users/u-abc123/calls/c-xyz987/recordings',
##     'startTime'           : '2016-12-29T23:50:15Z',
##     'state'               : 'completed',
##     'to'                  : '+19192223333',
##     'transcriptionEnabled': False,
##     'transcriptions'      : 'https://api.../v1/users/u-abc123/calls/c-xyz987/transcriptions'
##   }
## ]
