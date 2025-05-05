import speech_recognition as sr
import csv

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def save_to_csv(data, filename="data_entries.csv"):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    print("Welcome to the Speech Data Entry System!")
    while True:
        print("\nEnter a new record (say 'stop' to end):")
        entry = recognize_speech()
        if entry:
            if entry.lower() == 'stop':
                break
            save_to_csv([entry])
            print("Entry saved.")
        else:
            print("No data recorded.")

    print("Exiting system.")

if _name_ == "_main_":
    main()
