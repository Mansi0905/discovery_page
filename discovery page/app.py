from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        skills = request.form['skills']
        interests = request.form['interests']
        work_pref = request.form['work_pref']

        # Print in console to verify
        print(f"Name: {name}")
        print(f"Skills: {skills}")
        print(f"Interests: {interests}")
        print(f"Work Preference: {work_pref}")

        return f"<h2>Thank you, {name}! Your form has been submitted.</h2>"

    except Exception as e:
        return f"<h2>Error: {str(e)}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
