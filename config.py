import configparser
import json
import sqlite3
import os
from flask import Flask, jsonify

# Function to read and parse the configuration file
def parse_config(file_path):
    config_data = {}
    
    if not os.path.exists(file_path):
        print(f"Error: Configuration file '{file_path}' not found.")
        return None
    
    config = configparser.ConfigParser()
    
    try:
        config.read(file_path)
        for section in config.sections():
            config_data[section] = {key: config[section][key] for key in config[section]}
        return config_data
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return None

# Function to save data to SQLite database
def save_to_database(data, db_path="config_data.db"):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("CREATE TABLE IF NOT EXISTS Config (id INTEGER PRIMARY KEY, data TEXT)")
        
        json_data = json.dumps(data)
        cursor.execute("INSERT INTO Config (data) VALUES (?)", (json_data,))
        
        conn.commit()
        conn.close()
        print("Data saved to database successfully.")
    except Exception as e:
        print(f"Error saving to database: {e}")

# Flask API to provide a GET request endpoint
app = Flask(__name__)

@app.route('/get_config', methods=['GET'])
def get_config():
    try:
        conn = sqlite3.connect("config_data.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT data FROM Config ORDER BY id DESC LIMIT 1")
        row = cursor.fetchone()
        
        conn.close()
        
        if row:
            return jsonify(json.loads(row[0]))
        else:
            return jsonify({"error": "No configuration data found"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    config_file_path = "config.ini"
    
    config_data = parse_config(config_file_path)
    
    if config_data:
        save_to_database(config_data)
    
    print("Starting Flask API...")
    app.run(host="0.0.0.0", port=5000, debug=True)