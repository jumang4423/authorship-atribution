# for calculating cosine similarity between two dictionaries

from result import Ok, Result
import numpy as np


def list_of_keys_merged(training_dicts: list[dict], test_dict: dict) -> Result[list[str], str]:
    # collecting all keys for both dictionaries to access them
    all_dict_keys_merged: list[str] = []
    for trained_dict in training_dicts:
        for key in trained_dict.keys():
            all_dict_keys_merged.append(key)
    for key in test_dict.keys():
        all_dict_keys_merged.append(key)

    return Ok(all_dict_keys_merged)


def cosine_similarity(trained_dicts: list[dict], train_dict: dict,  test_dict: dict) -> Result[float, str]:
    list_of_keys = list_of_keys_merged(trained_dicts, test_dict).unwrap()

    if len(list_of_keys) == 0:
        return Result.err("List of keys is empty")
    d1_count_list: list[float] = []
    d2_count_list: list[float] = []
    for key in list_of_keys:
        if key in train_dict:
            d1_count_list.append(train_dict[key])
        else:
            d1_count_list.append(0)

        if key in test_dict:
            d2_count_list.append(test_dict[key])
        else:
            d2_count_list.append(0)

    return Ok(np.dot(d1_count_list, d2_count_list) / (np.linalg.norm(d1_count_list) * np.linalg.norm(d2_count_list)))
