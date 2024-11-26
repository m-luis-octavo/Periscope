# Dependencies
from flask import Flask, render_template, request, redirect, url_for
import components.riotAPI

# Setup
app = Flask(__name__)
app.static_folder = 'static'

# Naive search history
# history = ['nah']

# Setting up the main page
@app.route('/', methods=('GET', 'POST'))
def index(SummonerNameList=[]):

    # If there is content to be added, this code is executed instead
    if request.method == "POST":
        # Retrieve user inputs
        # User name and tagline
        name = request.form.get('player')
        # Region
        SummonerName = components.riotAPI.printSummonerV2(name)
        # Add to history
        SummonerNameList.append(SummonerName)

        # Return HTML with updated values
        return render_template('index.html', SummonerNameList=SummonerName)

    return render_template('index.html')

# Login 
# Landing page
@app.route('/login')
def login():
    return render_template('login.html')

# Initiate login
@app.route('/login_success')
def login_success():
    ...


# Misc pages go here


# Run the app
if __name__ == '__main__':
    app.run(debug=True)