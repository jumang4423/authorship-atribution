# for lexing the input file

from result import Ok, Result


# remove unnecessary chars
def remove_char_from_word(word_list: list[str]) -> list[str]:
    new_word_list: list[str] = []
    for word in word_list:
        word = word.replace("\n", "")
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(";", "")
        word = word.replace(":", "")
        word = word.replace("(", "")
        word = word.replace(")", "")
        word = word.replace("[", "")
        word = word.replace("]", "")
        word = word.replace("{", "")
        word = word.replace("}", "")
        # upper case to lower case
        word = word.lower()
        new_word_list.append(word)

    return new_word_list


def split_by_whitespace(documents: list[str]) -> Result[list, str]:
    # split by whitespace
    wordArray: list[str] = []
    for document in documents:
        filtered_word_list = remove_char_from_word(document.split())
        for word in filtered_word_list:
            wordArray.append(word)
    return Ok(wordArray)


def gen_dict_from_word_list(word_list: list[str]) -> dict:
    word_dict: dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def lexical_analysis(documents) -> Result[list, str]:
    # split by whitespace
    wordArray: list[str] = split_by_whitespace(documents).unwrap()
    # add to the dict with count
    word_dict: dict = gen_dict_from_word_list(wordArray)

    return Ok(word_dict)
