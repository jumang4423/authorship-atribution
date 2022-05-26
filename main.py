# Problem, is to identify the actual author of a text from ten candidate authors Write a program that measures the
# cosine similarity (or another measure) for the training set and then uses the result to identify the author of the
# test set. The program should provide numerical results for all TEN test sets against all TEN authors. Finally,
# the program names the most likely author for each test set. This may be in the form of a probability statement,
# e.g. XXX is most likely the author (90%).

import file_loader
import yaml
from result import Ok, Result, Err
import lexer, parser


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
    new_word_list: list[str] = lexer.remove_char_from_word(test_data_str)
    new_dict = lexer.gen_dict_from_word_list(new_word_list)

    return Ok(new_dict)


def config_loader() -> Result[dict, str]:
    try:
        with open('config.yml', 'r') as file:
            return Ok(yaml.load(file, Loader=yaml.FullLoader))
    except Exception as e:
        return Err(str(e))


def main():
    # load settings
    settings_obj = config_loader().unwrap()
    datasets_path = settings_obj['datasets_path']
    test_data_path = settings_obj['test_data']['file_path']
    test_author_name = settings_obj['test_data']['author_name']

    # load text
    trained_data_list_dict = prepare_training_arr_dict(datasets_path).unwrap()
    test_data_dict = prepare_test_dict(test_data_path).unwrap()

    # calculate cosine similarity
    cosine_similarity_list_dict = []
    for author_dict in trained_data_list_dict:
        cosine_similarity_list_dict.append({'name': author_dict['name'],
                                            'cosine_similarity': parser.cosine_similarity(author_dict['dict'],
                                                                                          test_data_dict).unwrap()})

    # sort by cosine similarity
    sorted_cosine_similarity_list_dict = sorted(cosine_similarity_list_dict, key=lambda k: k['cosine_similarity'],
                                                reverse=True)

    # print result who is most likely
    print("-o expected author: " + test_author_name)
    print("-o most likely author: " + sorted_cosine_similarity_list_dict[0]['name'])


if __name__ == '__main__':
    main()
