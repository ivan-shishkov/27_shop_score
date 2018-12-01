from flask import Flask, render_template, jsonify

from shop_score import get_orders_processing_info

app = Flask(__name__)


@app.route('/orders-processing-info')
def orders_processing_info():
    return jsonify(orders_processing_info=get_orders_processing_info())


@app.route('/')
def score():
    return render_template('score.html')


if __name__ == "__main__":
    app.run()
