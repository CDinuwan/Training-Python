from twilio.rest import TwilioRestClient
from credentials import account_sid,auth_token,my_sell,my_twillio

client=TwilioRestClient(account_sid,auth_token)

my_msg="".join["silly person\n" for i in range(100)]
message=client.messages.create(to=my_sell,from_=my_twillio,body=my_msg)