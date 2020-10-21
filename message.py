
from twilio.rest import Client 
 
account_sid = 'AC353d933e060e00f95c1d5ac35b165538' 
auth_token = '1d9dec1f62d7c5ed0c6d116b9ceac9af' 
client = Client(account_sid, auth_token) 
def send_message():
    message = client.messages.create(
                               from_='whatsapp:+14155238886',  
                               body='You got this one life! Make the most out it. Stay Agile!',      
                               to='whatsapp:+918433754458' 
                           )
 
    print(message.sid)