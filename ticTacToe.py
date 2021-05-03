def printBoard(board):
    print(board['LT'] +' | '+board['MT']+' | '+board['RT'])
    print('--+---+--')
    print(board['LM'] +' | '+board['MM']+' | '+board['RM'])
    print('--+---+--')
    print(board['LL'] +' | '+board['ML']+' | '+board['RL'])




theBoard={'LT':' ','MT':' ','RT':' ',
'LM':' ','MM':' ','RM':' ',
'LL':' ','ML':' ','RL':' '
}

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('turn for '+ turn + '.Move on which space?')
    move=input()
    theBoard[move]=turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'
printBoard(theBoard)
