import sys
import operator
import spotipy
import spotipy.util as util
import os

scope = 'user-library-read';
limit = 100;

#insert lines for SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET AND SPOTIPY_REDIRECT_URI HERE, IN THIS FORMAT:
os.environ['SPOTIPY_CLIENT_ID'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
os.environ['SPOTIPY_CLIENT_SECRET'] ='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
os.environ['SPOTIPY_REDIRECT_URI']='http://XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

def mainloop():
    filename = "songdict.txt"
    infopersong = []
    songdict= {}
    #insert your Playlist ID's here! in phlist! please replace the y's. separate with commas, have them in quotes.
    phlist =["yyyyyyyyyyyyyy"]

    try:
        os.environ["SPOTIPY_CLIENT_ID"]
    except KeyError:
        print "Please set the environment variables"
        sys.exit(1)


    if len(sys.argv) > 1:
        username = sys.argv[1];
    else:
        print("Usage: %s username", sys.argv[0]);
        sys.exit();


    token = util.prompt_for_user_token(username, scope);
    if token:
        #set up file
        f = open(filename, "w")

        #authentication steps
        spotify=spotipy.Spotify(auth=token);
        print("Authenticated");
        sp = spotipy.Spotify(auth=token)

        for ID in phlist:
        #for each playlist, grab the song name.
            results = sp.user_playlist(username, ID)
            track = results.get("tracks")

            #tracks has a huge dictionary/list format
            for x in track['items']:
                infopersong.append(x)
            for song in range(1, len(infopersong)-1):
                songname = infopersong[song]['track']['name']
                # print songname
                if songname in songdict:
                    value = songdict.get(songname)+1
                    songdict[songname] = value
                else:
                    songdict[songname] = 1

        # orders dictionary with most valued keys first
        songdict=sorted(songdict.items(), key=operator.itemgetter(1), reverse=True);
        # print songdict
        
        #saves results to a file
        f.write(str(songdict))

if __name__ == "__main__":
    mainloop()
