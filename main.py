# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request, url_for
import pymongo
from werkzeug.utils import redirect

orderapp = Flask('__name__')


@orderapp.route('/insertdata', methods=['POST', 'GET'])
def insert_db():
    name = request.form['custname']
    phno = request.form['custphn']
    item = request.form['item']
    quantity = request.form['quantity']
    '''name = "ishu"
    phno = 9789100224
    item = "cupcake"
    quantity = 1 '''
    # cost = redirect(url_for('calculatecost', item=item, quantity=quantity))
    cost = calculatecost(item, quantity)
    result = f'Total price of the order is {cost}'

    # connecting to mongodeb
    cloudclient = pymongo.MongoClient(
        r"mongodb+srv://ishwarya:ishusonu@cluster0.riei5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    myclouddb = cloudclient.MyDB
    bakecakecollection = myclouddb.bakecakeDB
    order = {
        'Customer Name': name,
        'Phone Number': phno,
        'Order Item': item,
        'quantity': quantity,
        'Total Amount': cost
    }
    try:
        bakecakecollection.insert_one(order)
        return "Order Placed successfully %s" % result
    except Exception as e:
        return "Problem in placing order. Try after some time.. %s" % e

    # @orderapp.route('/<item>/<quantity>')


def calculatecost(item, quantity):
    if item == 'cupcake':
        costperpiece = 10
        res = str(costperpiece * int(quantity))
        return res
    elif item == 'macrons':
        costperpiece = 40
        res = str(costperpiece * int(quantity))
        return res
    elif item == 'cakeslice':
        costperpiece = 30
        res = str(costperpiece * int(quantity))
        return res
    elif item == 'donut':
        costperpiece = 35
        res = str(costperpiece * int(quantity))
        return res


@orderapp.route('/bakecake', methods=['POST', 'GET'])
def renderoderpage():
    return render_template('index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    orderapp.run()
