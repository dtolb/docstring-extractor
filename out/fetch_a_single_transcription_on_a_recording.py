# Example: Fetch a single transcription on a recording 
my_transcription = api.get_transcription('recordingId', 'transcriptionId')
print(my_transcription)
## {
##     'chargeableDuration': 11,
##     'id'                : '{transcriptionId}',
##     'state'             : 'completed',
##     'text'              : 'Hey there, I was calling to talk about plans for this saturday. ',
##     'textSize'          : 63,
##     'textUrl'           : 'https://api.catapult.inetwork.com/.../media/{transcriptionId}',
##     'time'              : '2014-12-23T23:08:59Z'
## }
