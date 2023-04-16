from flask import Flask, request, render_template, redirect, jsonify, session
# import requests
# from flask_debugtoolbar import DebugToolbar

from forex_python.converter import CurrencyRates
from convert import Survey
app = Flask(__name__)

app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# survey = Survey()
result=["Give me something to convert!"]

@app.route("/", methods = ['GET', 'POST'])
def home_page():
    """ Shows the form
    #should have inputs for two different currencies
    #should have an input for the amount as well. accepts integer(?)
    """
    return render_template('index.html')


@app.route("/conversion", methods = ['GET', 'POST'])
def show_conversion():
    """shows the users conversion"""
    return render_template('convSubmit.html', result=result)


@app.route("/conversion/new", methods=["POST"])
def add_conversion():
    """clear old conversion from list and add new"""
    result=[]
    survey = Survey(request.form["convertFrom"], request.form["convertTo"], request.form["value"])
    result.append(survey.convertCurrency())
    return redirect("/conversion")


    
    
# responses_key= "responses"

# T= CurrencyRates()

# @app.route("/Index2", methods=["POST"])
# def save_answer():
#     line2 = request.data.get("C1", "C2", int("amt"))
#     responses = session[responses_key]  
#     responses.append(line2)
#     responses = session[responses]

#     rate = T.convert(line2[0],line2[1],int(line2[2]))
#     return rate,render_template("/Index2.html", rate="response") 
    
# @app.route('/results', methods=['POST'])
# def process():
#     conv_from = request.form['conv_from']
#     conv_to = request.form['conv_to']
#     amount = float(request.form['amount'])
    
#     rates = CurrencyRates()
#     codes = CurrencyCodes()
    
#     try:
#         results = round(rates.convert(conv_from, conv_to, amount), 2)
#         symbol = codes.get_symbol(conv_to)
#         return render_template("/results.html", conv_from=conv_from, conv_to=conv_to, amount=amount, results=results, symbol=symbol)
#     except RatesNotAvailableError:
#         flash("Please enter a valid currency")
#         return redirect('/')
#     except (ValueError, TypeError):
#         flash("Oops something went wrong")
#         return redirect('/')
    
#     #or:
    
    
# @app.route('/results', methods=['POST'])
# def process():
#     conv_from = request.form['conv_from']
#     conv_to = request.form['conv_to']
    
#     rates = CurrencyRates()
#     codes = CurrencyCodes()
    
#     try:
#         amount = float(request.form['amount'])
#         results = round(rates.convert(conv_from, conv_to, amount), 2)
#         symbol = codes.get_symbol(conv_to)
#         return render_template("/results.html", conv_from=conv_from, conv_to=conv_to, amount=amount, results=results, symbol=symbol)
#     except RatesNotAvailableError:
#         flash("Please enter a valid currency")
#         return redirect('/')
#     except ValueError:
#         flash("Invalid amount provided!")
#         return redirect('/')
#     except TypeError:
#         flash("Oops something went wrong")
#         return redirect('/')
