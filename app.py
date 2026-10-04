import sqlite3
from flask import Flask, render_template, request, jsonify
from scansion_detailed import ScansionDetailed

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('aruuz.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    db = get_db()
    scanner = ScansionDetailed(db)
    
    try:
        detailed_results = scanner.scan_poem_detailed(text)
    except Exception as e:
        db.close()
        return jsonify({'error': str(e)}), 500
        
    db.close()
    return jsonify(detailed_results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
