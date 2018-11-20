# Example: Fetch recording information 
my_recording = api.get_recording('recordingId2')
print(my_recording)
## {
##     'call'     :'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId2',
##     'endTime'  :'2017-01-30T17:53:30Z',
##     'id'       :'rec-recordingId2',
##     'media'    :'https://api.catapult.inetwork.com/v1/users/u-abc123/media/c-callId2-1.wav',
##     'mediaName':'c-callId2-1.wav',
##     'startTime':'2017-01-30T17:53:20Z',
##     'state'    :'complete'
## }
