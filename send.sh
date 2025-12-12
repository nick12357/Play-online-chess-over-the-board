read api
read move
read board_id
                ########################################################################################################################
curl "https://lichess.org/api/board/game/$board_id/move/$move?offeringDraw=false" \
  --request POST \
  --header "Authorization: Bearer $api"