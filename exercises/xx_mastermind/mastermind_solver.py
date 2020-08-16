from collections import Counter
import itertools
import random

def hits_and_misses(guess_seq, true_seq):
    """
    computes the match score of the guessed sequence p, given the true sequence q.
    :param guess_seq: a string containing guessed sequence guessed
    :param true_seq: the target sequence
    :return: the matches, a tuple of two integers:
        num_hits: the number of correct tokens in correct places
        num_misses: the number of correct tokens at wrong place in the sequence
    """
    num_hits = sum(guess_token == true_token
               for guess_token, true_token
               in zip(guess_seq, true_seq))
    num_misses = sum((Counter(guess_seq) & Counter(true_seq)).values()) - num_hits
    return num_hits, num_misses


def brute_force_solver(allowed_symbols, secret_sequence, maximum_iterations=100, verbose=True):
    """
    plays a game of mastermind and prints the result
    :param symbols: a string containing all the allowed symbols with no delimeter (no spaces).
    :param hidden_sequence: a string containing the sequence to guess.
    :return: discovered sequence
    """
    # number of tokens in the sequence to guess:
    len_sequence = len(secret_sequence)
    # generate all possible guesses
    possible_sequences = list(itertools.product(allowed_symbols, repeat=len_sequence))
    if verbose:
        print("there are", len(possible_sequences), 'possible sequences.')

    # verify that a solution can be found.
    if tuple(secret_sequence) in possible_sequences:
        # brute force solver.
        # 1. randomly select one of the remaining possibilities as the current guess.
        # 2. compute match-score for given guess.
        # 3. remove all sequnces that match differently than the guess from list of possible sequences
        # 4. repeat until either: 1) only one possible sequence remains or 2) maximum number of iteration reached
        for _ in range(maximum_iterations):
            if len(possible_sequences) > 1:
                print(len(possible_sequences), 'possibilities remaining')
                guess_seq = random.choice(possible_sequences)
                result = hits_and_misses(secret_sequence, guess_seq)
                print('guessing:', guess_seq, 'matches:', result)
                possible_sequences = [
                    sequence
                    for sequence
                    in possible_sequences
                    if hits_and_misses(guess_seq, sequence) == result
                ]
            else:
                break

        if len(possible_sequences) != 1:
            print('failed to find solution in', maximum_iterations,
                  'narrowed it down to', len(possible_sequences), "options")
        elif verbose:
            print(possible_sequences, hits_and_misses(possible_sequences[0], secret_sequence))
    else:
        # something has gone wrong:
        #         print(secret_sequence)
        #         print(possible_sequences)
        print('error! target sequence contains',
              [symbol for symbol in secret_sequence if symbol not in allowed_symbols],
              'which is/are not among allowed tokens:', list(allowed_symbols)
              )
    return possible_sequences[0]


def test_solver(allowed_symbols, len_sequence=3):
    """
    function to test the above function and apply them for a game of mastermind.
    :param symbols: a string containing all allowed symbols, without delimeter (no spaces), and no repeats
    :param len_sequence: an integer indicating the number of symbols in the hidden sequence to guess.
    :return: the discovered solution, and the hidden sequence.
    """
    secret_sequence = ""
    for _ in range(len_sequence):
        secret_sequence += allowed_symbols[random.randint(0, len_sequence - 1)]
    print('secret:', secret_sequence)

    solution = brute_force_solver(allowed_symbols, secret_sequence)
    return solution == tuple(secret_sequence)






