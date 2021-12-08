import speech_recognition as sr
import time
i = 10
while i>0:
    i-=1
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Powiedz komende po angielsku || || Zostało poleceń:", i+1)
        audio = recognizer.listen(source)
    try:
        words = recognizer.recognize_google(audio)
        print(recognizer.recognize_google(audio))
        if "hi" in words:
            print("No siema!")
        elif "how are you" in words:
            print("Świetnie dzięki!")
        elif "goodbye" in words:
            print("Nara ziom!")
        elif "jagoda" in words:
            print("Ładne imię Jagódko")
        elif "go" in words:
            if "left" in words:
                print("Skręcam tylko w prawo lewaku")
            if "right" in words:
                print("jazda w prawo!!")
            if "ahead" in words:
                print("Jedziemy z tym koksem")
        elif "stop" in words:
            print("stoję na Twój rozkaz panie")
    except:
        print("Co? nie słyszałem...:( poczekaj sek")
        time.sleep(2)
        continue
        
    time.sleep(1)
