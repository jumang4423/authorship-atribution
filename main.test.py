# libs
import os
from src import main_logics, file_loader

# global variables
config_file_path = "./config.yml"


def main():
    # load settings
    settings_obj = main_logics.config_loader(config_file_path).unwrap()
    datasets_path = settings_obj['datasets_path']
    test_data_path = settings_obj['test_data_dir']

    # start prediction
    print()
    print("-o dataset_path: " + datasets_path)
    print("-o test_data_path: " + test_data_path)
    print()

    cur_index = 0
    coverage_count = 0
    file_number = file_loader.get_file_number(test_data_path)

    # predict every test file
    for root, _, files in os.walk(test_data_path):
        for file in files:
            result_dict = main_logics.predict_test(datasets_path, os.path.join(root, file))
            cur_index += 1

            # if input_file includes most_similar_author, coverage_count + 1
            if result_dict['is_pred_ok']:
                coverage_count += 1

            # print result
            print("(c" + str(cur_index) + "/"+str(file_number)+")\t" + str(result_dict))

    # print coverage
    print()
    print("-o test coverage: " + str((coverage_count / file_number) * 100) + "%")
    print()


if __name__ == '__main__':
    main()
