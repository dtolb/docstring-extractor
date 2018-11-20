# Example: stop bridging audio 
my_bridge = api.get_bridge('brg-bridgeId')
print(my_bridge["bridgeAudio"])
## True
api.update_bridge(my_bridge['id'], call_ids = ['callId1', 'callId2'], bridge_audio = False)
my_bridge = api.get_bridge(my_bridge['id'])
print(my_bridge["bridgeAudio"])
## False
