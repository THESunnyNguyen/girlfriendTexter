import openai
import spacy
import os

spacys={}

def set_spacys():
    global spacys
    if os.environ.get('FLASK_ENVIRONMENT') == 'local':
        print("DOING LOCAL STUFF")
        spacys = {
            'fr': "fr_core_news_sm"
        }
    else:
        spacys = {
            'en': "en_core_web_sm",
            'fr': "fr_core_news_sm",
            'es': "es_core_news_sm",
            'ja': "ja_core_news_sm",
            'zh': "zh_core_web_sm",
            'de': "de_core_news_sm",
            'nl': "nl_core_news_sm",
            'it': "it_core_news_sm",
            'pt': "pt_core_news_sm",
            'ko': "ko_core_news_sm",
            'el': "el_core_news_sm",
            'fi': "fi_core_news_sm",
            'ru': "ru_core_news_sm",
            'uk': "uk_core_news_sm"
        }


def get_chat_message(messages):
    openai.api_key = '**************************************'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    message = response["choices"][0]["message"]
    return message


def get_style_message(level):
  if not level or level==0:
    return "Talk to me in a way that a beginner in the language would understand."
  if level==1:
    return "Talk to me in a way that an upper-beginner language learner would understand."
  if level==2:
    return "Talk to me in a way that a lower-intermediate language learner would understand."
  if level==3:
    return "Talk to me in a way that an upper-intermediate language learner would understand."
  if level==4:
    return "Talk to me in a way that an advanced language learner would understand."
  if level==5:
    return "Talk to me in a way that a native would understand."
  return "Talk to me in a way that a beginner in the language would understand."


def get_language(id):
    languages = {
        'en': "English",
        'fr': "French",
        'es': "Spanish",
        'ja': "Japanese",
        'zh': "Mandarin",
        'de': "German",
        'nl': "Dutch",
        'it': "Italian",
        'pt': "Portugese",
        'ko': "Korean",
        'el': "Greek",
        'fi': "Finnish",
        'ru': "Russian",
        'uk': "Ukranian"
    }
    return languages[id]

def get_tesseract_language(id):
    languages = {
        'en': "eng",
        'fr': "fra",
        'es': "spa",
        'ja': "jpn",
        'zh': "chi_sim",
        'de': "deu",
        'nl': "nld",
        'it': "ita",
        'pt': "por",
        'ko': "kor",
        'el': "grc",
        'fi': "fin",
        'ru': "rus",
        'uk': "ukr"
    }
    return languages[id]


def lemmatize(sentence, id):
    if id not in spacys:
        raise Exception(f"Language ID {id} not valid")
    nlp_id = spacys[id]

    nlp = spacy.load(nlp_id)

    try:
        doc = nlp(sentence)
        return doc
    except Exception as e:
        raise Exception(f"Something went wrong when lemmatizing")
