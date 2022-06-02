# for loading files from the file system

import os
from result import Ok, Err, Result


# return a list of object
def load_data(path) -> Result[list, str]:
    datasets = []
    try:
        for author_name in os.listdir(path):
            author_path = path + author_name + '/'
            author_documents = {"name": author_name, "documents": []}
            for file_name in os.listdir(author_path):
                file_path = author_path + file_name
                with open(file_path, 'r') as f:
                    author_documents["documents"].append(f.read())
            datasets.append(author_documents)
    except:
        return Err("Error: cannot load data from the file system")
    return Ok(datasets)


# return a list of object
def load_data_from_path(path) -> Result[str, str]:
    try:
        with open(path, 'r') as f:
            return Ok(f.read())
    except:
        return Err("Error: cannot load data from the file system")


def loaded_datasets_to_list_of_name(loaded_datasets) -> Result[list, str]:
    list_of_name = list(map(lambda x: x["name"], loaded_datasets))
    return Ok(list_of_name)


def get_file_number(path) -> int:
    file_number = 0
    for _, _, files in os.walk(path):
        file_number += len(files)

    return file_number
