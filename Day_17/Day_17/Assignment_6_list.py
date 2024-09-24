# song = []
#
#     def add_songs():
#         song.append(input('Enter song name:'))
#         print("Song added to ur list")
#
#     def remove_song():
#         song.remove(input('Enter song name to delete:'))
#         print("Song deleted from ur list")
#
#     def display_song():
#         print(f'Your song list : {", ".join(song)}')
#
#     def slice_playlist():
#         start = int(input("Enter the starting index: "))
#         end = int(input("Enter the end index: "))
#         print(f"Your sliced list: {song[start:end]}")
#         return song[start:end]
#
#     add_songs()
#     add_songs()
#     add_songs()
#     display_song()
#     remove_song()
#     slice_playlist()
# # print(song)
# except Exception as e:
#     print(e)
#
# finally:
#     print("Execution completed")



list1=[]

def Add_songs(*args):
    for i in args:
        list1.append(i)

def Remove_song(title):
    list1.remove(title)

def View_Songs():
    print(list1)

def sliced_Playlist(start,end):
    print(list1[start:end])

Add_songs("Tum se","Heeriye","Malhaari","Gajanana","Bulleya")
View_Songs()
Remove_song("Bulleya")
View_Songs()
sliced_Playlist(2,4)