from gtts import gTTS  # Converte textos para audio
from playsound import playsound # Tocar um audio

def cria_audio(audio,nome_audio):
    tss = gTTS(audio, lang='pt', tld='pt')
    tss.save(f'audios/{nome_audio}.mp3')
    



cria_audio('Espero que todos tenham um feliz natal !!!','feliz_natal')


#playsound('audios/jorgebomDia.mp3')


# import unidecode

# original = 'João é o ronaldo'
# print(unidecode.unidecode(original) + 'jojo')