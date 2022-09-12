from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'

debug = DebugToolbarExtension(app)

"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""
        self.prompts = words
        self.template = text
        

    def generate(self, answers):
        """Substitute answers into text."""
        text = self.template
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
s = Story(["noun", "verb"], "I love to {verb} a good {noun}.")
t = Story(["noun", "clothing"], "I walk around my {noun} in my {clothing}.")
stories = [s,t,story]
pick_a_story = choice(stories)
str_temp = (pick_a_story.template)
obj_new = []
for madlib in stories:
    obj_new.append(str(madlib.template)[:10])
    
@app.route('/')
def go_home():
    if request.args:
        str_story = request.args.get('storyID') 
        ans = (stories[int(str_story)].prompts)
        return render_template('madlibs.html', ans=ans)
    return render_template('madlibs.html', stories=obj_new)


@app.route('/buildMadlibs')
def go_madlibs():
    new_obj = {}
    for req in request.args:
        new_obj[req] = request.args[req]
    # return new_obj
    return render_template('buildMadlibs.html', what=new_obj, story=stories[int(request.args['storyID'])])

@app.route('/createStory')
def create_madlib():
    return render_template('createMadlibs.html')