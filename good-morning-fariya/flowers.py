from twilio.rest import Client

account_sid = 'AC94c6d243a67740501d2760740de5fd4a'
auth_token = 'f8cd097efef95d57816798ee3a217e45'
client = Client(account_sid, auth_token)


def good_morning():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Good Morning, Fariya 💞',
        to='whatsapp:+919627692786'
    )
    print(message.sid)
