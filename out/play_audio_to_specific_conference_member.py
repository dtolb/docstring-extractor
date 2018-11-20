# Example: Play audio to specific conference member 
api.play_audio_to_conference_member('conferenceId', 'memberId', fileUrl=http://host/path/file.mp3)
api.play_audio_to_conference_member('conferenceId', 'memberId',
                                    sentence='Press 0 to complete call', gender='female')
# or with extension methods
api.play_audio_file_to_conference_member('conferenceId', 'memberId', 'http://host/path/file.mp3')
api.speak_sentence_to_conference_member('conferenceId', 'memberId', 'Hello')
