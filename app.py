from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Connected!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    
    msg = request.form.get('Body')      #get the message
    phone_no = request.form.get('From')    #get phone number

    reply = fetch_reply(msg, phone_no)      #setting input for fetch reply in utils

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
