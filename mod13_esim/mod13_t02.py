from flask import Flask, jsonify
import json
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(port=3306, host="localhost",
                                         database="flight_game",
                                         user="",
                                         password="",
                                         autocommit=True,
                                         use_pure=True
                                         )
@app.route("/kentta/<code>")

def get_country_name_by_code(code):
    cursor = connection.cursor(dictionary=True)
    sql = 'SELECT gps_code as "code", name AS "Name", municipality as "Municipality" FROM airport WHERE gps_code = %s'
    cursor.execute(sql, (code,))
    result = cursor.fetchone()

    if result:
        return jsonify(result)
    else:
        return jsonify(f"Lentokenttää ei löydy {code} koodilla")


#käynnistää serverin joten alimmaisena ja kerran
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
