import sqlite3
from flask import Flask, render_template, request, jsonify
from scansion_detailed import ScansionDetailed
from meters import Meters

app = Flask(__name__)

import os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aruuz.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meters', methods=['GET'])
def get_meters():
    seen = set()
    meter_list = []
    for name, meter in zip(Meters.meter_names, Meters.meters):
        if name in seen: continue
        seen.add(name)
        feet_chunks = meter.split('/')
        feet_names = []
        for c in feet_chunks:
            clean_c = c.replace('+', '')
            if clean_c in Meters.feet:
                feet_names.append(Meters.feet_names[Meters.feet.index(clean_c)])
        meter_list.append({
            "name": name,
            "feet": " ".join(feet_names)
        })
    return jsonify(meter_list)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json or {}
    text = data.get('text', '')
    selected_meter = data.get('meter', None)
    mode = data.get('mode', 'ghazal')
    
    if not text.strip():
        return jsonify({'error': 'براہ کرم کچھ کلام درج کریں۔'}), 400
    
    db = get_db()
    scanner = ScansionDetailed(db)
    
    try:
        detailed_results = scanner.scan_poem_detailed(text, selected_meter=selected_meter, mode=mode)
    except Exception as e:
        db.close()
        return jsonify({'error': str(e)}), 500
        
    db.close()
    return jsonify(detailed_results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
