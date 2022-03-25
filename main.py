import os
import random
import words

TITLE = 'WORDLE'
NL = '\n'


class Game:
        
    def setup_game(self): # reset everything and generate word
            self.word = random.choice(words.list)
            self.game_ended = False
            self.tries = ['','','','','']
            self.in_place = ['','','','','']
            self.in_place_nr = 0
            self.in_word = ['','','','','']
            self.not_in_word = []
            self.try_nr = 0
            self.status = ''
            self.main()
            
    def print_board(self): # main screen
        os.system('cls')
        print(TITLE)
        print(2*NL)
        if len(self.not_in_word) > 0:
            print('Not in word: ' + str(self.not_in_word))
        print(NL)
        for _try in self.tries: # print all tried words
            if _try != '':
                if len(self.in_word[self.tries.index(_try)]) > 0:
                    print(_try + ' |', end = ' ')
                    print('in word: [' + self.in_word[self.tries.index(_try)], end = ']; ') # letters in word
                    print('in place: [' + self.in_place[self.tries.index(_try)] + ']') # letters in place
                else:
                    print(_try) # if neither in word nor in place just print the word normally
        if self.status != '':
            print(NL)
            print(self.status)
        print(NL)
        print('Your guess: ')
        
    def print_win_board(self):
            os.system('cls')
            print(TITLE)
            print(3*NL)
            print('You won! The word was ' + self.word + ' and you made it in ' + str(self.try_nr) + ' tries!')
            print('Play Again? Type "y"')
            input_play_again = input()
            if input_play_again == 'y' or input_play_again == 'Y':
                self.setup_game()
    
    def print_loss_board(self):
            os.system('cls')
            print(TITLE)
            print(3*NL)
            print('You lost! The word was ' + self.word)
            print('Play Again? Type "y"')
            input_play_again = input()
            if input_play_again == 'y' or input_play_again == 'Y':
                self.setup_game()
    
    def main(self):
        while not self.game_ended:
            
            self.print_board()
            self.curr_try = input().lower() # lowercase input for comparing
            
            if (len(self.curr_try) != 5) or self.curr_try not in words.list:
                self.status = 'Invalid input' 
            else:
                self.tries[self.try_nr] = self.curr_try # add tried word to list
                for i in range(5):
                    if self.curr_try[i] in self.word and self.curr_try[i] not in self.in_word[self.try_nr]: # check if letter in word and avoid duplicate
                        self.in_word[self.try_nr] += ' ' + self.curr_try[i] + ' ' # add letter to in_word
                    else:
                        if self.curr_try[i] not in self.not_in_word: # avoid duplicates
                            self.not_in_word.append(self.curr_try[i]) # add to not in word list
                    if self.curr_try[i] == self.word[i]: # check if letter at the same place in word
                        self.in_place[self.try_nr] += ' ' + self.curr_try[i] + ' ' # add letter to in_list
                self.try_nr += 1
                self.status = '' # no error message/status because successful
                    
            if self.curr_try == self.word: # if word guessed
                won = True
                self.game_ended = True
            elif self.try_nr >= len(self.tries): # if all tries used
                won = False
                self.game_ended = True

        if self.game_ended:
            if won:
                self.print_win_board()
            else:
                self.print_loss_board()

if __name__ == '__main__':
    Game().setup_game()