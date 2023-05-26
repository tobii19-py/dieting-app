from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calories import Calorie
from temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        pass


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ", default=175)
    age = StringField("Age: ", default=32)
    temperature = StringField("Temperature: ", default=75)
    city = StringField("City: ", default="dallas")
    country = StringField("Country: ", default="usa")

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form_page', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)