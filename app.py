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


def get_story():
    f = open("stories.txt", "r")
    stories_from_file=[]
    for x in f:
        # another_story = None
        # stories_from_file = []
        list_stories = []
        arr_stories = ''
        temp_prompt = ''
        prompt =[]
        template = ''
        list_stories.append(x.replace('\n', ''))
        arr_stories = list_stories[0].split('],')
        temp_prompt = arr_stories[0].split(',')
        for temps in temp_prompt:
            prompt.append(str(temps).replace('[',''))
        template = arr_stories[1]
        another_story = Story(prompt, template)
        stories_from_file.append(another_story)
        # print(prompt)
    return (stories_from_file)
# Here's a story to get you started

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
s = Story(["noun", "verb"], "I love to {verb} a good {noun}.")
t = Story(["noun", "clothing"], "I walk around my {noun} in my {clothing}.")

stories = get_story()
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
    new_obj = request.args
    # return new_obj
    return render_template('buildMadlibs.html', what=new_obj, story=stories[int(request.args['storyID'])])

@app.route('/createStory')
def create_madlib():
    return render_template('createMadlibs.html')

@app.route('/createMadlib', methods=["POST"])
def create_new_madlib():
    comment = request.form["txtArea"]
    words = request.form["txtWords"]
    new_story = Story(words,comment)
    
    x = open('stories.txt', 'a')
    x.write( f"[{words}], {comment}\n")
    x.close()
    return render_template('addMadlib.html', ml=comment, words=words, new_story=new_story)
