from take_command import take_command
from events import save_event
from speak import speak
from validate import validate_name
from wish_me import wish_me

def main():
    speak("Podemos iniciar a entrevista?")
    print("Diga [SIM PODEMOS] para avançar!")
    query = take_command().lower()

    if 'sim podemos' in query:
        speak("Certo, qual é seu nome?")
        print("Diga [SEU NOME] para avançar!")
        name = take_command()

        if validate_name(name) is False:
            speak("Desculpe, não entendi seu nome!")

        wish_me(name)

        speak("Podemos começar falando um pouco sobre você?")
        print("Diga [SIM] para avançar!")
        query = take_command().lower()

        if 'sim' in query:
            speak('Legal, agora me conte sobre você!')
            query = take_command().lower()
            save_event(query)
 
 
if __name__ == "__main__":
    main()
