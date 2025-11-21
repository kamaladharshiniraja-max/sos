from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS
# Initialize Flask app
app = Flask(__name__)  # ✅ Correct syntax
CORS(app)
# ==== TWILIO CREDENTIALS ====
account_sid = "ACc57e89002c62c5837bcd6e80be611f3f"         # Replace with your Twilio Account SID
auth_token = "7cdcadabe154061c456b7b36a4c27009"   # Replace with your Twilio Auth Token
twilio_number = "+15734968807"          # Replace with your Twilio phone number
client = Client(account_sid, auth_token)

# Emergency numbers (Add your personal numbers here)
emergency_numbers = [
    "+918825805313",  # Example: your personal number
    "+918940841517",  # Example: family member
    "+918675827299",
    "+917530013449",
    "+916369861836",
    "+919655765923"  # Example: friend
]

# SOS route
@app.route('/sos', methods=['POST'])
def sos():
    data = request.get_json()
    
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    if not latitude or not longitude:
        return jsonify({"error": "Latitude and Longitude required"}), 400

    # Google Maps link
    map_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    message_body = f"🚨 SOS ALERT!\nLocation: {map_link}"

    # Send SMS to all emergency numbers
    for number in emergency_numbers:
        client.messages.create(
            to=number,
            from_=twilio_number,
            body=message_body
        )

    return jsonify({"message": "SOS Sent Successfully!"})

# Run the app
if __name__ == '__main__':
    app.run(port=5000)