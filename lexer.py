# for lexing the input file

from result import Ok, Result


def split_by_whitespace(documents: list[str]) -> Result[list, str]:
    # split by whitespace
    wordArray: list[str] = []
    for document in documents:
        # remove unnecessary chars
        for word in document.split():
            word = word.replace("\n", "")
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace("!", "")
            word = word.replace("?", "")
            word = word.replace(";", "")
            word = word.replace(":", "")
            word = word.replace("-", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("[", "")
            word = word.replace("]", "")
            word = word.replace("{", "")
            word = word.replace("}", "")
            word = word.replace("'", "")
            word = word.replace("\"", "")
            word = word.replace("‚", "")
            word = word.replace("-", "")
            # upper case to lower case
            word = word.lower()
            wordArray.append(word)
    return Ok(wordArray)


def gen_dict_from_word_list(word_list: list[str]) -> dict:
    word_dict: dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for key, value in word_dict.items():
        word_dict[key] = value / len(word_list)
    return word_dict


def lexical_analysis(documents) -> Result[list, str]:
    # split by whitespace
    wordArray: list[str] = split_by_whitespace(documents).unwrap()
    # add to the dict with count
    word_dict: dict = gen_dict_from_word_list(wordArray)

    return Ok(word_dict)
