# Example: Toggle the call recording 
my_call_id = api.create_call(to='+19192223333', from_='+18281114444')
my_call = api.get_call(my_call_id)
print(my_call['recordingEnabled'])
## False
api.toggle_call_recording(my_call_id)
my_call = api.get_call(my_call_id)
print(my_call['recordingEnabled'])
## True
api.toggle_call_recording(my_call_id)
my_call = api.get_call(my_call_id)
print(my_call['recordingEnabled'])
## False
