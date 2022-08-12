"""
Create a program that:

1.) Given a string that may contain numbers larger than 999...

2.) Produce a new string that has inserted commas (or underscores ("_")) as
    necessary to make the numbers easier to read.

Example 1:
Given String: "There are 1000 cars in the parking lot. 35000 in the parking lot next door."
Output: "There are 1,000 cars in the parking lot. 35,000 in the parking lot next door."

Example 2:
Given String: "100 2500 35 26000 8000000 7542"
Output: "100 2,500 35 26,000 8,000,000 7,542"

or if the given delimiter is "_":

Output: "100 2_500 35 26_000 8_000_000 7_542"

Constraints:
Any numbers in the strings will be positive whole numbers.

"""


def add_delimiter(s: str, d: str = ',') -> str:
    """In numbers greater than 999, delimiters are added every third digit from the right."""

    # 1.)   Ensure that the delimiter is either ',' or '_'. If not,
    #       raise an exception.
    if (d != ",") and (d != "_"):
        raise Exception("Invalid delimiter. Must be ',' or '_'.")

    # 2.)   Split the string into a list of words
    word_list = s.split()

    # 3.)   Iterate through the list, and if the word is a valid number
    #       (<str>.isdecimal() tells us this), format the word to have
    #       the appropriate delimiter.
    for i, val in enumerate(word_list):
        if val.isdecimal() and d == ",":
            word_list[i] = f"{int(val):,}"
        elif val.isdecimal() and d == "_":
            word_list[i] = f"{int(val):_}"

    # 4.)   Now all the words/numbers should be formatted, but they're still
    #       in a list. Make a new string <final_sentence>, and then fill it with
    #       the words from the list.
    final_sentence = ""

    for val in word_list:
        final_sentence = final_sentence + val + " "

    # 5.)   Remove any trailing whitespace.
    final_sentence = final_sentence.rstrip()

    return final_sentence


def main() -> None:
    test_string = "100 2500 35 26000 8000000 7542"
    value = add_delimiter(test_string, ",")

    print("value: ", value)


if __name__ == '__main__':
    main()
