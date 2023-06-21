from gtts import gTTS

print("--------------- Text to voice converter ---------------")

text = input("Insert text: ")
lang = input("Language (en = English, fr = French): ")

# The program allows only two languages for this exercise
while lang not in ["en", "fr"]:
    print("Invalid input! Please choose one of the two options.")
    lang = input("Language (en = English, fr = French): ")

try:
    result = gTTS(text=text, lang=lang, slow=False)

    rename = input("Name your mp3 file: ")
    while not rename.strip():
        print("Invalid filename! Please enter a valid filename.")
        rename = input("Name your mp3 file: ")

    result.save(rename + ".mp3")
    print("MP3 file saved successfully.")
except Exception as e:
    print("An error occurred:", str(e))
