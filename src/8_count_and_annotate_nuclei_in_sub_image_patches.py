import argparse
from utils import path_utils
from mirzaevinom_nuclei_segmenter import predict

def output_predictions(case_id_path, output_diretory_path):
    predict.predict_and_output_results(case_id_path, output_diretory_path)



parser = argparse.ArgumentParser(description="Counting the nuclei in the sub image patches")
parser.add_argument("-i", "--input_folder_path", type=str, help="The path to the input folder.", required=True)
parser.add_argument("-o", "--output_folder_path", type=str, help="The path to the output folder."
                                                                 " If output folder doesn't exists at runtime "
                                                                 "the script will create it.",
                    required=True)
args = parser.parse_args()

input_folder_path = args.input_folder_path
output_folder_path = args.output_folder_path

path_utils.halt_script_if_path_does_not_exist(input_folder_path)
path_utils.create_directory_if_directory_does_not_exist_at_path(output_folder_path)
case_directory_paths = path_utils.create_full_paths_to_directories_in_directory_path(input_folder_path)

for case_directory_path in case_directory_paths:
    case_id = case_directory_path.split('/')[-1]
    case_id_output_path = output_folder_path + "/" + case_id
    path_utils.create_directory_if_directory_does_not_exist_at_path(case_id_output_path)

    output_predictions(case_directory_path + "/", case_id_output_path)

