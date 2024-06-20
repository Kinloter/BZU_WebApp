from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for the store products
products = [
    {"id": 1, "name": "Product 1", "price": 25.00},
    {"id": 2, "name": "Product 2", "price": 45.00}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/buy/<int:product_id>', methods=['POST'])
def buy(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return f"Bought {product['name']} successfully!"
    else:
        return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
