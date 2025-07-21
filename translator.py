from googletrans import Translator


def translate_nepali_to_english(text):
    """
    Translate Nepali text to English using Google Translate.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Input must be a non-empty string.")

    translator = Translator()
    result = translator.translate(text, src='ne', dest='en')
    return result.text
