# Battleship Game

![battleship game](/images/battleship-game-play.png)

- https://battleships-23-b994430075a8.herokuapp.com/

- Created a simple battleship game user vs computer. 
- The game begins with the game rules.

## Game Rules:

- The game is played on an 8x8 grid.
- The computer randomly places 5 ships on the grid.
- Your objective is to destroy all the computer's ships by guessing their locations.
- On each turn, you will enter a row and column to guess the location of a ship.
- If your guess is a hit, the corresponding position on the guess board will show 'X'.
- If your guess is a miss, the corresponding position on the guess board will show '-'.
- You have a total of 10 turns to sink all the ships.
- The game ends when you either sink all the ships or run out of turns.
- To enter your guess, input the row and column using the format 'A1' to 'H8'.
- If you enter an invalid row or column, you will be prompted to enter a valid choice.
- You cannot guess the same position multiple times.
- The grid will be displayed after each guess, showing your hits, misses, and remaining turns.

![game rules](/images/game-rules.png)

- Then you scroll down to the gameplay board.

![boardgame](/images/board-game-play.png)

## Features:

- You have a total of 10 turns to sink the ship.
- After 10 truns and you have not won you are told that you have run out of turns. 
- Player takes turn by entering first row number 1 for example.
- Then the palyer is asked to enter collumn letter A for example.
- This detrmines the move.
- After each turn the board will dispaly and ("X") for a hit or a ("-") for a miss.
- If the player hits a battleship, a congratulatory message is displayed.
- If the player misses, a message indicating a miss is displayed.

## Testing:

- I have tested the gameplay within the console of codeanywhere while building the game.
- After deploying to Heroku i then tested the game to check it is working properly. 

## Validator Testing:

- tested the code in CL Python Linter and discovered issues with white space
- lines to long and not eneough line spacing between lines. 
- all of which have been fixed. 
- one issue i have not been able to solve is missing whitespace after ','
- on lines 79 and 89

![cl python linter](/images/cl-python-linter.png)

## Technologies used:

## Languages:

- Python: The main language used to develop the application.
- JavaScript: The language used by the Code Institute to run the mock terminal in the browser.
- HTML: The language used by the Code Institute to create the layout needed to run the mock terminal in the browser.


## Bugs:

- Found a bug with application accepting an empty input.
- I fixed it by adding an aditional check in the (if) statement. 


## Deployment:

- The application has been deployed to Heroku. The steps taken were:

## Heroku:
- Open the "new" menu and click on "Create new app".
- Fill form fields with app name and region (Europe) depends on where are you live. Click on "Create app".
- In the "Settings" section, click on "Add buildpack" and add Python and NodeJS, in that order.
- In "Settings" section, click "convig vars" and add to Key - PORT and Value - 8000. 
- In "Deployment method", select the GitHub option and provide the repository details. Click on "Connect".
- Click on "Deploy Branch" with comprahending repository.

- The live link can be found here - https://battleships-23-b994430075a8.herokuapp.com/

## Credits:

- Inspired from youtube Learn Python with CodeCademy: Battleship! By Dylan Israel.



