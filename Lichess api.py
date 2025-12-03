import requests

api=input("lichess api")
move=input("move in uci format")
requests.post(
    "https://lichess.org/api/board/game/5IrD6Gzz/move/",move,
    headers={
      "Authorization": api
    },
    params={
      "offeringDraw": "false"
    }

)
