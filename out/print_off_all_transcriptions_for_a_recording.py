# Example: Print off all transcriptions for a recording 
transcriptions_list = api.list_transcriptions('recordingId')
print(list(transcriptions_list))
## [
##     {
##         'chargeableDuration': 60,
##         'id': '{transcription-id}',
##         'state': 'completed',
##         'time': '2014-10-09T12:09:16Z',
##         'text': '{transcription-text}',
##         'textSize': 3627,
##         'textUrl': '{url-to-full-text}'
##     },
##     {
##         'chargeableDuration': 60,
##         'id': '{transcription-id}',
##         'state': 'completed',
##         'text': '{transcription-text}',
##         'time': '2014-10-09T14:04:44Z',
##         'textSize': 72,
##         'textUrl': '{url-to-full-text}'
##     }
## ]
