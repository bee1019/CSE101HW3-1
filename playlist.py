# Your name: Bansri Shah
# Your SBU ID: 110335850
# Your NetID (Blackboard username): bpshah
#
# CSE 101, Fall 2018
# Assignment 3-1 (Playlists) starter code

# Complete the functions below for this assignment

import string, random

def buildLibrary(filename):
    library = {}

    for line in open(filename):
        line = line.strip()
        temp = line.split(",")
        genre = temp[0]
        title = temp[1]
        artist = temp[2]
        colon = temp[3].index(":")
        time = int(temp[3][:colon]) * 60
        time += int(temp[3][colon + 1:])
        
        song = [title, artist, time]

        if genre not in library:
            library[genre] = [song]
        else:
            library[genre].append(song)
            
    return library


def buildPlayList(library, genres, length):
    tempList = []
    for i in genres:
        if i in library:
            tempList.extend(library[i])
    for i in range(len(tempList)):
        tempList[i] = tempList[i][:2]

    if len(tempList) == 0:
        return []
    elif len(tempList) < length:
        return random.sample(tempList, len(tempList))
    else:
        return random.sample(tempList, length)


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Test of Part 1
    print("Testing buildLibrary() with file 'library1.txt':")
    lib1 = buildLibrary("library1.txt")
    print("Library contents are:\n", lib1)
    print("\n\n")

    print("Testing buildLibrary() with file 'library2.txt':")
    lib2 = buildLibrary("library2.txt")
    print("Library contents are:\n", lib2)
    print("\n\n")

    print("Testing buildLibrary() with file 'library3.txt':")
    lib3 = buildLibrary("library3.txt")
    print("Library contents are:\n", lib3)
    print("\n\n")

    print("Testing buildLibrary() with file 'library4.txt':")
    lib4 = buildLibrary("library4.txt")
    print("Library contents are:\n", lib4)
    print("\n\n")

    # Test of Part 2
    # normal operation
    print("Testing buildPlayList() on the contents of library1.txt: 6 songs drawn from the blues, childrens, and dance genres:", buildPlayList(lib1, ["blues", "childrens", "dance"], 6))
    print()

    # Too few songs
    print("Testing buildPlayList() on the contents of library1.txt: 12 songs drawn from the blues and kpop genres:", buildPlayList(lib1, ["blues", "kpop"], 12))
    print()
    
    # Nonexistent genre
    print("Testing buildPlayList() on the contents of library2.txt: 4 songs drawn from the classical, country, and opera genres:", buildPlayList(lib2, ["classical", "country", "opera"], 4))
    print()
    
    # No valid genres
    print("Testing buildPlayList() on the contents of library3.txt: 8 songs drawn from the classical, childrens, and dance genres:", buildPlayList(lib3, ["classical", "childrens", "dance"], 8))
    print()
    

