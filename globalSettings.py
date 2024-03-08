def text_formatter(text):
    text = ' '.join([x for x in text.split(' ') if x != '']).capitalize()
    return text