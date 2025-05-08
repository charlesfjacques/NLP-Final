use_speech_to_text = False # Switch to true if using speech to text

def load():
    if use_speech_to_text:
        from speech_to_text.stt_listen import load as _load
        _load()

def listen():
    if use_speech_to_text:
        from speech_to_text.stt_listen import listen as _listen
    else:
        from speech_to_text.non_stt_listen import listen as _listen
    return _listen()

def check_for_word(sentence, key_words): # function that takes a list or string, and listens for a key word, if said returns true
    sentence = sentence.upper().strip().split()
    
    if isinstance(key_words, str):
        key_words = [key_words.upper()]
    else:
        key_words = [word.upper() for word in key_words]
    
    return any(word in sentence for word in key_words)