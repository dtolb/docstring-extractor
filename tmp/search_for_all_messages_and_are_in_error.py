# Example: Search for all messages and are in error 
message_list = api.list_messages()
for message in message_list:
    if message['state'] == 'error':
        print(message['id'])
## m-it6ewpyiyadfe
## m-pjnqofcjyadfe
## m-t2gspvs6iadfe
## m-shuh6d6pyadfe
