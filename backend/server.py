from flask import Flask, request, jsonify
import products
from connector import get_sql_connection
import json

#import orders
import uom

app= Flask(__name__)


connection= get_sql_connection()


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def getProducts():
    products_data = products.get_all_products(connection)
    response = jsonify(products_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products.insert_product_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/getAllOrders', methods=['GET'])
# def get_all_orders():
#     response = orders.get_all_orders(connection)
#     response = jsonify(response)
#     response.headers.add('access-control-allow-Origine', '*')
#     return response
#
#
#
# @app.route('/insertOrder', methods=['POST'])
# def insert_order():
#     request_payload = json.loads(request.form['data'])
#     order_id = orders_dao.insert_order(connection, request_payload)
#     response = jsonify({
#         'order_id': order_id
#     })
#     response.headers.add('access-control-allow-Origine', '*')
#     return response



@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('access-control-allow-Origin', '*')
    return response




if __name__=='__main__':
    print('Start python Flask Server')
    app.run(port=5000)