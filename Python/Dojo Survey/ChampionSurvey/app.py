from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    email = request.form.get('email')
    favorite_champion = request.form.get('favorite_champion')
    survey_answers = request.form.getlist('survey_answers')
    radio_choice = request.form.get('radio_choice')

    return render_template('result.html', name=name, email=email, favorite_champion=favorite_champion, survey_answers=survey_answers, radio_choice=radio_choice)

if __name__ == '__main__':
    app.run(debug=True)