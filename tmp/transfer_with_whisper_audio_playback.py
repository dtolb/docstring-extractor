# Example: Transfer with whisper audio playback 
my_audio = api.build_audio_playback('http://my_site.com/file.mp3', loop_enabled=True)
my_call = api.get_call('c-callId')
api.transfer_call('c-callId', to = '+1234564890', whisper_audio = my_audio )
