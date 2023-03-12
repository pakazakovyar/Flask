from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {"firstname": "Bobbi", "surname": "Bobston"}
    friends = [
        {
            'firstname': 'Shauludin', 'surname': "Chigiryaev"
        },
        {
            'firstname': 'Sahka', 'surname': "Mirniy"
        },
        {
            'firstname': 'Anton', 'surname': "Bravl"
        }]
    #print(url_for('index'))
    return render_template('index.html',title = "Моя страница", user = user, friends = friends)


@app.route('/gg')
def gg():
   # print(url_for('gg'))
    return 'gg bro'

if __name__ == '__main__':
    app.run(debug = True)