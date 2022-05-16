# Problem, is to identify the actual author of a text from ten candidate authors
# Write a program that measures the cosine similarity (or another measure) for the training set and then uses the result to identify the author of the test set.
# The program should provide numerical results for all TEN test sets against all TEN authors.
# Finally, the program names the most likely author for each test set.
# This may be in the form of a probability statement, e.g. XXX is most likely the author (90%).

import os

datasets_path = './datasets/'
test_data_path = './test_data/'

# Array<{name, Array<string>}>のデータをdatasets_path及びtest_data_pathから読み込む
# datasets_path/authorname/hoge.txtというようなファイル構成になっている
def load_data(path):
    datasets = []
    for author_name in os.listdir(path):
        author_path = path + author_name + '/'
        for file_name in os.listdir(author_path):
            file_path = author_path + file_name
            with open(file_path, 'r') as f:
                datasets.append({'name': author_name, 'text': f.read()})
    return datasets


def main():
    loaded_datasets = load_data(datasets_path)
    # print loaded_datasets
    print(loaded_datasets)


if __name__ == '__main__':
    main()