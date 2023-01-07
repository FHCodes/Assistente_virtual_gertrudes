# Capturar audio, trabalha com 3 bibliotecas -> pip install gcloud, pip install google-api-python-client e pip install PyAudio
import speech_recognition as sr 
from playsound import playsound # Tocar um audio
from cria_audios import cria_audio
import unidecode
from random import choice


hotword = ['gertrudes','stoodi','gertrude','studio','street','virtude','strut','pertutti','trudys']

def dialogo():
    count = 0
    while True:
        trigger = captura_audio()
        print('Você disse:' + trigger)

        if trigger in hotword:
            if count == 0:
                resposta('fixos/Saudacao')
                emocao = False
            if count == 1:
                resposta('fixos/Acertou_gg')
                resposta('fixos/Saudacao')
                emocao = False
            if count > 1:
                cria_audio(f"Erraste meu nome {count} vezes!!!",'Bolada')
                resposta('Bolada')
                resposta('fixos/gg_puta')
                emocao = True
            
            while True:
                trigger = captura_audio()
                print(trigger)
                executa_comandos(trigger,emocao)
        else:
            count +=1
            resposta('fixos/Nao_Entende')

def captura_audio():
    while True:
        try:
            microfone = sr.Recognizer()
            with sr.Microphone() as source:
                print("Aguardando comando !!!")
                microfone.adjust_for_ambient_noise(source, duration=0.5)
                audio = microfone.listen(source)
                trigger = microfone.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower().strip()
                return trigger
        except sr.UnknownValueError:
            print("Não foi possivel reconhecer o audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
    
def executa_comandos(trigger,emocao):
    if ('boa noite' in trigger or 'boa tarde' in trigger or 'bom dia' in trigger) and ('para' in trigger or 'ao' in trigger):
        saudacao(trigger,emocao)

    elif ('eu' in trigger and 'bonito' in trigger):
        bonito(emocao)

    elif 'alexa' in trigger:
        melhor()
    
    elif 'feliz natal' in trigger:
        resposta('fixos/feliz_natal')

    elif 'toca' in trigger:
        tocar(trigger)
        
    else:
        resposta('fixos/Nao_Entendo2')

#Dialogo

def saudacao(trigger,emocao):
    nome = trigger.split().pop()

    if 'bom dia' in trigger:
        cria_audio(f'Espero que tenhas um bom dia {nome}',unidecode.unidecode(nome) + 'bomDia')
        resposta(unidecode.unidecode(nome) + 'bomDia')
    elif 'boa tarde' in trigger:
        cria_audio(f'Espero que tenhas uma boa tarde {nome}',unidecode.unidecode(nome) + 'boaTarde')
        resposta(unidecode.unidecode(nome) + 'boaTarde')
    elif 'boa noite' in trigger:
        cria_audio(f'Espero que tenhas uma boa noite {nome}',unidecode.unidecode(nome) + 'boaNoite')
        resposta(unidecode.unidecode(nome) + 'boaNoite')

def bonito(emocao):
    if emocao == False:
        escolhas = ['Eu_bonito2','Eu_bonito3','Eu_bonito4','Eu_bonito5']
        elemento = choice(escolhas)
        resposta(f'fixos/{elemento}')

    else:
        resposta('fixos/Eu_Bonito')
      
    
def melhor():
    resposta('fixos/compara')

def tocar(trigger):
    if 'natal' in trigger:
        resposta('fixos/JN')
    
def resposta(nome):
    playsound(f'audios/{nome}.mp3')

dialogo()
   