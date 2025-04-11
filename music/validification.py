def clean_word(word):
    cleaned = ""
    for i in word:
        if i.isalpha():
            cleaned += i
    return cleaned

def get_song_name_artist(query):
    q = query.lower().split()
    song_title = ""
    artist_title = ""
    artist_check = None
    if "by" in query: #change this later to prompt grammar?
        artist_check = True
    for i in q:
        if i == "play": #change this later to prompt grammar?
            if artist_check:
                song_list = q[q.index(i)+1:q.index("by")]
            else:
                song_list = q[q.index(i)+1:]
        if i == "by" and artist_check: #change this later to prompt grammar?
            artist_list = q[q.index(i)+1:]

    try:
        for i in song_list:
            song_title += i + " "

        if artist_check:
            for i in artist_list:
                artist_title += i + " "
    except:
        song_title = None
        artist_title = None

    return(song_title, artist_title)

def check_title(song_title):
    #search through spotify if the song exists, take that title (add later)
    spotify_title = "Back In The U.S.S.R - Remastered 2009"

    alpha_song_list = []
    #this section seees if all the words in the song query all purely alphabetical
    for i in song_title.split():
        if i.isalpha():
            alpha_song_list.append(True)
        else:
            alpha_song_list.append(False)

    # print(alpha_song_list)

    running = True
    valid = None
    start = 0
    while running:
        test_list = [] 
        #moving test until the spotify title has the query title
        for i in range(len(song_title.split())):
            song_w = song_title.split()[i]
            try:
                spotify_w = (spotify_title.lower().split()[i+start])
            except:
                valid = False
                return valid
        
            if alpha_song_list[i] == True:
                spotify_w = clean_word(spotify_w)
            if song_w == spotify_w:
                test_list.append(True)
            else:
                test_list.append(False)

        if all(test_list):
            valid = True
            running = False
        else:
            start +=1
    return valid

def check_artist(artist_title):
    #get artists from same spotify track - list of strings
    spotify_artists = ["Beach Boys", "The Beatles"]
    
    running = True
    valid = None
    while running:
        #searches each artist and sees if it matches
        for a in spotify_artists:
            test_list = []
            if len(a.split()) == len(artist_title.split()):
                for n in range(len(a.split())):
                    if a.split()[n].lower() == artist_title.split()[n]:
                        # print(a.split()[n].lower(),artist_title.split()[n])
                        test_list.append(True)
                    else:
                        test_list.append(False)
        if all(test_list) and len(test_list) >0:
            valid = True
            running = False
        else:
            valid = False
            running = False

    return valid
