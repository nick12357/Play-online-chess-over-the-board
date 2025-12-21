import berserk
import time
token=input("token")



######################################################################################################
#listifier
def uci_moves_list(moves_str:str):
    moves_str = (moves_str or "").strip()
    return moves_str.split() if moves_str else []

    






#############################################################################################################

Session = berserk.TokenSession(token)
client = berserk.Client(session=Session)
print(Session)
me = client.account.get()
print("logged in as", me.get("username"))




print("creating a public seek...")
client.board.seek(
    time=10,
    increment=2,
    rated=False
)
print("seek created waiting for opponent...")
game_id=None
for event in client.board.stream_incoming_events():
    if event.get("type") == "gameStart":
        game_id = event["game"]["id"]
        print("game started")
        print("game id: ", game_id)
        break

#game started

print("streaming game")
last_moves=[]
mycolour = None
for event in client.board.stream_game_state(game_id):
    if event.get("type") == "gameFull":
        White = event.get("white", {})
        Black = event.get("black", {})       
        if White.get("name", "") == me.get("username"):
            mycolour="White"
        else:
            mycolour="Black"
        
        moves=uci_moves_list(event.get("moves"))
        print("my colour is: ", mycolour)
        print("initial moves: ", moves)
    
    elif event.get("type") == "gameState":
        #moves are the up-to-date moves from lichess (everything happened since the beginning of the game)
        #new moves are the difference between last moves and the current state of the game
        moves=uci_moves_list(event.get("moves"))
        if len(last_moves) < len(moves):
            newmoves = moves[len(last_moves):]
            #colon means after
            for move in newmoves:
                print("newmoves are", move)
        last_moves = moves
    
    
    played = len(last_moves)

    #percent is remander
    if mycolour == "White":
        is_myturn = (played % 2 == 0)
    else:
        is_myturn = (played % 2 == 1)
    print("my turn: ", is_myturn)

    if is_myturn:
        userinput=input("make a move in uci format: ")
        client.board.make_move(game_id,userinput)






 
                






    










