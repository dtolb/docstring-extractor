# Example: Bulk Send Picture or Text messages (or both) 
results = api.send_messages([
    {'from': '+1234567980', 'to': '+1234567981', 'text': 'SMS message'},
    {'from': '+1234567980', 'to': '+1234567982', 'text': 'SMS message2'}
])
