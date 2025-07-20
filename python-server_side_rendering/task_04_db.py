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
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

# Read from CSV file
def read_csv():
    try:
        data = []
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price and id to appropriate types
                data.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

# Read from SQLite
def read_sql(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        # Convert to list of dicts
        return [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
    except Exception as e:
        print(f"Error reading SQL: {e}")
        return None  # Signals a DB error

# Route for displaying products
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
        elif product_id and not data:
            error = "Product not found"
    else:
        error = "Wrong source"

    if source in ['json', 'csv'] and not error:
        if product_id:
            data = [item for item in data if item.get('id') == product_id]
            if not data:
                error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
