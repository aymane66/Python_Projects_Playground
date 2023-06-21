from deep_translator import GoogleTranslator


def translate_text():
    try:
        print("----------- English to German Translator -----------")
        text = input("Enter the text you want to translate: ")

        translator = GoogleTranslator(source='en', target='de')
        translation = translator.translate(text)

        print("Translation:")
        print(translation)
    except Exception as e:
        print("An error occurred while translating:", str(e))


translate_text()
