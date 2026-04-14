from flask import Flask, render_template, request, jsonify
from repository.payment_repository import process_payment

app = Flask(__name__)

@app.route('/payment', methods=['GET', 'POST'])
def payment():

    # If request comes from Postman (JSON)
    if request.is_json:
        data = request.get_json()

        user_id = data.get("user_id")
        merchant_id = data.get("merchant_id")
        amount = data.get("amount")

        message = process_payment(user_id, merchant_id, amount)

        return jsonify({"message": message})

    # If request comes from HTML form
    message = ""

    if request.method == 'POST':

        user_id = request.form.get('user_id')
        merchant_id = request.form.get('merchant_id')
        amount = request.form.get('amount')

        if user_id and merchant_id and amount:
            user_id = int(user_id)
            merchant_id = int(merchant_id)
            amount = float(amount)

            message = process_payment(user_id, merchant_id, amount)
        else:
            message = "Please fill all fields"

    return render_template('payment.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)