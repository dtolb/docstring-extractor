# Examples: Play either file for speak sentence 
api.play_audio_to_bridge('bridgeId', fileUrl='http://host/path/file.mp3')
api.play_audio_to_bridge('bridgeId', sentence='Press 0 to complete call', gender='female')
# or with extension methods
api.play_audio_file_to_bridge('bridgeId', 'http://host/path/file.mp3')
api.speak_sentence_to_bridge('bridgeId', 'Hello')
