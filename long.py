

# WRITE A FUNCTION TAKES STRING AS ARGUMENT AND THEN FINDS THE LOONGEST WORD AND PRINTS IT
def longest(*word):
    
    words=str(word)

    new_word =words.split(" ")

    vist = []

    for i in new_word:
        vist.append(i)
    
    vist.sort(key=len)

    print (vist[-1])

longest("loooogest vg hgf jhjgfd hfd")
