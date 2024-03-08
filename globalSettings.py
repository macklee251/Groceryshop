from dal import CategoriaDal
def text_formatter(text):
    try:
        text = ' '.join([x for x in text.split(' ') if x != '']).capitalize()
        return text
    except:
        return text

def checking_duplicity(name, description):
    try:
        for category in CategoriaDal.read():
            if category.name == name and category.description == description:
                return True
        return False
    except:
        pass