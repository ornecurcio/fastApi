import requests
import json

# response = requests.post("http://127.0.0.1:8000/create", json={"name": "Alice", "price": 5})

# Definir un nuevo endpoint que acepte un request con un texto, lo convierta a
# voz usando la librería gtts y guarde el audio en un archivo.
# Pruebenlo llamándolo desde un script y luego abran el archivo generado para
# confirmar que anduvo.

response = requests.post("http://127.0.0.1:8000/texto", json={"text": "Today is gonna be the day that they're gonna throw it back to you And by now, you should've somehow realised what you gotta do I don't believe that anybody feels the way I do about you now And backbeat, the word is on the street that the fire in your heart is out I'm sure you've heard it all before, but you never really had a doubt I don't believe that anybody feels the way I do about you now And all the roads we have to walk are winding And all the lights that lead us there are blinding There are many things that I would like to say to you, but I don't know how Because maybe"})
# You're gonna be the one that saves me
# And after all
# You're my wonderwall
# Today was gonna be the day, but they'll never throw it back to you
# And by now, you should've somehow realised what you're not to do
# I don't believe that anybody feels the way I do about you now
# And all the roads that lead you there were winding
# And all the lights that light the way are blinding
# There are many things that I would like to say to you, but I don't know how
# I said maybe
# You're gonna be the one that saves me
# And after all
# You're my wonderwall
# I said maybe (I said maybe)
# You're gonna be the one that saves me
# And after all
# You're my wonderwall
# I said maybe (I said maybe)
# You're gonna be the one that saves me (saves me)
# You're gonna be the one that saves me (saves me)
# You're gonna be the one that saves me (saves me)