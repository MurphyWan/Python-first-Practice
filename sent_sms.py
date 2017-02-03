from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "AC51c63d4a83cee616ab70eaecf37f5c81" # Your Account SID from www.twilio.com/console
auth_token  = "af1a68c45673d4f12f494b0baeb83921"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(
        body="Goodnight My lover,from San Francisco",
        to="+8613173659509",    # Replace with your phone number
        from_="+14154171983 ") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
