from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Currency Chatbot Webhook is running!"


@app.route("/webhook", methods=["POST"])
def index():
    data = request.get_json()

    # Get parameters from Dialogflow
    source_currency = data["queryResult"]["parameters"]["unit-currency"]["currency"]
    amount = data["queryResult"]["parameters"]["unit-currency"]["amount"]
    target_currency = data["queryResult"]["parameters"]["currency-name"]

    # Get conversion rate
    cf = fetch_conversion_factor(source_currency, target_currency)

    # Calculate converted amount
    final_amount = round(cf * amount, 2)

    # Send response back to Dialogflow
    response = {
        "fulfillmentText": f"{amount} {source_currency} is equal to {final_amount} {target_currency}."
    }

    return jsonify(response)


def fetch_conversion_factor(source_currency, target_currency):

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{source_currency}"

    response = requests.get(url)

    # Convert API response to JSON
    response = response.json()

    # Get conversion rate
    return response["conversion_rates"][target_currency]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    