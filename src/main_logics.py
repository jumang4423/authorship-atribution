# libs
import yaml
from result import Ok, Result, Err
from src import lexer, parser, file_loader

# variables for caching
trained_data_list_dict = []


# gen trained data
def gen_cached_trained_data(datasets_path: str):
    global trained_data_list_dict
    trained_data_list_dict = prepare_training_arr_dict(datasets_path).unwrap()


# Result<Array<{name: string, dict: {string: float}}>>
def prepare_training_arr_dict(datasets_path_str: str) -> Result[list[dict], str]:
    # load input datasets and test data
    input_dataset_list = file_loader.load_data(datasets_path_str).unwrap()

    # lexical analysis
    input_authors_dict: list[dict] = []

    for dataset in input_dataset_list:
        new_dict = lexer.lexical_analysis(dataset['documents']).unwrap()
        new_author_dict = ({'name': dataset["name"], 'dict': new_dict})
        # every author has different dict(mapping from word to frequency)
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


def prepare_test_dict_from_text(test_data_str: str) -> Result[dict, str]:
    # lexical analysis
    new_word_list: list[str] = lexer.remove_char_from_word(test_data_str.split())
    new_dict = lexer.gen_dict_from_word_list(new_word_list)

    return Ok(new_dict)


# load config file
def config_loader(config_path) -> Result[dict, str]:
    try:
        with open(config_path, 'r') as file:
            return Ok(yaml.load(file, Loader=yaml.FullLoader))
    except Exception as e:
        return Err(str(e))


def predict_test(datasets_path: str, test_data_path: str) -> dict:
    # load trained data but only once
    if len(trained_data_list_dict) == 0:
        gen_cached_trained_data(datasets_path)

    # load text
    test_data_dict = prepare_test_dict(test_data_path).unwrap()

    # calculate cosine similarity
    cosine_similarity_list_dict = []
    for author_dict in trained_data_list_dict:
        cosine_similarity_list_dict.append({'name': author_dict['name'],
                                            'cosine_similarity': parser.cosine_similarity(
                                                author_dict['dict'],
                                                test_data_dict).unwrap()})
    # find max cosine similarity
    predicted_author = max(cosine_similarity_list_dict, key=lambda k: k['cosine_similarity'])

    # result object
    return {
        'input_file': test_data_path,
        'predicted_author': predicted_author['name'],
        'is_prediction_correct': predicted_author['name'] in test_data_path
    }


def predict_test_from_text(datasets_path: str, plaintext: str) -> dict:
    if len(trained_data_list_dict) == 0:
        gen_cached_trained_data(datasets_path)

    # load text
    test_data_dict = prepare_test_dict_from_text(plaintext).unwrap()

    # calculate cosine similarity
    cosine_similarity_list_dict = []
    for author_dict in trained_data_list_dict:
        cosine_similarity_list_dict.append({'name': author_dict['name'],
                                            'cosine_similarity': parser.cosine_similarity(
                                                author_dict['dict'],
                                                test_data_dict).unwrap()})
    # find max cosine similarity
    predicted_author = max(cosine_similarity_list_dict, key=lambda k: k['cosine_similarity'])

    # result object
    return predicted_author['name']
