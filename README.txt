This code analyzes my (lisajoellehachmann) playlists for the most played songs and artists. It is specifically for the playlists contained in the phlist variable, where I provided each playlist's ID.

To get this code to run you need to:
1. Have python 2.7
2. Install Spotipy
3. Have authorization keys from Spotify. These rules and methods keep changing, so I will just say look it up with Spotify API. You'll need a client ID, a secret client id, and a callback url.
4. Replace the os variables left as 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX' with the authorization variables you just got.
5. Probably replace my playlists with yours. You'll need to go to each playlist on the web version of spotify (https://open.spotify.com/browse/featured), click them, and when it's on the playlist's page, it should be the back portion of the URL. This is the playlist ID.
Example: This is the format: https://open.spotify.com/user/xxxxxxxx/playlist/yyyyyyyyyyyyyyyyyyyyy
x's represent the spot with my user ID number and y's represent the playlist ID.
6. In order to run the code, you'll need to (in the command line) say python Ph_dictionary_songs.py xxxxxxxxxx
Again, here the x's represent your username ID. You'll need to put that number there.
7. It should take you to a web page, say "Is this you?" along with your Spotify username/profile picture, and you'll say yes. It'll go to your callback url, except with some extra string of numbers/letters on the end. Copy the whole thing and put it in the command line, which is waiting for this.
If you've done this exact thing already, it'll stop asking for this.
8. Either uncomment the line "print songdict", or open songdict.txt, which is now in the same folder. Now you know which songs you've added to your playlists the most.
