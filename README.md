# 💱 Currency Chatbot

A currency conversion chatbot built using Dialogflow, Python, Flask, and ExchangeRate-API.

## 🚀 Features

- Convert between multiple currencies
- Understands natural-language currency queries
- Supports currencies such as USD, EUR, INR, GBP, JPY, CAD, AUD, etc.
- Real-time exchange rates using ExchangeRate-API
- Dialogflow handles natural-language understanding
- Flask provides the webhook backend

## 🛠️ Technologies Used

- Python
- Flask
- Dialogflow
- ExchangeRate-API
- REST API
- ngrok
- Git & GitHub

## 🏗️ Architecture

User  
↓  
Dialogflow  
↓  
ngrok  
↓  
Flask Webhook  
↓  
ExchangeRate-API  
↓  
Currency Conversion  
↓  
Dialogflow Response  
↓  
User

## 📁 Project Structure

Currency-Chatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
└── venv/


```bash
git clone https://github.com/YOUR_USERNAME/Currency-Chatbot.git
cd Currency-Chatbot
