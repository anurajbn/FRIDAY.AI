import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import openai

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()  # Convert user input to lowercase
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""

def main():
    intro_text = "Allow me to introduce myself. I am Friday, your virtual assistant. I am here to help you with various tasks. The system is now fully operational."
    speak(intro_text)
    import openai
    openai.api_key = "YOUR_OPENAI_API_KEY"

    while True:
        text = takeCommand()

        if "goodbye" in text:
            speak("Goodbye!")
            break
        elif "open youtube" in text:
            print("Friday: Opening YouTube.")
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "open google" in text:
            print("Friday: Opening Google.")
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif "the time" in text:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            response = f"The current time is {current_time}."
            print("Friday:", response)
            speak(response)
        else:
            # Use OpenAI to generate responses for other queries
            ai_response = openai.Completion.create(
                engine="davinci",  # Choose an engine
                prompt=text,
                max_tokens=50
            )
            ai_text = ai_response.choices[0].text.strip()
            print("Friday:", ai_text)
            speak(ai_text)

if __name__ == "__main__":
    main()





