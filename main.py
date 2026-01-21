# Mood-based Song Suggester
import random

AVALIABLE_MOODS = ["Happy", "Sad", "Love", "Relaxed", "Angry"]

SONG_LIST = [
    {"title": "'Happy' by Pharrell Williams", "mood": "Happy"},
    {"title": "'Someone Like You' by Adele", "mood": "Sad"},
    {"title": "'Thinking Out Loud' by Ed Sheeran", "mood": "Love"},
    {"title": "'Weightless' by Marconi Union", "mood": "Relaxed"},
    {"title": "'Break Stuff' by Limp Bizkit", "mood": "Angry"},
    {"title": "'Don't Stop Me Now' by Queen", "mood": "Happy"},
    {"title": "'Hurt' by Johnny Cash", "mood": "Sad"},
    {"title": "'Perfect' by Ed Sheeran", "mood": "Love"},
    {"title": "'Banana Pancakes' by Jack Johnson", "mood": "Relaxed"},
    {"title": "'Killing in the Name' by Rage Against the Machine", "mood": "Angry"},
    {"title": "'Walking on Sunshine' by Katrina and the Waves", "mood": "Happy"},
    {"title": "'The Night We Met' by Lord Huron", "mood": "Sad"},
    {"title": "'All of Me' by John Legend", "mood": "Love"},
    {"title": "'Three Little Birds' by Bob Marley", "mood": "Relaxed"},
    {"title": "'Enter Sandman' by Metallica", "mood": "Angry"},
    {"title": "'Good Vibrations' by The Beach Boys", "mood": "Happy"},
    {"title": "'Mad World' by Gary Jules", "mood": "Sad"},
    {"title": "'At Last' by Etta James", "mood": "Love"},
    {"title": "'Ocean Eyes' by Billie Eilish", "mood": "Relaxed"},
    {"title": "'Bodies' by Drowning Pool", "mood": "Angry"},
    {"title": "'I Wanna Dance with Somebody' by Whitney Houston", "mood": "Happy"},
    {"title": "'Everybody Hurts' by R.E.M.", "mood": "Sad"},
    {"title": "'Can't Help Falling in Love' by Elvis Presley", "mood": "Love"},
    {"title": "'Come Away with Me' by Norah Jones", "mood": "Relaxed"},
    {"title": "'Given Up' by Linkin Park", "mood": "Angry"},
    {"title": "'Lovely Day' by Bill Withers", "mood": "Happy"},
    {"title": "'Tears in Heaven' by Eric Clapton", "mood": "Sad"},
    {"title": "'Make You Feel My Love' by Adele", "mood": "Love"},
    {"title": "'Breathe Me' by Sia", "mood": "Sad"},
    {"title": "'Chop Suey!' by System of a Down", "mood": "Angry"},
    {"title": "'Mr. Blue Sky' by Electric Light Orchestra", "mood": "Happy"},
    {"title": "'Black' by Pearl Jam", "mood": "Sad"},
    {"title": "'Your Song' by Elton John", "mood": "Love"},
    {"title": "'Bloom' by The Paper Kites", "mood": "Relaxed"},
    {"title": "'Last Resort' by Papa Roach", "mood": "Angry"},
    {"title": "'Here Comes the Sun' by The Beatles", "mood": "Happy"},
    {"title": "'Skinny Love' by Bon Iver", "mood": "Sad"},
    {"title": "'Unchained Melody' by The Righteous Brothers", "mood": "Love"},
    {"title": "'Holocene' by Bon Iver", "mood": "Relaxed"},
    {"title": "'You Oughta Know' by Alanis Morissette", "mood": "Angry"},
]

def format_song(song):
    return song['title']

def song_suggestion():
    mood_song_list = []

    user_mood = input(f"What mood are you in? {AVALIABLE_MOODS}").strip().capitalize()

    if not user_mood:
        print("No mood was inputted. We aren't mind readers try again.")
        return
    
    try:
        if user_mood in AVALIABLE_MOODS:
            for song in SONG_LIST:
                if song["mood"] == user_mood:
                    print_ready_song = format_song(song)
                    mood_song_list.append(print_ready_song)
    except:
        print(f"Mood not found in database. Please choose a mood we provide {AVALIABLE_MOODS}")

    suggestions = random.sample(mood_song_list, k=min(3, len(mood_song_list)))
    print(suggestions)
    

song_suggestion()