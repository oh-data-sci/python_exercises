"""
from: https://github.com/Kremzeeq/mastermind/blob/master/src/main.py
Mastermind: A Game of Numbers

This Mastermind game invites a player to guess digits for a randomly generated number
in the command line.
There are 3 modes of difficulty:
Easy and Medium mode: The player has to keep typing 4 digits until they guess the number.
Easy mode provides hints as to how many digits are correct, but not their position.
At the end of the game the player is informed about how many tries it took.
Hard Mode: Again, no hints and the player has to guess a 5 digit number.
At the end of the game, scores are logged in a CSV and the player is shown the
highest score for the respective game mode they played.
"""


from collections import Counter
import pandas as pd
import numpy as np
import logging
import re
import os

logger = logging.Logger('catch_all')


class MastermindGame:
    def __init__(self):
        self.guesses = 1
        self.playing = True
        self.game_mode_dict = {"e": "easy", "n": "normal", "h": "hard"}

    def execute(self):
        self.get_welcome_message()
        game_mode = self.get_game_mode()
        rand_num = self.get_code_for_game_mode(game_mode)
        self.start_game(game_mode, rand_num)
        self.end_game(game_mode, "mastermind_scores.csv")

    def get_welcome_message(self):
        print("Welcome to Mastermind! \nCan you crack the code?")
        print("\nThere are 3 modes")
        print("Easy mode: You enter a 4-digit number. If you guess wrong, "
              "the game will hint how many numbers were right")
        print("Medium mode: You enter a 4-digit number. No hints!")
        print("Hard mode: You enter a 5-digit number. No hints!")

    def get_game_mode(self):
        choosing_mode = True
        regex = re.compile(r'[enh]')
        game_mode = None
        while choosing_mode:
            game_mode = input("\nPlease choose a mode: Easy (E), Normal (N) or Hard (H): ").lower()
            if len(game_mode) == 1:
                if regex.match(game_mode):
                    choosing_mode = False
        print("You chose the game mode: {}".format(self.game_mode_dict[game_mode]))
        return game_mode

    def get_code_for_no_of_digits(self, num_of_digits):
        last_num = num_of_digits*"9"
        rand_num = str(np.random.randint(0, int(last_num)))
        str_len = num_of_digits - len(rand_num)
        rand_num = str(str_len*"0")+rand_num
        return rand_num

    def get_code_for_game_mode(self, game_mode):
        if game_mode == 'e' or game_mode == 'n':
            return self.get_code_for_no_of_digits(4)
        else:
            return self.get_code_for_no_of_digits(5)

    def start_game(self, game_mode, rand_num):
        while self.playing:
            player_guess = input("Please enter guess: ")
            self.validate_guess(player_guess, game_mode, rand_num)

    def validate_guess(self, player_guess, game_mode, rand_num):
        if player_guess == rand_num:
            print("Congratulations, you guessed the number in {} guesses".format(self.guesses))
            self.playing = False
            return {'success': True, 'result': player_guess}
        elif len(player_guess) == 4 and player_guess.isdigit():
            if game_mode == "e":
                self.give_easy_mode_hint(player_guess, rand_num)
            print("Please guess again!")
            self.guesses += 1
        else:
            print("Please ensure to enter correct number of digits")
        return {'success': False, 'result': player_guess}

    def give_easy_mode_hint(self, player_guess, rand_num):
        rand_num_dict = Counter(rand_num)
        for c, x in enumerate(player_guess):
            if player_guess[c] in rand_num_dict.keys():
                if rand_num_dict[x] > 0:
                    rand_num_dict[x] -= 1
        sum_of_dict_vals = sum(rand_num_dict.values())
        if sum_of_dict_vals in range(1, 5):
            nums_found = 4 - sum_of_dict_vals
            print("You guessed {} correct digit(s)".format(nums_found))
        elif sum_of_dict_vals == 0:
            print("You guessed all the correct digits. Now just get the order right!")
        else:
            print("No digits in code!")
        return sum(rand_num_dict.values())

    def write_game_details_to_file(self, game_mode, scores_csv):
        player_name = input("Please enter your name. \nThis will be kept in a score table: ")
        entry = "{},{},{}\n".format(player_name, self.guesses, game_mode)
        try:
            if os.path.isfile(scores_csv):
                with open(scores_csv, "a") as scores_file:
                    scores_file.write(entry)
            else:
                with open(scores_csv, "w") as scores_file:
                    scores_file.write("player name,guesses,game mode\n")
                    scores_file.write("{}".format(entry))
        except Exception as e:
            logger.error(e, exc_info=True)

    def show_high_score_for_game_mode(self, game_mode, scores_csv):
        try:
            df = pd.read_csv(scores_csv)
            game_mode_df = df[df["game mode"] == game_mode]
            highest_score = game_mode_df["guesses"].min()
            highest_score_df = game_mode_df[game_mode_df["guesses"] == highest_score]
            print("\nHighest scores for {} game mode:".format(self.game_mode_dict[game_mode]))
            print(highest_score_df)
        except Exception as e:
            logger.error(e, exc_info=True)

    def end_game(self, game_mode, scores_csv):
        self.write_game_details_to_file(game_mode, scores_csv)
        self.show_high_score_for_game_mode(game_mode, scores_csv)


mastermind_game = MastermindGame()
mastermind_game.execute()
