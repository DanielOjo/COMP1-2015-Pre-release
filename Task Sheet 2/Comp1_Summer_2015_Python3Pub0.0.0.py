# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

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
  return piece_colour,piece_name


def GetTypeOfGame():
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
  print("2. Load exsiting game")
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
  if selection == 1: #Start new game
    pass 
  elif selection == 2: #Load exsiting game
    pass
  elif selection == 3: #Play sample game
    sample_game = play_game(Board)
  elif selection == 4: #View high scores
    pass
  elif selection == 5: #Settings
    pass
  elif selection == 6: #Quit Program
    pass
  
def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if ColourOfPiece == "W":
    if FinishRank == StartRank - 1:
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
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

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

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
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "    

def display_in_game_options():
  print()
  print("Options")
  print("1. Save Game")
  print("2. Quit to Menu")
  print("3. Return to Game")
  print("4. Surrender") #Task 13

def get_option(StartSquare, FinishSquare,WhoseTurn):
  print()
  option = int(input("Please select an option: "))
  if option == 1: #Save Game
    pass 
  elif option == 2: #Quit to Menu
    display_menu()
    selection = get_menu_selection()
    choice = make_selection(selection)
  elif option == 3: #Return to Game
    StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
  elif option == 4: #Task 13
    if WhoseTurn == "W": 
      print("White surrendered. Black wins!")
    else:
      print("Black surrendered. White wins!")
  

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
    FinishSquare = " "
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
  

def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    #Just needs a print statement :D
    print("White Redum promoted to Marzaz Pani")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
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

def play_game(Board):
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    SampleGame = GetTypeOfGame()

    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)

    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        StartSquare, FinishSquare = GetMove(StartSquare, FinishSquare)
        if StartSquare == -1: #Task 12
          display_in_game_options()
          options = get_option(StartSquare, FinishSquare,WhoseTurn)
        StartRank = StartSquare % 10
        StartFile = StartSquare // 10
        FinishRank = FinishSquare % 10
        FinishFile = FinishSquare // 10
        MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
        if not(MoveIsLegal):
          print("That is not a legal move - please try again")
        confirm = ConfirmMove(StartSquare, FinishSquare) #amending my function
        if not confirm:
          MoveIsLegal = False #restarts the while loop

      GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)

      MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
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
  Board = CreateBoard() #0th index not used
  display_menu()#Task 11
  selection = get_menu_selection()#Task 11
  choice = make_selection(selection)#Task 11
  
      
