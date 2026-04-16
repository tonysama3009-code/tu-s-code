from flask import Flask, jsonify

app = Flask(__name__)

# Task 3: Prime Number Logic
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

@app.route('/prime_number/<int:number>')
def check_prime(number):
    return jsonify({
        "Number": number, 
        "isPrime": is_prime(number)
    })

# Task 4: Airport Logic (Mock database for example)
@app.route('/airport/<icao>')
def get_airport(icao):
    # This is where you'd normally query your SQL database
    # For now, here is a logic check for the required JSON 404
    airports = {
        "LFLL": {"name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
        "EFHK": {"name": "Helsinki-Vantaa Airport", "city": "Helsinki", "country": "FI"}
    }
    
    code = icao.upper()
    if code in airports:
        return jsonify({
            "icao": code,
            "name": airports[code]["name"],
            "city": airports[code]["city"],
            "country": airports[code]["country"]
        })
    else:
        # Task 4 Requirement: Return 404 in JSON format
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(port=5000)