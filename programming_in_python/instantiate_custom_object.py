class MyFirstClass(): # 1.1 Define a class
    print("Who wrote this?") # 1.2 Add a print statement inside it
    index = "Author-Book" # create a string variable named index, and initialize it with a string "Author-Book"

    def hand_list(self, philosopher, book): # 3.1 Define a function called hand_list() with the help of a def keyword
        print(MyFirstClass.index) # 3.2 Pass the parameter self into it and then pass two parameters, philospher, and book
        print(philosopher +" wrote the book " + book) # 4.1 Write a print statement using the print() function that will give such output such as:"Plato wrote the book: Republic"
# where "Plato" is the philosopher and "Republic" is the book

whodunnit = MyFirstClass() # 5.1 create and instantiate an object of that class, called whodunnit
whodunnit.hand_list("Sun Tzu", "The Art of War") #5.2 Call method hand_list() over this object "whodunnit" and pass two values to it namely "Sun Tzu" and "The Art of War".