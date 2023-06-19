import pywhatkit


def text_to_handwriting(text):
    try:
        pywhatkit.text_to_handwriting(text, rgb=(0, 0, 0))
        print("Text converted to handwriting successfully! ")
    except Exception as e:
        print("Error occurred: ", str(e))


def send_to_whatsapp(number, message):
    try:
        pywhatkit.sendwhatmsg_instantly(number, message)
        print("Message sent to whatsApp contact successfully! ")
    except Exception as e:
        print("Error occurred: ", str(e))


def youtube_play(yt_search):
    try:
        pywhatkit.playonyt(yt_search)
        print("Youtube video playing ...")
    except Exception as e:
        print("Error occurred: ", str(e))


def google_search(g_search):
    try:
        pywhatkit.search(g_search)
        print("Searching on Google ...")
    except Exception as e:
        print("Error occurred: ", str(e))