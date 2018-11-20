# Example: List bridges 1000 at a time 
bridges = api.list_bridges(size=1000)
for bridge in bridges:
    print(bridge["id"])
## brg-6mv7pi22i
## brg-3emq7olua
## brg-bbufdc7yq
## brg-dvpvd7cuy
## brg-5ws2buzmq
