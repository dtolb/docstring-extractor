# Example: Fetch and list conference members 
my_conf_id = api.create_conference(from_='+19192223333')
print(my_conf)
# conf-confId
my_call_id = api.create_call(from_='+19192223333', to='+19192223334', conference_id= 'conf-confId')
print(my_call_id)
# c-callId
my_conf_member_id = api.create_conference_member(my_conf_id, call_id=my_call_id)
print(my_conf_member_id)
# member-memberId
my_conference_members = list_conference_members(my_conf_id)
print(list(my_conference_members))
## [
##    {
##       'addedTime'  :'2017-01-30T22:01:11Z',
##       'call'       :'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId',
##       'hold'       :False,
##       'id'         :'member-memberId',
##       'joinTone'   :False,
##       'leavingTone':False,
##       'mute'       :False,
##       'removedTime':'2017-01-30T22:01:21Z',
##       'state'      :'completed'
##    }
## ]
