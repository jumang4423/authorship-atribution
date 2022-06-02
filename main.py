# libs
import os
from src import main_logics, file_loader

# global variables
config_file_path = "./config.yml"


def main():
    # load settings
    settings_obj = main_logics.config_loader(config_file_path).unwrap()
    datasets_path = settings_obj['datasets_path']

    # print the prediction
    input_doc = input()
    print(main_logics.predict_test_from_text(datasets_path, input_doc))


if __name__ == '__main__':
    main()
