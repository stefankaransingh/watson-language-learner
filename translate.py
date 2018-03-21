import random
import requests

import email_sender
import load_words

from local import RECEIVER_EMAIL,USERNAME,PASSWORD

URL = "https://gateway.watsonplatform.net/language-translator/api/v2/translate"

LANGUAGE_DICT = {
    'French':'en-fr',
    'Arabic':'en-ar',
    'Spanish':'en-es',
    'Portuguese':'en-pt'
}

LEARN_LANGUAGE = 'Spanish'

WORDS = load_words.get_words()

def translate(text,model_id):
    querystring = {"text":text,
                   "model_id":model_id
                  }
    response = requests.get(URL,auth=(USERNAME, PASSWORD),params=querystring)
    return response.text

if  __name__ == '__main__':

    word_for_the_day = random.choice(WORDS)
    model_id = LANGUAGE_DICT[LEARN_LANGUAGE]
    translated_word = translate(word_for_the_day,model_id)

    message = "The word for the day is {0} and when translated to {1} it's {2}"\
            .format(word_for_the_day,LEARN_LANGUAGE,translated_word)

    subject = "The word for the day is {0} !".format(word_for_the_day)

    email_sender.send_email(RECEIVER_EMAIL,subject,message)
