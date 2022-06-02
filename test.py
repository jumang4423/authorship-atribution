import os

import file_loader
import yaml
from result import Ok, Result, Err
import lexer, parser

# variables for caching
trained_data_list_dict = []
dict_array = []
config_file_path = "./config.yml"


def gen_cached_trained_data(datasets_path: str):
    global trained_data_list_dict, dict_array
    trained_data_list_dict = prepare_training_arr_dict(datasets_path).unwrap()
    for trained_data_dict in trained_data_list_dict:
        dict_array.append(trained_data_dict['dict'])


# Result<Array<{name: string, dict: {string: float}}>>
def prepare_training_arr_dict(datasets_path_str: str) -> Result[list[dict], str]:
    # load input datasets and test data
    input_dataset_list = file_loader.load_data(datasets_path_str).unwrap()

    # lexical analysis
    input_authors_dict: list[dict] = []

    for dataset in input_dataset_list:
        new_dict = lexer.lexical_analysis(dataset['documents']).unwrap()
        new_author_dict = ({'name': dataset["name"], 'dict': new_dict})
        input_authors_dict.append(new_author_dict)

    return Ok(input_authors_dict)


# Result<{string: float}>
def prepare_test_dict(testFilePath: str) -> Result[dict, str]:
    # load input datasets and test data
    test_data_str = file_loader.load_data_from_path(testFilePath).unwrap()

    # lexical analysis
    new_word_list: list[str] = lexer.remove_char_from_word(test_data_str.split())
    new_dict = lexer.gen_dict_from_word_list(new_word_list)

    return Ok(new_dict)


def config_loader() -> Result[dict, str]:
    global config_file_path
    try:
        with open(config_file_path, 'r') as file:
            return Ok(yaml.load(file, Loader=yaml.FullLoader))
    except Exception as e:
        return Err(str(e))


def predict_test(datasets_path: str, test_data_path: str) -> dict:
    if len(trained_data_list_dict) == 0:
        gen_cached_trained_data(datasets_path)

    # load text
    test_data_dict = prepare_test_dict(test_data_path).unwrap()

    # calculate cosine similarity
    cosine_similarity_list_dict = []
    for author_dict in trained_data_list_dict:
        cosine_similarity_list_dict.append({'name': author_dict['name'],
                                            'cosine_similarity': parser.cosine_similarity(dict_array,
                                                                                          author_dict['dict'],
                                                                                          test_data_dict).unwrap()})

    # find max cosine similarity
    predicted_author = max(cosine_similarity_list_dict, key=lambda k: k['cosine_similarity'])

    return {
        'input_file': test_data_path,
        'predicted_author': predicted_author['name'],
        'is_prediction_correct': predicted_author['name'] in test_data_path
    }


def main():
    # load settings
    settings_obj = config_loader().unwrap()
    datasets_path = settings_obj['datasets_path']
    test_data_path = settings_obj['test_data_dir']

    # predict
    print()
    print("-o dataset_path: " + datasets_path)
    print("-o test_data_path: " + test_data_path)
    print()

    # get all files
    test_count = 0
    coverage_count = 0
    file_number = file_loader.get_file_number(test_data_path)

    for root, dirs, files in os.walk(test_data_path):
        for file in files:
            result_dict = predict_test(datasets_path, os.path.join(root, file))
            test_count += 1

            # if input_file includes most_similar_author, coverage_count + 1
            if result_dict['predicted_author'] in result_dict['input_file']:
                coverage_count += 1

            # print result
            print(str(int(test_count / file_number * 100)) + "%:\t" + str(result_dict))

    # print coverage
    print()
    print("-o test coverage: " + str((coverage_count / test_count) * 100) + "%")
    print()


if __name__ == '__main__':
    main()
