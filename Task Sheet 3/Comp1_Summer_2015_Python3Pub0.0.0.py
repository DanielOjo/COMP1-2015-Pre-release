# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8
Kashshaptu = False
  
def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def GetPieceName(StartRank, StartFile, Board):
  #Gets the colour of the piece in the board 
  piece_colour = Board[StartRank][StartFile][0]
  if piece_colour == "W":
    piece_colour = "White"
  elif piece_colour == "B": 
    piece_colour = "Black" 
  #Gets the name of the piece in the board
  piece_name = Board[StartRank][StartFile][1]
  if piece_name == "R":
    piece_name = "Redum"
  elif piece_name == "S":
    piece_name = "Sarrum"
  elif piece_name == "M":
    piece_name = "MarzazPani"
  elif piece_name == "G":
    piece_name = "Gisgigir"
  elif piece_name == "N":
    piece_name = "Nabu"
  elif piece_name == "E":
    piece_name = "Etlu"
  #Task 22
  elif piece_name == "K":
    piece_name = "Kashshaptu"
  return piece_colour,piece_name


def GetTypeOfGame(): #Changed in Task 11 
  valid = False
  while not valid: 
    TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
    TypeOfGame = TypeOfGame.upper()[0]
    if TypeOfGame == "Y" or TypeOfGame == "N":
      valid = True
    else:
      print("Please enter Y or N")
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):            
    print("     -------------------------")
    print("R{0}".format(RankNo), end="   ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -------------------------")
  print()
  print("      F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def display_menu(): #Task 11
  print("Main Menu")
  print("1. Start new game")
  print("2. Load existing game")
  print("3. Play sample game")
  print("4. View high scores")
  print("5. Settings")
  print("6. Quit Program")

def get_menu_selection(): #Task 11
  valid = False
  while not valid:
    print()
    selection = int(input("Please select an option: "))
    if selection >0 and selection <=6:
      valid = True
    else:
      print("Please enter a valid number: ")
      valid = False
  return selection

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
        Kashshaptu = KashshaptuActive()
        #return Kashshaptu
        valid = True
      elif question == 9:
        print()
        valid = True        
    elif selection == 6: #Quit Program
      pass

def KashshaptuActive():
  kashshaptu_state = input("Do you wish to use the Kashshaptu piece (Y/N)? ")
  kashshaptu_state = kashshaptu_state.lower()
  if kashshaptu_state == "y":
    Kashshaptu = True
    print("Kashshaptu Active")
    print()
  elif kashshaptu_state == "n":
    print("Kashshaptu not active")
    print()
  else:
    print("please enter Y or N")

  return Kashshaptu
  
def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):#Task 19 #BUG Black piece can only move 2 spaces on first turn
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if StartRank == 7: #Start of the game
      if FinishRank == StartRank - 2:
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
        CheckRedumMoveIsLegal = True
  elif StartRank == 2:
    if FinishRank == StartRank + 2:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):#17
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): #Task 16
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) ==(abs(FinishFile - StartFile) == 0)):
      CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):#Task 18
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 1):  
    CheckEtluMoveIsLegal = True
  elif (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckKashshaptuIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile): #Task 22
  CheckKashshaptuIsLegal = False
  #if: #Work in progress
    #CheckKashshaptuIsLegal = True
  return CheckKashshaptuIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  elif 0 > FinishFile > 9 or 0 > FinishRank > 9: #This is what I added
    MoveIsLegal = False
  else:
    PieceType = Board[StartRank][StartFile][1]
    PieceColour = Board[StartRank][StartFile][0]
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
        
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    game_board = InitialiseSampleBoard(Board, SampleGame)
  else:
    game_board = InitialiseNewBoard(Board) 

def InitialiseSampleBoard(Board, SampleGame):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"

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
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S" #Added if statement to Swap the M & S round in the Rank = 1 (Where the Black pieces are)
            else:  
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"            

          elif FileNo == 5:
            if RankNo == 1:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M" #Same thing done here
            else:
              Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    

def display_in_game_options():#Task 12
  print()
  print("Options")
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender") #Task 13

def get_option():#Task 12
  print()
  valid = False
  while not valid:
    option = int(input("Please select an option: "))
    if option == 1: #Save Game
      valid = True
    elif option == 2: #Quit to Menu
      valid = True
    elif option == 3: #Return to Game
      valid = True
    elif option == 4: #Surrender #Task 13
      valid = True
    else:
      print("Please enter a valid option")
  return option
  
def GetMove(StartSquare, FinishSquare):
  valid = False
  while not valid:
    StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "))
    if StartSquare >10 and StartSquare <89:
      valid = True
    elif StartSquare == -1: #Task 12
      valid = True
    else:
      print("Please provide both FILE and RANK for this move")
  if StartSquare == -1: #I did this so that it would not ask for the Finish Square
    FinishSquare = FinishSquare
  else:
    valid = False
    while not valid:
      FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if FinishSquare >10 and FinishSquare <89:
        valid = True
      else:
        print("Please provide both FILE and RANK for this move")
  return StartSquare, FinishSquare                 

def ConfirmMove(StartSquare, FinishSquare):
  StartSquare = str(StartSquare)
  FinishSquare = str(FinishSquare)
  print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartSquare[1],StartSquare[0],FinishSquare[1],FinishSquare[1]))
  question = input("Confirm move?(Yes/No): ")
  question = question.lower()[0]
  if question == "y":
    confirm = True
  elif question == "n":
    confirm = False
  else:
    print("Please enter a valid answer!")
  return confirm
  

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, Kashshaptu):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    if Kashshaptu: #Task 22 added if statements for when Kashshaptu is active
      Board[FinishRank][FinishFile] = "WK"
      Board[StartRank][StartFile] = "  "
      print("White Redum promoted to Kashshaptu")
    else:
      Board[FinishRank][FinishFile] = "WM"
      Board[StartRank][StartFile] = "  "
      #Just needs a print statement :D
      print("White Redum promoted to Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    if Kashshaptu == True:
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
    
def play_game(SampleGame):
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    #SampleGame = GetTypeOfGame()

    #if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      #SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)

    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        if StartSquare == -1: #Task 12
          display_in_game_options()
          option = get_option()
          if option == 1: #Save Game #I need a way to break the while loop after an option has been selected 
            pass
          elif option == 2:
            #GameOver = True #<---- Did not break while loop >_>
            #Quit to Menu
            pass #This is handled by
                 #display_menu()and by
                 #selection = get_menu_selection()
                 #While loop may be needed in the main program :P
                 #Maybe function?
          elif option == 3: #Return to Game
            #Need to restart it to GetMove(StartSquare, FinishSquare)
            MoveIsLegal = False #restarts the while loop
          elif option == 4: #Surrender
            pass #This will be handled by GameOver
                 #This will be tricky >_>
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
        if MoveIsLegal:
          confirm = ConfirmMove(StartSquare, FinishSquare) #amending my function
          if not confirm:
            MoveIsLegal = False #restarts the while loop

      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)

      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn,Kashshaptu)
      if GameOver:
        DisplayWinner(WhoseTurn)
      if WhoseTurn == "W":
        WhoseTurn = "B"
      else:
        WhoseTurn = "W"

    PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
    if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
      PlayAgain = chr(ord(PlayAgain) - 32)

if __name__ == "__main__":
  checker = False #Set up this while loop
  while not checker: # I may need this later #I was right I did need it XD
    Board = CreateBoard() #0th index not used
    display_menu()#Task 11
    selection = get_menu_selection()#Task 11
    choice = make_selection(selection)#Task 11
    
  
      
