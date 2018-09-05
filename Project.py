import re             #all needed imports for program
import urllib.request
import webbrowser
import time
import random

def main(songs): #main function where primary variables are set
    library=[]
    print("Enter your song(s) into the library with this format: 'SONG x ARTIST'\nIf you would like to finish entering songs before the inital limit, enter 'N' \n")
    x=0
    while x<songs: #run this loop as many times as there is # of songs, unless requested otherwise
        
        while True: #while loop for input robusticity
            print("Enter your song and artist:")
            song=input("")
            if song == 'N' or song == 'n' or song == "No" or song == "no":
                break
            if "x" in song or "X" in song:
                break
            print("\n*****Sorry, you need to enter a valid input!*****\n")

        if song == 'N' or song == 'n' or song == "No" or song == "no":
            break
               
        library.append(song) #add input into music library
        x+=1 #increase count for while loop
    pickSong(library) #call for function

def pickSong(library): #function for allowing user to choose what song to play
    
    count=0 #variable for song #
    print("\nHere is your music library. Choose the number of the respective song to choose what song to play.\n")
    for line in library: #iterate through list, print each object with each index
        print(count,"-----",line)
        count+=1
        
    if len(library)>1: #sets choice # for optional random song, "shuffle"
        print(count,"-----","SHUFFLE")
        
    ans="y" #loop for whether user wants to play another song in library
    while ans == "y" or ans =="Y" or ans == "Yes" or ans =="yes" or "y" in ans or "Y" in ans:
        nums=[] #list for robusticity
        for x in range(0,len(library)+1):
            nums.append(str(x))
            
        while True: #while loop for robusticity, includes num[] list
            choice=input("\nWhich song would you like to play? ")
            if len(choice)<5 and choice in nums:
                choice=int(choice)
                break
            print("\n*****Sorry, you have to enter a valid integer input.*****\n")

        if len(library)>1: #if more than one song in library, implement shuffle option
            if choice == len(library):
                choice= random.randint(0,len(library)-1)
        
        playSong(library,choice) #calls for function where song choice is transformed into youtube link
        print()

        while True: # (robust while loop) when playSong function funs, ask if user if they want to play anothe song
            ans=input("Would you like to play another song? ")
            if "y" in ans or "Y" in ans or "ye" in ans or "Ye" in ans or "n" in ans or "N" in ans:
                break
            if type(ans) is int:
                break
            print("\n*****Sorry, please enter a valid input.*****\n")

def playSong(library,choice): #function for link translation
    songChoice=library[choice] #song chosen
    song=songChoice.replace(" ","+")#replace spaces with +'s for link
    site= "https://www.youtube.com/results?search_query="+song #song search query for video link

    find = b'<a.*?/a>' #HTML filter
    reader = urllib.request.urlopen(site) #reader for HTML page/source code
    allLinks = re.findall(find,reader.read(),re.MULTILINE) #find all "links" on current youtube search page

    links = []
    linkClass = 'class="yt-uix-sessionlink yt-uix-tile-link' 

    for temp in allLinks: #add all links to list
        if b'linkClass in temp':
            url_filter = b'href=".*?"'
            linkTemp = re.findall(url_filter,temp,re.MULTILINE)
            links.append(linkTemp)

    link=""
    for x in links:     #find the actual YOUTUBE VIDEO links
        link_str=str(x[0])
        if "watch?" in link_str: #since first "watch" occurance in youtube links is the song, choose this link
            watchSpot=link_str.index("watch?") 
            link="https://www.youtube.com/"+link_str[watchSpot:] #add the specific song video link to base youß-youtube link
            link=link[:-2]
            print("Loading song...")    #open the youtube video link in browser (play song)
            time.sleep(2)
            webbrowser.open(link)
            break

ans="y"

while ans=="y" or ans=="Y" or ans =="yes" or "y" in ans: #loop if user wants to play another song
    x=10000 #set max for # of songs in library
    nums=[]
    for spot in range(0,x): #add indexes into list, convert to string to check for input robusticity
        nums.append(str(spot))
        
    while True: #input robusticity
        songs=input("Enter the number of songs you would like to enter into your music library: ")
        if len(songs)<5 and songs in nums:
            songs=int(songs)
            break
        print("\n*****Sorry, you have to enter a valid integer input.*****\n")
        
    print()
    main(songs) #call for main function with library
    print("--------------------------------------")

    while True: #input robusticity
            ans=input("Would you like to create another music library?")
            if "y" in ans or "Y" in ans or "ye" in ans or "Ye" in ans or "n" in ans or "N" in ans:
                break
            if type(ans) is int:
                break
            print("\n*****Sorry, please enter a valid input.*****\n")

