# Example: Transfer with whisper 
my_sentence = api.build_sentence(sentence = "Hello from Bandwidth",
                     gender="Female",
                     locale="en_UK",
                     voice="Bridget",
                     loop_enabled=True
                    )
my_call = api.get_call('c-callId')
api.transfer_call('c-callId', to = '+1234564890', caller_id = my_call['from'], whisper_audio = my_sentence )
