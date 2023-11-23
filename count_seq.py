# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 11/22/2023
# Description: Generator function that goes on indefinitely and doesn't take arguments, only generates a sequence that
# starts like: 2, 12, 1112, 3112, 132112

def count_seq():
    """
    Function that creates a sequence, starting at 2, based on counting the digits in the previous term
    """
    # initialize string with the first term
    current_term = "2"
    yield current_term

    while True:
        # initiate infinite loop, initialize count to 1 and an empty string to start building the sequence
        count = 1
        next_term = ""
        for terms in range(1, len(current_term)):
            # check if current is same as the one before it
            if current_term[terms] == current_term[terms - 1]:
                count += 1
            else:
                # add the consecutive of current digit and the digit itself to the next_term then reset count to 1
                next_term += str(count) + current_term[terms - 1]
                count = 1

        # add the count of the last number
        next_term += str(count) + current_term[-1]
        # update current term for the next one
        current_term = next_term
        # new term
        yield current_term
