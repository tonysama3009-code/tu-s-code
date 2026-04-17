from flask import Flask, jsonify
import json

app = Flask(__name__)

# --- Task 4: Airport Lookup ---
@app.route('/airport/<code>')
def airport(code):
    # Convert code to uppercase to match the JSON keys
    icao_code = code.upper()
    try:
        with open('airports.json', 'r') as f:
            data = json.load(f)
            
            if icao_code not in data:
                # Requirement: Return 404 error in JSON format
                return jsonify({"error": "Airport not found"}), 404
            
            # Requirement: Return specific JSON format
            store_code = {
                "icao": icao_code,
                "name": data[icao_code]['name'],
                "city": data[icao_code]['city'],
                "country": data[icao_code]['country']
            }
            return jsonify(store_code)
    except FileNotFoundError:
        return jsonify({"error": "Database file not found"}), 500

# --- Task 3: Prime Number Service ---
@app.route('/prime_number/<number>')
def prime_number(number):
    try:
        # Convert to int for calculation
        num = int(float(number))
        
        # Logic to check prime
        if num < 2:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
        
        # Requirement: Return JSON format {"Number": 31, "isPrime": true}
        return jsonify({
            "Number": num,
            "isPrime": is_prime
        })
    except ValueError:
        return jsonify({"error": "Invalid number provided"}), 400

# --- Server Configuration ---
if __name__ == '__main__':
    # Combined your two run statements into one
    app.run(host='127.0.0.1', port=5000, debug=True)