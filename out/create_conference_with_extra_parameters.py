# Example: create conference with extra parameters 
conference_id = api.create_conference(from_ = "+12018994444", callback_url = "http://google.com",
                                      callback_timeout= 2000, fallback_url = "http://yahoo.com")
print(conference_id)
## conf-ixaagbn5wcyskisiy
my_conf = api.get_conference(conference_id)
print(my_conf)
## {   'activeMembers'     : 0,
##     'callbackHttpMethod': 'post',
##     'callbackTimeout'   : 2000,
##     'callbackUrl'       : 'http://google.com',
##     'createdTime'       : '2017-01-26T01:58:59Z',
##     'fallbackUrl'       : 'http://yahoo.com',
##     'from'              : '+12018994444',
##     'hold'              : False,
##     'id'                : 'conf-ixaagbn5wcyskisiy',
##     'mute'              : False,
##     'state'             : 'created'}
