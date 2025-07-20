from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Read from JSON file
def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except Exception:
        return []

# Read from CSV file
def read_csv():
    products = []
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception:
        pass
    return products

# Read from SQLite database
def read_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Enable dictionary-like row access
        cursor = conn.cursor()

        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")

        rows = cursor.fetchall()
        products = [{
            'id': row['id'],
            'name': row['name'],
            'category': row['category'],
            'price': row['price']
        } for row in rows]

        conn.close()
        return products
    except sqlite3.Error:
        return None  # Return None on error

# Route to display products
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    data = []
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql(product_id)
        if data is None:
            error = "Database error"
    else:
        error = "Wrong source"

    # Filter by ID if not using SQL and ID is provided
    if product_id and source in ['json', 'csv']:
        data = [item for item in data if item.get('id') == product_id]
        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
