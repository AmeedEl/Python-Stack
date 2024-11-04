from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/champion')
def champion():
    return 'Champion!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:id>/<string:name>')   # for a route '/users/____/___' , two parameters in the url get passed as username and id
def show_user_profile(id, name):   # only write (users) and if you want to check write a number after (users) e.x "users/8"
    return ("Hello: "+ name )* id


#Bonus
@app.route('/items/<int:id>/<string:name>')
def get_item(id, name):
    return f'ID: {id}, Name: {name}'

#Bonus
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__=="__main__":
    app.run(debug=True)