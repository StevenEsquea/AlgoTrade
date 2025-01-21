import os
import re
import json

from flask import Flask
from flask import render_template, request
from flask import jsonify
import yfinance as yf
#from flask_cors import CORS

from back.strategies.moving_average_crossover import MovingAverageCross

app = Flask(__name__)
#CORS(app)

files = os.listdir("back/strategies")

lang_es = {
    "null_selection" : "Selecciona la estrategia deseada"
}

lang_en = {
    "null_selection" : "Select the strategy"
}

strategy_files = []
for file in files:
    if re.search(".py$", file) != None:
        strategy_files.append(file)

strategies_info = {
    "moving_average_crossover.py":
        {"name": "Moving Average Crossover"}
    }

strategy_names = [lang_en['null_selection']]
for file in strategy_files:
    strategy_names.append(strategies_info[file]["name"])

accepted_periods = {
    "1d": "1 day",
    "5d": "5 days",
    "1mo": "1 month",
    "3mo": "3 months",
    "6mo": "6 months",
    "1y": "1 year",
    "2y": "2 years",
    "5y": "5 years",
    "10y": "10 years",
    "ytd": "Years-to-day",
    "max": "Maximum"
}

accepted_intervals = {
    "1m": "1 minute",
    "2m": "2 minutes",
    "5m": "5 minutes",
    "15m": "15 minutes",
    "30m": "30 minutes",
    "60m": "60 minutes",
    "90m": "90 minutes",
    "1h": "1 hour",
    "1d": "1 day",
    "5d": "5 days",
    "1wk": "1 week",
    "1mo": "1 month",
    "3mo": "3 months"
}

accepted_periods_codes = list(accepted_periods.keys())
accepted_periods_texts = list(accepted_periods.values())
accepted_intervals_codes = list(accepted_intervals.keys())
accepted_intervals_texts = list(accepted_intervals.values())

ticker_data = ""

@app.route("/")
def home():
    return render_template('home.html', strategies_list = strategy_names, accepted_periods = accepted_periods_texts, accepted_intervals = accepted_intervals_texts)

@app.route("/search_ticker_info", methods=["POST"])
def search_ticker_info():
    request_data = request.json
    request_data_dict = json.loads(request_data)
    ticker = request_data_dict["myTickerName"]
    global ticker_data
    ticker_data = yf.Ticker(ticker)

    try:
        ticker_shortName = ticker_data.info["shortName"]
        data = {"informacion" : ticker_shortName}
        return jsonify(data)

    except:
        return "Parece que el ticker ingresado no pertenece a ninguna empresa. Intenta de nuevo con otro."

@app.route("/about")
def about():
    return "Software developed"

@app.route("/run", methods=["POST"])
def run():
    request_data = request.json
    request_data_dict = json.loads(request_data)

#    initial_date = request_data_dict["initial_date"]
#    final_date = request_data_dict["final_date"]
    
    low_period = request_data_dict["myPeriod1"]
    high_period = request_data_dict["myPeriod2"]
    requested_temporality = accepted_periods_codes[accepted_periods_texts.index(request_data_dict["myTemporality"])]
    requested_interval = accepted_intervals_codes[accepted_intervals_texts.index(request_data_dict["myInterval"])]

    simulation = MovingAverageCross(
        int(low_period),
        int(high_period),
        ticker_data.history(
            period = requested_temporality,
            interval = requested_interval)["Close"])

    response_data = simulation.ganancia()
    img = simulation.visualizar()

    response_data["img"] = img

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug="true")