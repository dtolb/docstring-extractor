# Example: Fetch calls from specific telephone number 
call_list = api.list_calls(from_ = '+19192223333', size = 1000)
total_chargeable_duration = 0
for call in call_list:
    total_chargeable_duration += call['chargeableDuration']
print(total_chargeable_duration)
## 240
