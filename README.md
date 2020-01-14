# GET SMS 
```
pip install getsms
pip install requests
```
# SEND MESSAGE
```
from get_sms import Getsms
message = Getsms(login=login, password=password, nickname=nickname)
phone_numbers = ['998998158172', '998995451872']
results = message.send_message(phone_numbers=phone_number, text='Hello World')

if 'error' in results:
    print(results)

for result in results:
    print(result.phone_number)

# RESPONSE FIELDS
phone_number
text
date_received
message_id
request_id
client_ip
user_id
```

# CHECK STATUS
```
from get_sms import Getsms
message = Getsms(login=login, password=password, nickname=nickname)
request_ids = [1234567, 456789]
results = message.check_status(request_ids)
if 'error' in results:
    print(results)

for result in results:
    print(result.status)

# RESPONSE FIELDS
phone_number
status
text
user_id
date_received
date_sent
date_delivered
message_id
request_id
count_messages
client_ip
description
```