import speech_recognition as sr

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Candidado(a) disse: {query}\n")
        return query

    except Exception as ex:
        print(ex)