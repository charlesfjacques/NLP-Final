use_speech_to_text = False # Switch to true if using speech to text
def listen():
    if use_speech_to_text:
        from speech_to_text.stt_listen import listen as _listen
    else:
        from speech_to_text.non_stt_listen import listen as _listen
    return _listen()