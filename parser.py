# for calculating cosine similarity between two dictionaries

from result import Ok, Result
import numpy as np


def list_of_keys_merged(d1: dict, d2: dict) -> Result[list[str], str]:
    # collecting all keys for both dictionaries to access them
    all_dict_keys_merged: list[str] = []
    for key in d1.keys():
        all_dict_keys_merged.append(key)
    for key in d2.keys():
        all_dict_keys_merged.append(key)

    return Ok(all_dict_keys_merged)


def cosine_similarity(d1: dict, d2: dict) -> Result[float, str]:
    list_of_keys = list_of_keys_merged(d1, d2).unwrap()

    if len(list_of_keys) == 0:
        return Result.err("List of keys is empty")
    d1_count_list: list[float] = []
    d2_count_list: list[float] = []
    for key in list_of_keys:
        if key in d1:
            d1_count_list.append(d1[key])
        else:
            d1_count_list.append(0)

        if key in d2:
            d2_count_list.append(d2[key])
        else:
            d2_count_list.append(0)

    return Ok(np.dot(d1_count_list, d2_count_list) / (np.linalg.norm(d1_count_list) * np.linalg.norm(d2_count_list)))
