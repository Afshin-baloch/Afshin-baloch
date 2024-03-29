from twilio.rest import Client

# مشخصات حساب Twilio خود را در این قسمت وارد کنید
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# شماره تلفن هدف را در این قسمت وارد کنید
target_phone_number = '+1234567890'

# ایجاد یک نمونه از کلاس Client با استفاده از مشخصات حساب Twilio
client = Client(account_sid, auth_token)

# ارسال پیامک با استفاده از شماره تلفن شما به شماره تلفن هدف
message = client.messages.create(
    body='Hello, World!',
    from_='YOUR_TWILIO_PHONE_NUMBER',
    to=target_phone_number
)

print(message.sid)