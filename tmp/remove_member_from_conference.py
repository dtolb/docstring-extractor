# Example: Remove Member from Conference 
my_conf = api.get_conference('conferenceId')
my_conf_members = list(api.list_conference_members(my_conf['id']))
print(my_conf_members)
## [{ 'addedTime'  : '2017-01-30T23:17:11Z',
##    'call'       : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId',
##    'hold'       : False,
##    'id'         : 'member-memberId',
##    'joinTone'   : False,
##    'leavingTone': False,
##    'mute'       : False,
##    'state'      : 'active'},
##  { 'addedTime'  : '2017-01-30T23:17:14Z',
##    'call'       : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId2',
##    'hold'       : False,
##    'id'         : 'member-memberId2',
##    'joinTone'   : False,
##    'leavingTone': False,
##    'mute'       : False,
##    'state'      : 'active'}]
api.remove_conference_member(my_conf['id'], my_conf_members[1]['id'])
my_conf_members = list(api.list_conference_members(my_conf['id']))
print(my_conf_members)
## [{ 'addedTime'  : '2017-01-30T23:17:11Z',
##    'call'       : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId',
##    'hold'       : False,
##    'id'         : 'member-memberId',
##    'joinTone'   : False,
##    'leavingTone': False,
##    'mute'       : False,
##    'state'      : 'active'},
##  { 'addedTime'  : '2017-01-30T23:17:14Z',
##    'call'       : 'https://api.catapult.inetwork.com/v1/users/u-abc123/calls/c-callId2',
##    'hold'       : False,
##    'id'         : 'member-memberId2',
##    'joinTone'   : False,
##    'leavingTone': False,
##    'mute'       : False,
##    'state'      : 'completed'}]
