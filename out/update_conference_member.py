# Example: update conference member 
my_conf_id = api.create_conference(from_='+19192223333')
print(my_conf)
# conf-confId
my_call_id = api.create_call(from_='+19192223333', to='+19192223334', conference_id= 'conf-confId')
print(my_call_id)
# c-callId
my_conf_member_id = api.create_conference_member(my_conf_id, call_id=my_call_id, join_tone=True)
print(my_conf_member_id)
# member-memberId
my_conf_member = api.get_conference_member(my_conf_id, my_member_id)
print(my_conf_member)
## {
##     'addedTime': '2017-01-30T22:01:11Z',
##     'call'         : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId',
##     'hold'         : False,
##     'id'           : 'member-memberId',
##     'joinTone'     : True,
##     'leavingTone'  : False,
##     'mute'         : False,
##     'removedTime'  : '2017-01-30T22:01:21Z',
##     'state'        : 'active'
## }
api.update_conference_member(my_conf_id, my_member_id, mute=True, hold=True)
my_conf = api.get_conference_member(my_member_id)
## {
##     'addedTime': '2017-01-30T22:01:11Z',
##     'call'         : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId',
##     'hold'         : True,
##     'id'           : 'member-memberId',
##     'joinTone'     : True,
##     'leavingTone'  : False,
##     'mute'         : True,
##     'removedTime'  : '2017-01-30T22:01:21Z',
##     'state'        : 'active'
## }
