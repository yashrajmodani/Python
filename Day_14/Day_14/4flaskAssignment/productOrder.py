
from flask import Flask, render_template,request,url_for,session,redirect

order = Flask(__name__)
print(order)

order.secret_key = 'secret'

@order.route("/", methods=['Get', 'POST'])
def homepage():
    if request.method == 'POST':
        product = request.form['pname']
        quantity = request.form['quantity']
        session['product'] = product
        session['quantity'] = quantity
        return redirect(url_for("shippingDetail"))
    return render_template('homepage.html')

@order.route("/shippingDetail", methods=['Get', 'POST'])
def userInfo():
    if request.method == 'POST':
        user_name = request.form['name']
        address = request.form['address']
        mob = request.form['mobile']

        session['name'] = user_name
        session['address'] = address
        session['mob'] = mob
        return redirect(url_for("orderSumm"))

    return render_template('shippingDetail.html')

@order.route("/orderSumm", methods=["GET"])
def orderSumm():
    product = session.get('product')
    quantity = session.get('quantity')
    name = session.get('name')
    address = session.get('address')
    mob = session.get('mob')
    return render_template('orderSumm.html', product=product, quantity=quantity, name1=name, address=address, mobile = mob)




if __name__ == "__main__":
    order.run(debug=True, port=5010)
