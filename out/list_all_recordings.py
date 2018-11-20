# Example: List all recordings 
recording_list = api.list_recordings(size=1000)
print(recording_list)
## [
##     {
##         'call'     :'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId',
##         'endTime'  :'2017-01-30T17:58:45Z',
##         'id'       :'rec-recordingId',
##         'media'    :'https://api.catapult.inetwork.com/v1/users/u-abc123/media/c-callId-1.wav',
##         'mediaName':'c-callId-1.wav',
##         'startTime':'2017-01-30T17:58:34Z',
##         'state'    :'complete'
##     },
##     {
##         'call'     :'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId2',
##         'endTime'  :'2017-01-30T17:53:30Z',
##         'id'       :'rec-recordingId2',
##         'media'    :'https://api.catapult.inetwork.com/v1/users/u-abc123/media/c-callId2-1.wav',
##         'mediaName':'c-callId2-1.wav',
##         'startTime':'2017-01-30T17:53:20Z',
##         'state'    :'complete'
##     }
## ]
