from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """generate to questions form with word prompts"""
    
    prompts = silly_story.prompts

    return render_template('questions.html', prompts=prompts)


@app.route('/results')
def results():
    """Displays results as text story from story instance 
    from the homepage form"""

    story = silly_story.generate(request.args)
    return render_template('story.html', story=story)


