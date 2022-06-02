# for lexing the input file
import os

from result import Ok, Result


def lexical_analysis(documents) -> Result[list, str]:
    # split by whitespace
    wordArray: list[str] = split_by_whitespace(documents).unwrap()
    # add to the dict with count
    word_dict: dict = gen_dict_from_word_list(wordArray)

    return Ok(word_dict)


def split_by_whitespace(documents: list[str]) -> Result[list, str]:
    # split by whitespace
    wordArray: list[str] = []
    for document in documents:
        filtered_word_list = str_clearner(document)
        for word in filtered_word_list:
            wordArray.append(word)
    return Ok(wordArray)


def str_clearner(doc_str: str) -> list[str]:
    doc_str = doc_str \
        .replace("$", "@") \
        .replace("-", "@") \
        .replace("\"", "@") \
        .replace("\n", "@") \
        .replace(".", "@") \
        .replace(" ", "@") \
        .replace("@@", "@") \
        .lower()

    return doc_str.split("@")


def gen_dict_from_word_list(word_list: list[str]) -> dict:
    word_dict: dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict
