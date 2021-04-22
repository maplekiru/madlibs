from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

currentStory = None

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """generate drop down menu or story templates"""

    return render_template('home.html', stories=stories)

@app.route('/story')
def questions():
    """generate questions form with word prompts"""
    
    promptId = request.args.get("stories")

    story = [story for story in stories if story.id == promptId]

    currentStory = stories.index(story[0])

    prompts = story[0].prompts

    return render_template('questions.html', prompts=prompts)


@app.route('/results')
def results():
    """Displays results as text story from story instance 
    from the homepage form"""

    story = stories[currentStory].generate(request.args)
    return render_template('story.html', story=story)


