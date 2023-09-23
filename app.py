from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch results for a polling unit by unique ID
def get_polling_unit_results(polling_unit_id):
    conn = sqlite3.connect(' bincom_test.sql')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = ?", (polling_unit_id,))
    results = cursor.fetchall()

    conn.close()
    return results

@app.route('/', methods=['GET', 'POST'])
def display_polling_unit_results():
    if request.method == 'POST':
        polling_unit_id = request.form['polling_unit_id']
        results = get_polling_unit_results(polling_unit_id)
        return render_template('results.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
