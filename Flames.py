def flames_game(player1, player2):

    player1 = player1.replace(" ", "").lower()
    player2 = player2.replace(" ", "").lower()
    

    for char in player1[:]:
        if char in player2:
            player1 = player1.replace(char, '', 1)
            player2 = player2.replace(char, '', 1)
    
  
    remaining_count = len(player1) + len(player2)
    
 
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
  
    while len(flames) > 1:
        split_index = (remaining_count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames) - 1]

    result = flames[0]
    

    status = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    
    return f'status = {status[result]}'

player1 = "alex"
player2 = "john"
print(flames_game(player1, player2))