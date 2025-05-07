import speech_recognition as sr
from textblob import TextBlob
import datetime
import os

def transcribe_and_correct():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Start speaking...")
        audio = recognizer.listen(source)

    try:
        raw_text = recognizer.recognize_google(audio)
        print("Original Transcript:", raw_text)

        corrected = str(TextBlob(raw_text).correct())
        print("Corrected Transcript:", corrected)

        # Create output folder
        os.makedirs("corrected_transcripts", exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"corrected_transcripts/transcript_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write("Original: " + raw_text + "\n")
            f.write("Corrected: " + corrected)

        print(f"✅ Transcript saved to {filename}")

    except sr.UnknownValueError:
        print("❌ Could not understand the audio")
    except sr.RequestError as e:
        print("❌ API error:", e)

if __name__ == "__main__":
    transcribe_and_correct()
