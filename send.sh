read -p "whats the api key" api
read -p "whats your move" move
read -p "whats the board id" board_id

                ########################################################################################################################
curl "https://lichess.org/api/board/game/$board_id/move/$move?offeringDraw=false" \
  --request POST \
  --header "Authorization: Bearer $api"