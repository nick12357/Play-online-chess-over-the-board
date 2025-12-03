import requests

api=input("lichess api")
move=input("move in uci format")
gameid=input("game id")
requests.post(
    "https://lichess.org/api/board/game/",gameid ,"/", move,
    headers={
      "Authorization": api
    },
    params={
      "offeringDraw": "false"
    }

)
