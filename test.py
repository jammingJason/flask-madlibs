class Story:
 
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
        print(prompt)
    return (stories_from_file)