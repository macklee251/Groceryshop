from dal import CategoriaDal
def text_formatter(text):
    text = ' '.join([x for x in text.split(' ') if x != '']).capitalize()
    return text

def checking_duplicity(name, description):
    try:
        for element in CategoriaDal.read():
            if element.name == name and element.description == description :
                return True
            else:
                return False
    except:
        pass
            