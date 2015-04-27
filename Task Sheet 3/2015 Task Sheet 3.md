
#Task Sheet 3 - Further Game Improvements

##Introduction
This series of tasks focuses on adding additional features to the Capture the Sarrum game.

##Task 21 - Sarrum and Marzaz Pani initial positions
When a new game is started, the positioning of the pieces on the board is **symmetrical**:

![](images/board_setup.png)

In the game of Chess, the King and Queen pieces are positioned differently. The King of one side faces the Queen of the opposing side. If Capture the Sarrum was changed so that the Sarrum and Marzaz Pani followed the Chess positioning rules the board would look as follows:

![](images/altered_board_setup.png)

Attempt the **exercises** below.

---
1. **Identify** the function responsible for positioning the Sarrum and Marzaz Pani pieces during the setup of the board.
`InitialiseNewBoard`
2. **Make** the neccessary changes to this function so that the setup positioning reflects the screenshot above.
```python
def InitialiseNewBoard(Board):
  for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"

          elif FileNo == 4:
            #Task 21
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S" #Added if statement to Swap the M & S round in the Rank = 1
            else:  
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"            

          elif FileNo == 5:
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M" #Same thing done here
            else:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "  
```
---

##Task 22 - Kashshaptu
In the preliminary material there is mention of an additional piece called a **Kashshaptu** or **Witch**. The preliminary material mentions that it is not known how this piece is supposed to work in the game.

One interpretation of the **Kashshaptu** is that it is a special piece that only enters play once a **Redum** has been **promoted** i.e. the Redum is promoted to a Kashshaptu instead of a Marzaz Pani.

The Kashshaptu piece is very powerful and is capable of moving and taking pieces as if it were any of the other pieces **except** the Sarrum itself.

Because this piece is so powerful its inclusion in the game is always **optional**.

To add this to the game a settings **sub-menu** is required:

![](images/submenu.png)

This menu will provide the option to turn the piece on and off as the user wishes. It should always be **off** when the program loads but if the setting is changed to **on** then all games will use the Kashshaptu piece until either the option is turned off again or the program exits.

Once in game, if a Redum is promoted an appropriate message should be displayed and the code **WK** or **BK** should be used to represent the Kashshaptu:

![](images/redum_promotion.png)

Attempt the **exercises** below.

---
1. **Add** the necessary functions to the program so that the settings menu shown above is added to the game. **Ensure** that the value indicating whether the Kashshaptu is on or off is easily accessible by all the other functions in the program.
```python
def make_selection(selection): #Task 11
  valid = False
  while not valid:
    if selection == 1: #Start new game
      play_game("N")
      valid = True 
    elif selection == 2: #Load exsiting game
      pass
    elif selection == 3: #Play sample game
      play_game("Y")
      valid = True
    elif selection == 4: #View high scores
      pass
    elif selection == 5: #Settings
      #Task 22
      print()
      print("1. Use Kashshaptu Piece")
      print("9. Return to Main Menu")
      question = int(input("Please select setting to change "))
      if question == 1:
        kashshaptu_state = input("Do you wish to use the Kashshaptu piece (Y/N)? ")
        kashshaptu_state = kashshaptu_state.lower()
        if kashshaptu_state == "y":
          print("Kashshaptu Active")
          print()
          display_menu()
        elif kashshaptu_state == "n":
          print("Kashshaptu not active")
          print()
          display_menu()
        else:
          print("please enter Y or N")
      elif question == 9:
        print()
        display_menu()                      
```
2. **Identify** the function responsible for promoting the Redum piece.
`MakeMove`

3. **Make** any necessary changes to the function identified in question 2 so that the Redum can be promoted to a Kashshaptu **if** the option to use this piece has been turned on.
```python
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    if Kashshaptu = True: #Task 22 added if statements for when Kashshaptu is active
      Board[FinishRank][FinishFile] = "WK"
      Board[StartRank][StartFile] = "  "
      print("White Redum promoted to Kashshaptu")
    else:
      Board[FinishRank][FinishFile] = "WM"
      Board[StartRank][StartFile] = "  "
      #Just needs a print statement :D
      print("White Redum promoted to Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    if Kashshaptu = True:
      Board[FinishRank][FinishFile] = "BM"
      Board[StartRank][StartFile] = "  "
      print("Black Redum promoted to Kashshaptu")
    else:
      Board[FinishRank][FinishFile] = "BM"
      Board[StartRank][StartFile] = "  "
      print("Black Redum promoted to Marzaz Pani")
  else:
    piece_colour, piece_name = GetPieceName(FinishRank, FinishFile, Board)
    piece_colour2, piece_name2 = GetPieceName(StartRank, StartFile, Board)
    if piece_colour == "White" or piece_colour == "Black":
      print("{0} {1} has taken {2} {3}".format(piece_colour2, piece_name2,piece_colour, piece_name))
    Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
    Board[StartRank][StartFile] = "  "
```
4. **Ensure** that the correct piece name is displayed when the Redum is promoted and make any improvements required to do so
I added a print statement for when the piece is promoted
5. The Kashshaptu piece can move as if it were any of the other pieces, except the Sarrum. **Write** a function that will check to make sure the Kashshaptu move is legal. In addition, make any other improvements necessary to ensure that a Kashshaptu move is recognised correctly.

7. Write a **test plan** to ensure that the Kashshaptu functionality works as intended.

---

##Task 23 - Hall of Fame
Many games have the ability to view high scores, so you can see who in your group is the best at the game. Whilst there is no real scoring in Capture the Sarrum it would be possible to track the **number of moves** the winner takes to capture the Sarrum. This could then be displayed in a table, accessible from the main menu:

![](images/no_scores.png)

![](images/high_scores.png)

**Notice** that either a message saying that there are no scores or a table is displayed (depending on what is appropriate).

Attempt the **exercises** below.

---
1. **Write** a new function called `display_high_scores()` that takes a list of scores as an argument and then either presents an appropriate formatted table of the scores (similar to the one given above) or a message saying that there are currently no scores.
---

In order to add their name and score to the table the winner of each game should be prompted as shown:

![](images/add_score.png)

Attempt the **exercises** below.

---
2. **Make** the changes necessary to track the number of moves that have been played in the game.
3. **Amend** the function responsible for displaying the winning message so that it shows the number of moves taken (similar to the screenshot above).
4. **Add** the function(s) necessary to prompt the user to add their score to the high score table. **Ensure** that you include the following when storing the score:

    - Player name
    - Colour played
    - Number of moves taken
    - The current date
---

##Task 24 - Save Hall of Fame
In the last task you added the ability to track high scores but they do not **presist** between runs of the program i.e. the scores are lost when the program exits.

The score table should be saved to a **file** when the program exits.

Attempt the **exercises** below.

---
1. **Write** a new function called `save_high_scores()` that takes `scores` as an argument and then saves then to either a binary or text file.
2. **Modify** the program so that the `save_high_scores()` function is called before the program exits.
---

##Task 25 - Load Hall of Fame
Now that the program stores the scores into a file it should be possible to load these scores when the program first loads.

Attempt the **exercises** below.

---
1. **Write** a new function called `load_high_scores()` that loads the scores from a file and then returns the list of scores. **Ensure** that your function can deal with the situation where no file is found.
2. **Modify** the program so that the `load_high_scores()` function is called when the program launches.
---

##Task 26 - Save and Load Board Games
Sometimes it is not possible to finish a game that you have started, perhaps you get called away for dinner or you are going out to meet friends. In these situations it would be handy to be able to save the game and continue it at a later date.

You have already added an **in-game menu** that enables you to select a save option from within the game:

![](images/save_game.png)

In addition there is an option on the main menu to load a game.

Attempt the **exercises** below.

---
1. **Identify** the pieces of data that will need to be saved to be able to resume a game from where you left off:

    |Number|Data Description|
    |------|----------------|
    |1| |
    |2| |
    |3| |
    |4| |
    |5| |
    |6| |
    |7| |

2. **Write** a new function called `save_board_state()` that takes the argument `board_state` and then saves this to either a binary or text file.
3. **Make** any necessary changes to the program so that it is possible to call the `save_board_state()` function from the in-game menu.
4. **Write** a new function called `load_board_state()` that loads the board state from a file and returns it to the program.
5. **Make** any necessary changes to the program so that it is possible to call the `load_board_state()` function from the main menu and then resume the saved game.
---

##Task 27 - Resume Current Game
Occasionally it may be necessary to use the **in-game** menu option **Quit to Menu**:

![](images/quit_to_menu.png)

This may be because you want to check some high scores or something similar. In this case it should be possible to **resume** the game you were playing rather than having to start a new one or explicitly save and load the game.

If a game is in progress the program should detected this when selecting the following options from the main menu:

- Start new game
- Play sample game

![](images/resume_game)

In the above screenshot the program prompts you to decide whether you want to continue the previous game or not.

Attempt the **exercises** below.

---
1. **Make** any necessary changes to the game so that the state of the game is saved when quitting to the main menu.
2. **Make** any necessary changes to the program so that the user has the option of restoring a previously started game when selecting "**Start new game**" or "**Play sample game**" from the main menu.
---

##Task 28 - Sort Hall of Fame
Currently the hall of fame is presented in the order that the entries were added to the list. It would be better if they were **sorted** so that those that won in fewer moves are at the top i.e. ascending order.

Attempt the **exercises** below.

---
1. **Write** a new function called `sort_high_scores()` that will take the list of scores as a parameter and sort them appropriately. You should use the **bubble sort** algorithm to do this.
2. **Make** any necessary changes to the program so that this new function is called before the scores are displayed.
---

##Next
This task sheet has focused on improving the game further. The final task sheet will give some suggestions for further improvements that you can make to the game.






> Written with [StackEdit](https://stackedit.io/).