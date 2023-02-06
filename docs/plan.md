## Work plan

### Game module:
1. Service: parse a 2d grid as input. Provide methods to get/set cell value
3. Service: create a service to evaluate 2D grid on winning condition


### Backend:
1. Store game object in database
2. Create a new game, provide a permanent link to the game


### API Schema:
1. POST /game - Create a new game
2. GET /game/:id - Get game setup and players
3. POST /game/:id/move - Make a move & re-evaluate game winning conditions


### Frontend
1. Starter page:
    1.1 Create a new game
    2.2 Join a game

2. Game:
    2. Load the game: 
        1.1 Game board
        1.2 Players - on opposite sides

    3. Game process:
        1.1 Highlight the current player move
        1.2 Make move on clicking a cell
        1.3 Show stats: time, moves

3. Game End:
    1.1 Block game canvas
    1.2 Show modal for both players: Winner / Draw


### Deployment:
1. Deploy backend to lambda
2. Deploy FE to S3
3. Setup github actions to deploy on push to master
