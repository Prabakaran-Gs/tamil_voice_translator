from googletrans import Translator
from gtts import gTTS

translator = Translator()

def find_st(statement,d='ta',s='en'):
    '''
    Parameters : statement -> string that contains the words to be translated
    Parameters : d -> code for the language to be translated [ default = 'en' ]
    Parameters : s -> representation of the language of the string
    ****************************************************************
    returns : string that contains the traslated words
    '''
    t_st = translator.translate(statement,dest=d,src = s)
    return t_st

def voice_cmd(statement,src='ta'):
    '''
    Parameters : statement -> string for which voice is generated
    Parameters : src -> representation of language of the statement
    ****************************************************************
    returns : voice file is saved
    '''
    file = gTTS(statement,lang= src)
    file.save("static/voice.mp3")


def trans(statement):
    st = find_st(statement).text
    voice_cmd(st)