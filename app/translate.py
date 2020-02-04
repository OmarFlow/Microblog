import requests

from flask_babel import _
from flask import current_app


def translate(text, source_lang, dest_lang):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YA_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    payload = {
        'key': current_app.config['YA_TRANSLATOR_KEY'],
        'text': text,
        'lang': f'{source_lang}-{dest_lang}'
    }

    print(source_lang)
    print(dest_lang)

    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',
                     params=payload)

    if r.status_code != 200:
        return _('Error: the translation service failed.')

    result = r.json()['text'][0]

    return result
