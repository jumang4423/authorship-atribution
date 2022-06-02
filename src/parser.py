# for calculating cosine similarity between two dictionaries

from result import Ok, Result
import numpy as np


# glocal variables
train_dict_sorted_by_count = []


def calc_weight(test_dict_sorted_by_count: list[str], train_dict_sorted_by_count_pointer: list[str], key: str) -> Result[float, str]:
    # calculate the given key rank by sorting the count
    key_rank_test = 1
    key_rank_train = 1
    for key_train in train_dict_sorted_by_count_pointer:
        if key == key_train:
            break
        key_rank_train += 1

    # calculate the given key rank by sorting the count
    for key_test in test_dict_sorted_by_count:
        if key == key_test:
            break
        key_rank_test += 1

    return Ok(key_rank_train / key_rank_test)


# returns a list of keys from a dictionary
def cosine_similarity(train_dict: dict,  test_dict: dict) -> Result[float, str]:
    global train_dict_sorted_by_count
    d1_count_list: list[float] = []
    d2_count_list: list[float] = []

    # calc ranking for each word
    test_dict_sorted_by_count: list[str] = sorted(test_dict.keys(), key=lambda x: test_dict[x], reverse=True)
    if len(train_dict_sorted_by_count) == 0:
        train_dict_sorted_by_count = sorted(train_dict.keys(), key=lambda x: train_dict[x], reverse=True)

    # calculating the count of each word in the training dictionary
    for key in test_dict.keys():
        weight = calc_weight(test_dict_sorted_by_count, train_dict_sorted_by_count, key).unwrap()
        d1_count_list.append(test_dict[key] * weight)
        if key in train_dict:
            d2_count_list.append(train_dict[key])
        else:
            d2_count_list.append(0)

    # calculating cosine similarity
    return Ok(np.dot(d1_count_list, d2_count_list) / (np.linalg.norm(d1_count_list) * np.linalg.norm(d2_count_list)))
