from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

#client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')

# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name = request.form['name_order']
    quan = request.form['quan_order']
    addr = request.form['addr_order']
    phone = request.form['phone_order']

    data = {
        'name': name,
        'quan': quan,
        'addr': addr,
        'phone': phone
    }
    db.order.insert_one(data)

    return jsonify({'msg': '주문이 완료되었습니다!'})


# 주문 목록보기(GET) API
@app.route('/order', methods=['GET'])
def view_orders():
    order_data = list(db.order.find({}, {'_id':False}))
    return jsonify({'all_order_data': order_data})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)