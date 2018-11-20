# Example: Fetch all calls that were in a bridge 
call_list = api.get_bridge_calls('bridgeId')
print(list(call_list))
## [
##     {
##         "activeTime"      : "2013-05-22T19:49:39Z",
##         "direction"       : "out",
##         "from"            : "{fromNumber}",
##         "id"              : "{callId1}",
##         "bridgeId"        : "{bridgeId}",
##         "startTime"       : "2013-05-22T19:49:35Z",
##         "state"           : "active",
##         "to"              : "{toNumber1}",
##         "recordingEnabled": false,
##         "events"          : "https://api.catapult.inetwork.com/v1/users/{userId}/calls/{callId1}/events",
##         "bridge"          : "https://api.catapult.inetwork.com/v1/users/{userId}/bridges/{bridgeId}"
##     },
##     {
##         "activeTime"      : "2013-05-22T19:50:16Z",
##         "direction"       : "out",
##         "from"            : "{fromNumber}",
##         "id"              : "{callId2}",
##         "bridgeId"        : "{bridgeId}",
##         "startTime"       : "2013-05-22T19:50:16Z",
##         "state"           : "active",
##         "to"              : "{toNumber2}",
##         "recordingEnabled": false,
##         "events"          : "https://api.catapult.inetwork.com/v1/users/{userId}/calls/{callId2}/events",
##         "bridge"          : "https://api.catapult.inetwork.com/v1/users/{userId}/bridges/{bridgeId}"
##     }
## ]
