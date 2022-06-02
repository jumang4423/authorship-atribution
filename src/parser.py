# for calculating cosine similarity between two dictionaries

from result import Ok, Result
import numpy as np

# for caching
cached_all_dict_keys_merged = []


# returns a list of keys from all dictionaries
def list_of_keys_merged(training_dicts: list[dict], test_dict: dict) -> Result[list[str], str]:
    global cached_all_dict_keys_merged
    # collecting all keys for both dictionaries to access them
    if len(cached_all_dict_keys_merged) == 0:
        for trained_dict in training_dicts:
            for key in trained_dict.keys():
                cached_all_dict_keys_merged.append(key)

    return Ok(cached_all_dict_keys_merged + list(test_dict.keys()))


# returns a list of keys from a dictionary
def cosine_similarity(train_dict: dict,  test_dict: dict) -> Result[float, str]:
    d1_count_list: list[float] = []
    d2_count_list: list[float] = []

    # calculating the count of each word in the training dictionary
    for key in test_dict.keys():
        if key in test_dict:
            d1_count_list.append(test_dict[key])
            if key in train_dict:
                d2_count_list.append(train_dict[key])
            else:
                d2_count_list.append(0)

    # calculating cosine similarity
    return Ok(np.dot(d1_count_list, d2_count_list) / (np.linalg.norm(d1_count_list) * np.linalg.norm(d2_count_list)))
