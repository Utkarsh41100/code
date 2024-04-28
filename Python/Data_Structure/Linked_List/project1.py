""" Project Idea: Music Playlist Manager

Description:
Create a music playlist manager application using linked lists. This application allows users to create, edit, and manage playlists of songs.

Features:

Song Database: Implement a linked list to store information about songs. Each node of the linked list can represent a song, containing attributes such as song title, artist, album, duration, etc.
Playlist Creation: Allow users to create multiple playlists. Each playlist will be represented by a separate linked list, where each node contains a reference to a song in the song database.
Playlist Operations: Implement operations such as adding songs to a playlist, removing songs from a playlist, and displaying the contents of a playlist.
Playlist Management: Enable users to rename playlists, delete playlists, and reorder songs within a playlist.
Playback Functionality: Add basic playback functionality to play songs from the playlist. You can simulate playback by printing the details of the currently playing song (title, artist, duration).
Search and Sorting: Implement search functionality to find songs by title, artist, or album. Additionally, allow users to sort songs within a playlist based on different criteria (e.g., title, artist, duration).
User Interface (Optional): If you're comfortable with GUI frameworks like Tkinter or PyQt, consider creating a graphical user interface (GUI) for your application to enhance user experience.
Implementation Tips:

Start by designing the classes and data structures for songs and playlists. Plan how they will interact with each other.
Implement basic operations such as insertion, deletion, and traversal for linked lists.
Test each functionality thoroughly to ensure correctness and robustness.
Consider error handling and edge cases, such as handling empty playlists or invalid input.
Extensions:

Implement additional features such as shuffle, repeat, and skip functionality.
Integrate file I/O to load and save playlists from/to disk.
Explore advanced data structures like doubly linked lists or circular linked lists for more efficient operations.
Enhance the user interface with features like album artwork display, song progress bar, or keyboard shortcuts.
Building a music playlist manager using linked lists will not only reinforce your understanding of linked list operations but also provide a practical application to showcase your programming skills. Have fun coding!

Take a hint from this code """

class Student:
    def __init__(self, name, trade, reg_number):
        self.name = name
        self.trade = trade
        self.reg_number = reg_number

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Other methods like insert_at_index, deleteatbeg, deleteatlast, deleteatindex, display remain unchanged

# Testing the LinkedList

first = LinkedList()
first.insert_at_beginning(Student("Alice", "Computer Science", "CS101"))
first.insert_at_end(Student("Bob", "Electrical Engineering", "EE201"))
first.insert_at_end(Student("Charlie", "Mechanical Engineering", "ME301"))
first.display()

