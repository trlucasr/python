from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9b08e27e1096bd526bcd168606c6fc07"
# Your Auth Token from twilio.com/console
auth_token  = "8d0a987efbeb4acfaa7351ee9f31cb22"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15005550006", 
    from_="+5511993816793",
    body="Olá, Jojo. Este é um Bot automático Python")

print(message.sid)