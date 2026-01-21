# Mood-Based Song Suggester

A simple Python application that suggests songs based on your current mood.

## Overview

This program allows users to input their mood and receive personalized song recommendations. It features a curated database of 40 songs across five mood categories and provides random suggestions without repeating recommendations in the same session.

## Features

- **5 Mood Categories**: Happy, Sad, Love, Relaxed, Angry
- **40 Song Database**: A collection of popular songs organized by mood
- **Customizable Suggestions**: Choose how many songs you'd like (3-10)
- **No Repeats**: Songs are tracked and won't be suggested twice in the same session
- **User-Friendly Interface**: Simple text-based menu system

## How to Run

```bash
python main.py
```

## How to Use

1. Run the program
2. Choose from the main menu:
   - Enter `1` to get song suggestions
   - Enter `2` to exit
3. Select a mood from the available options
4. Choose how many songs you'd like (default: 3)
5. View your suggestions and request more if desired

## Available Moods

- Happy
- Sad
- Love
- Relaxed
- Angry

## Project Structure

- `main.py` - Main application file containing all functionality
- `SONG_LIST` - Database of 40 songs with titles and associated moods
- `AVAILABLE_MOODS` - List of mood categories

## Example

```
What mood are you in? Happy
Here are your 3 suggestions:
1. 'Walking on Sunshine' by Katrina and the Waves
2. 'Here Comes the Sun' by The Beatles
3. 'Good Vibrations' by The Beach Boys
```

## Technologies Used

- Python 3
- `random` module for song selection

## Potential Future Improvements (Not Promised)

- Add user ratings for songs
- Expand song database
- Implement genre filtering
- Save favorites to a file
