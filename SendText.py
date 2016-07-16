from twilio.rest import TwilioRestClient

account_sid = "ACe35b7777d7e53a423fb7e843d8bd9b43"
auth_token = "6c8f058a0318efa1113197f82f7ddcb9"
client = TwilioRestClient(account_sid,auth_token)
message = client.sms.messages.create(body="I Love You :) ",to="+13608184000",from_="+13022890383")
print message.sid
