import functions

print("------------------ Tasks Automation ------------------")
print("1- Convert a text to handwriting.")
print("2- Send a message to WhatsApp contact.")
print("3- Play a Youtube video.")
print("4- Search via Google.")
print()


while True:
    order = input("Task to run: ")
    try:
        order = int(order)
        if 1 <= order <= 4:
            print("You selected:", order)
            break
        else:
            print("Invalid input! Please insert a number from 1 to 4")
    except ValueError:
        print("Invalid input! Please insert a numeric value. ")

if order == 1:
    text = input("Insert the text to be converted: ")
    functions.text_to_handwriting(text)

elif order == 2:
    number = input("Phone Number: ")
    message = input("Your Message: ")
    functions.send_to_whatsapp(number, message)
    print("Opening the app ...")

elif order == 3:
    yt_search = input("Search for: ")
    functions.youtube_play(yt_search)
    print("Searching ...")
else:
    g_search = input("Search for: ")
    functions.google_search(g_search)
    print("Searching ... ")
