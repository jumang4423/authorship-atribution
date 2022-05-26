# Problem, is to identify the actual author of a text from ten candidate authors Write a program that measures the
# cosine similarity (or another measure) for the training set and then uses the result to identify the author of the
# test set. The program should provide numerical results for all TEN test sets against all TEN authors. Finally,
# the program names the most likely author for each test set. This may be in the form of a probability statement,
# e.g. XXX is most likely the author (90%).

import file_loader
import lexer

# global variables
datasets_path = './datasets/'
test_data_path = './test_data/'


def main():
    # 1. load input datasets and test data
    input_dataset_list = file_loader.load_data(datasets_path).unwrap()
    # testdata_list = file_loader.load_data(test_data_path).unwrap()

    # # 2. lexical analysis
    authors_dict: list[dict] = []
    for dataset in input_dataset_list:
        new_dict = lexer.lexical_analysis(dataset['documents']).unwrap()
        new_author_dict = ({'name': dataset["name"], 'dict': new_dict})
        authors_dict.append(new_author_dict)


if __name__ == '__main__':
    main()
