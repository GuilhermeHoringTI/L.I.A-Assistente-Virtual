import speech_recognition as sr
import pyttsx3
import pywhatkit
import os

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.runAndWait()


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'lia' in comando:
                comando = comando.replayce('lia', '')
                maquina.runAndWait()

    except:
        print('Microfone Off')

    return comando


def comando_voz():
    comando = executa_comando()
    if 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
    elif 'opera' in comando:
        resultado = os.system('start Opera.exe')
        maquina.say('Abrindo o Opera GX')
        maquina.runAndWait()
    elif 'google' in comando:
        resultado = os.system('start google.exe')
        maquina.say('Abrindo o Google')
        maquina.runAndWait()
    elif 'navegador' in comando:
        resultado = os.system('start msedge.exe')
        maquina.say('Abrindo o Microsoft Edge')
        maquina.runAndWait()
    elif 'excel' in comando:
        resultado = os.system('start excel.exe')
        maquina.say('Abrindo o Excel')
        maquina.runAndWait()
    elif 'word' in comando:
        resultado = os.system('start winword.exe')
        maquina.say('Abrindo o Word')
        maquina.runAndWait()
    elif 'powerpoint' in comando:
        resultado = os.system('start powerpnt.exe')
        maquina.say('Abrindo o Power Point')
        maquina.runAndWait()
    elif 'arquivos' in comando:
        resultado = os.system('start explorer.exe')
        maquina.say('Abrindo o Windows Explorer')
        maquina.runAndWait()


comando_voz()
