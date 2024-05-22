from datetime import datetime
from connector import get_sql_connection

def insert_order(connection, order):
    cursor=connection.cursor()
    query=( 'INSERT INTO orders' '(customer_name, total, datetime)' 'VALUES(%s, %s,%s)')
    data = (order['customer_name'], order['grand_total'], datetime.now())
    cursor.execute(query, data)
    order_id= cursor.lastrowid()
    connection.commit()
    return order_id



if __name__=='__main__':
    connection=get_sql_connection()
    print(insert_order(connection,{
           'customer_name': 'Aicha',
           'grand_total': 500,
           "datetime":datetime.now,
           'order_details':[
           {
                'product_id': 1,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 3,
                'quantity': 1,
                'total_price': 30
            }
        ]}

    ))