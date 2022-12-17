from flask import Flask, jsonify, make_response
from markupsafe import escape
import instaloader
import os

# Check if env variables are present
envVars = ['INSTAGRAM_USER', 'INSTAGRAM_PASSWORD']
for envVar in envVars:
    if not os.environ.get(envVar):
        print('Environment variable ' + envVar + ' not found. Exiting...')
        exit()
# Define port
PORT = os.environ.get('PORT', 3001)

# Create Flask app
app = Flask(__name__)

###################
###     API     ###
###################

# Get the stories info of a profile with authentication
@app.route('/api/igstories/username/<string:username>')
def get_stories(username):
    """
    Get the stories info with authentication, and return them

    Args:
        username: Instagram profile name to get the stories from
    Returns:
        stories: Stories info
    Raises:
        None
    """

    # Define the session file path
    sessionFilePath = './session'
    # Get Instaloader instance
    try:
        L = instaloader.Instaloader()
    except:
        return make_response('Cannot get Instaloader instance', 500)
    # Login
    try:
        # Try to load session from file
        L.load_session_from_file(os.environ.get('INSTAGRAM_USER'), filename=sessionFilePath)
    except:
        # Login if session is not available and save session to file
        try:
            L.login(os.environ.get('INSTAGRAM_USER'), os.environ.get('INSTAGRAM_PASSWORD'))
            L.save_session_to_file(filename=sessionFilePath)
        except:
            return make_response('Cannot login to Instagram', 500)
    # Get the profile info
    try:
        profile = instaloader.Profile.from_username(L.context, escape(username))
    except:
        return make_response('Cannot get profile info', 500)
    # Get the stories info
    try:
        rawStories = L.get_stories(userids=[profile.userid])
    except:
        return make_response('Cannot get stories info', 500)
    stories = []
    for story in rawStories:
        # Iterate over stories and store them in 'stories' list
        for item in story.get_items():
            stories.append(instaloader.get_json_structure(item))
    # Return the stories info
    return make_response(jsonify(stories), 200)

# Remove the session file
@app.route('/api/igstories/remove-session')
def remove_session():
    """
    Remove the session file

    Args:
        None
    Returns:
        None
    Raises:
        None
    """

    # Define the session file path
    sessionFilePath = './session'
    # Remove the session file
    try:
        os.remove(sessionFilePath)
        return make_response(jsonify('Session file removed'), 200)
    except:
        return make_response('Cannot remove session file', 500)

# Living check
@app.route('/api/igstories/living')
def living():
    return make_response(jsonify('I am alive'), 200)

# Readyness check
@app.route('/api/igstories/ready')
def ready():
    return make_response(jsonify('I am ready'), 200)

# Activate the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)