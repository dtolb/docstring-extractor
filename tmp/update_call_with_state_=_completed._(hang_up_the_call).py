# Update call with state = completed. (Hang up the call) 
my_call = api.get_call(call_id)
my_call_state = my_call['state']
print(my_call_state)
## started
api.update_call(my_call['id'], state='completed')
my_call = api.get_call(my_call['id'])
print(my_call['state'])
## completed
