"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k): # passed
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    selected_paragraphs = [p for p in paragraphs if select(p) == True]
    if len(selected_paragraphs) < k+1:
        return ''
    else:
        return selected_paragraphs[k]

    # END PROBLEM 1


def about(topic): # passed
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def select_func(str):
        processed_str = split(remove_punctuation(lower(str)))
        for t in topic:
            if any([s for s in processed_str if s == t]):
                return True
        return False
    return select_func
    # END PROBLEM 2


def accuracy(typed, reference): # passed
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if not typed:
        return 0.0
    check = [typed_words[i] for i in range(min(len(typed_words), len(reference_words))) if typed_words[i]==reference_words[i]]
    return len(check)/len(typed_words) * 100.0
    # END PROBLEM 3


def wpm(typed, elapsed): # passed
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed)/5.0) * (60.0/elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit): # passed
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    
    diff_rate = [diff_function(user_word, valid_word, limit) for valid_word in valid_words]
    # if min(diff_rate) > limit:
    #     return user_word
    min_diff_rate = diff_rate[0]
    index = 0

    for i in range(1, len(valid_words)):
        if diff_rate[i] < min_diff_rate:
            min_diff_rate = diff_rate[i]
            index = i

    if min_diff_rate > limit:
        return user_word
    else:
        return valid_words[index]
    # END PROBLEM 5


def shifty_shifts(start, goal, limit): # passed
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    assert False, "Remove this line for this diff function to be used."
    # BEGIN PROBLEM 6
    def calculate_diff(start, goal, num_of_change=0):
        if num_of_change > limit:
            return num_of_change
        if not start:
            return len(goal) + num_of_change
        if not goal:
            return len(start) + num_of_change
        if start[0] == goal[0]:
            return calculate_diff(start[1:], goal[1:], num_of_change)
        else:
            return calculate_diff(start[1:], goal[1:], num_of_change+1)
    return calculate_diff(start, goal)
    # END PROBLEM 6


def pawssible_patches(start, goal, limit): # passed
    """A diff function that computes the edit distance from START to GOAL."""
    # assert False, "Remove this line for this diff function to be used."
    def calculate_patches(start, goal, num_of_change=0):
        if num_of_change > limit:
            return num_of_change
        if not start or not goal: # add len(goal) times or delete len(start) times
            return max(len(goal), len(start)) + num_of_change
        
        if start[0] == goal[0]:
            return calculate_patches(start[1:], goal[1:], num_of_change)
        else:
            add_diff = add(start, goal, num_of_change)
            remove_diff = remove(start, goal, num_of_change)
            substitute_diff = substitute(start, goal, num_of_change)
            return min(add_diff, remove_diff, substitute_diff)

    def add(start, goal, num_of_change): # add the first char of str goal to the front of str start, with pruning
        return calculate_patches(start, goal[1:], num_of_change+1) # goal[0]+start, goal -> start, goal[1:]
    
    def remove(start, goal, num_of_change): # remove the first char of str start
        return calculate_patches(start[1:], goal, num_of_change+1)
    
    def substitute(start, goal, num_of_change): # change the first char of str start to the first element of str goal, with pruning
        return calculate_patches(start[1:], goal[1:], num_of_change+1) # goal[0]+start[1:], goal -> start[1:], goal[1:]
        
    return calculate_patches(start, goal)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send): # passed
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    i = 0
    while i < min(len(typed),len(prompt)):
        if typed[i] != prompt[i]:
            break
        i += 1
    progress = i / len(prompt)
    dict = {'id': user_id, 'progress': progress}
    send(dict)
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words): # passed
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # times = []
    # for player in times_per_player:
    #     player_times = []
    #     i = 1
    #     while i < len(player):
    #         player_times += [player[i] - player[i-1]]
    #         i += 1
    #     times += [player_times]
    times = [ [t_curr - t_prev for t_prev, t_curr in zip(player[:-1], player[1:])] for player in times_per_player] # pythonic!!!
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game): # passed
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    words = all_words(game)
    times = all_times(game)
    fast_word = [[] for player_index in player_indices]
    # for word_index in word_indices:
    #     word_times = [times[player_index][word_index] for player_index in player_indices]
    #     min_time = min(word_times)
    #     min_index = word_times.index(min_time)
    #     fast_word[min_index].append(words[word_index])

    # A much better way to implement!!! (note: enumerate, key=<list>.__get__item, append(), zip(*<list<list>>) )
    for word_index, word_time in enumerate(zip(*times)):
        fast_player_index = min(player_indices, key=word_time.__getitem__)
        fast_word[fast_player_index].append(words[word_index])
    return fast_word
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)