# Dependencies
from flask import Flask, render_template, request, redirect, url_for, session
import components.riotAPI
from authlib.integrations.flask_client import OAuth

# Setup
app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = 'PERI-KEYSCOPE10'

# Github OAuth config
oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id='Ov23li1wFmJXgVWxcixw',
    client_secret='5595aa46aa861bc66f209b3e8fc484d84c43c3b8',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

# Setting up the main page
@app.route('/', methods=('GET', 'POST'))
def index():
    user = session.get('user')
    if user:
        print(user)

    # If there is content to be added, this code is executed instead
    if request.method == "POST":
        # Naive list
        #SummonerInfo=[]
        # Retrieve user inputs
        # User name and tagline
        name = request.form.get('player')
        # Region

        # Riot API Function, returns a pre-processed list
        #SummonerName, SummonerLevel, SummonerIconURL = components.riotAPI.printSummonerV2(name)
        SummonerInfo = components.riotAPI.printSummonerV2(name)
        MatchInfo = components.riotAPI.printMatch(name)
        RankInfo = components.riotAPI.printPlayerRank(name)

        # WIP
        #components.riotAPI.printMatchStatistics(name)

        # Add to main info (naive implementation)
        #SummonerInfo.append(SummonerName)
        #SummonerInfo.append(SummonerLevel)
        #SummonerInfo.append(SummonerIconURL)
        
        # Return HTML with updated values
        return render_template('index.html', SummonerInfo=SummonerInfo, MatchInfo=MatchInfo, RankInfo=RankInfo)
    
    return render_template('index.html')

# Login 
# Landing page
@app.route('/login_landing')
def login_landing():
    return render_template('login.html')

@app.route('/login')
def login():
    # Replace with a landing page later
    #return render_template('login.html')
    return github.authorize_redirect(url_for('authorize', _external=True))

@app.route('/authorize')
def authorize():
     # Fetch the access token
    token = github.authorize_access_token()
    # Fetch user information from GitHub
    user = github.get('user').json()
    session['user'] = user  # Store user info in session
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# Initiate login
@app.route('/login_success')
def login_success():
    ...


# Misc pages go here


# Run the app
if __name__ == '__main__':
    app.run(debug=True)