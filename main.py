class player():
    player_symbol = 'YYY'
    player_name = 'John Doe'
   
def get_player_one_input(player_one,player_two):
    player_one.player_name = input('Player 1: What is your name: ')
    player_two.player_name = input('Player 2: what is your name: ')
    player_one.player_symbol = input('Player 1: Do you want to be X or O? ')
   
    while(player_one.player_symbol.lower() != 'x' and player_one.player_symbol.lower() != 'o'):
        player_one.player_symbol = input('Player 1: Do you want to be X or O? ')
    
    if player_one.player_symbol == 'X':
        player_two.player_symbol = 'O'
    else:
        player_two.player_symbol = 'X'
        
    print("Player 1 will be the first to move.", "His symbol is: ", player_one.player_symbol)
    print("Player 2 will be the second to move.", "His symbol is: ", player_two.player_symbol)
    
    if player_one.player_symbol == 'X':
        player_two.player_symbol = 'O'
    else:
        player_two.player_symbol = 'X'
    
    player_yes_no = input('Are you ready to play? ')
    if (player_yes_no.lower() == 'yes'):
        print('Let us begin')
        return player_one, player_two
    else:
        print('Let us play another time')
        break


def get_board_dimensions():
    return input('Enter the dimension of the square: ')

def build_list_of_list(dimensions):
    lst = [[' 'for j in range(dimensions)]for i in range(dimensions)]
    return lst

def print_square(gen_list, square_dimension):
    for i in range(square_dimension):
        print(gen_list[i])
        
def enter_symbol_position(gen_list, player, dimensions):
    row_position = int(input('Please Enter Position for the row in the Matrix: '))
    while(row_position > dimensions):
        row_position = int(input('Please Enter Position for the row in the Matrix: '))
    column_position = int(input('Please Enter Position for the column in the Matrix: '))
    while(column_position > dimensions):
        column_position = int(input('Please Enter Position for the column in the Matrix: '))
    #check if not filled
    if (gen_list[row_position][column_position] == ' '):
        gen_list[row_position][column_position] = player.player_symbol
        print_square(gen_list, dimensions)
        return gen_list
    
def get_column(matrix, column_num, dimensions):
    l = []
    for i in range(dimensions):
        l.append(matrix[i][column_num])
    return l
def get_diag(matrix, dimensions):
    return [matrix[i][i] for i in range(dimensions)]
def get_rev_diag(matrix, dimensions):
    counter = dimensions
    l = []
    for i in range(dimensions):
        counter = counter -1
        l.append(matrix[i][counter])
    return l

def check_list(testing_list):
    testing_list = iter(testing_list)
    try:
        first = next(testing_list)
    except StopIteration:
        return True
    return all(first == rest for rest in testing_list)

def win_condition_check(gen_list, square_dimension):
    #get columns of the list and check 
    list_columns = []
    for i in range(square_dimension):
        if check_list(get_column(gen_list, i,square_dimension)) == True:
            print('There is a win condition.')
            return True
    #get rows and check
    for i in range(square_dimension):
        if check_list(gen_list[i]) == True:
            print('There is a win condition.')
            return True
    #get diag and rev diag:
    if check_list(get_diag(gen_list, square_dimension)) == True:
        print('There is a win condition.')
        return True
    if checK_list(get_rev_diag(gen_list, square_dimension)) == True:
        print('There is a win condition.')
        return True
    
def print_intro():
    print('Welcome to Tic Tac Toe!', '\n')
    l = [[1,2,3],[4,5,6],[7,8,9]]
    print('This is the sample Board with the locations for X or O')
    print_square(l,3)
    print('\n')
    
def main():
    player_one = player()
    player_two = player()
    player_one, player_two = get_player_one_input(player_one,player_two)
    square_dimension = int(get_board_dimensions())
    gen_list = build_list_of_list(square_dimension)
    print_square(gen_list, square_dimension)
    for i in range(0, square_dimension**2):
        print('This is turn: ', i+1)
        if (i % 2 == 0):
            print('It is your turn: ', player_one.player_name)
            gen_list = enter_symbol_position(gen_list, player_one,square_dimension)
        else:
            print('It is your turn: ', player_two.player_name)
            gen_list = enter_symbol_position(gen_list, player_two,square_dimension)
        if i > 3:
            if win_condition_check(gen_list,square_dimension) == True:
                print('Game Over !!')
                break
                            
if __name__ == "__main__":
    main()
    
