# Play audio in file 
api.play_audio_to_call('callId', fileUrl= 'http://host/path/file.mp3')
api.play_audio_to_call('callId', sentence='Press 0 to complete call', gender='female')
# or with extension methods
api.play_audio_file_to_call('callId', 'http://host/path/file.mp3')
api.speak_sentence_to_call('callId', 'Hello')
