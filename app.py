from flask import Flask, render_template, request, flash, session, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes 

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"

c = CurrencyRates()
c_code = CurrencyCodes()

@app.route("/")
def show_converter():
    """display currency converter"""
    return render_template("forex.html")

@app.route("/convert", methods=["POST"])
def convert():
    """convert one currency to the next using form data"""
    
    from_currency = request.form["from_currency"].upper()
    to_currency = request.form["to_currency"].upper()
    amount = request.form.get("amount")

    session.update({
        "from_currency" : from_currency,
        "to_currency" : to_currency,
        "from_currency_code" : c_code.get_symbol(from_currency),
        "to_currency_code" : c_code.get_symbol(to_currency),
        "from_currency_name" : c_code.get_currency_name(from_currency),
        "to_currency_name" : c_code.get_currency_name(to_currency),
    })

    if not session["from_currency_name"]:
        flash(f"Not a valid code: {from_currency}")

    if not session["to_currency_name"]:
        flash(f"Not a valid code: {to_currency}")
    
    if amount is not None:
        try:
            session["amount"] = float(amount)
        except ValueError:
            flash("Invalid amount")
            
    if any(not session[key] for key in ("from_currency_name", "to_currency_name")) or "amount" not in session:
        return render_template("forex.html")
    else:
        session["converted_amount"] = c.convert(from_currency, to_currency, session["amount"])
        return redirect("/conversion")


@app.route("/conversion")
def show_conversion():
    """show final conversion"""

    result = f"{session.get('from_currency_code')}{session.get('amount'):.2f} {session.get('from_currency')} is equal to {session.get('to_currency_code')}{session.get('converted_amount'):.2f} {session.get('to_currency')}."

    return render_template("converted.html", result = result)
