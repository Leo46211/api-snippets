# Download the Python helper library from twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

map_permission = client.sync \
    .services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
    .sync_maps("Players") \
    .sync_map_permissions("bob") \
    .update(True, True, False)

print(map_permission.read)  # True
print(map_permission.write)  # True
print(map_permission.manage)  # False
