def get_story():
    list_stories = []
    f = open("stories.txt", "r")
    for x in f:
        # str_file_contents = f.readline()
        # str_file_contents = str_file_contents.replace('[', '')
        list_stories.append(x.replace('\n', ''))
    return (list_stories)