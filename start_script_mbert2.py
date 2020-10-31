import subprocess


def run():
    subprocess.call(["python", "incremental_learning.py",
                     "--train_data_path", "../data/croatian/cro_train.tsv",
                    "--test_data_path", "../data/croatian/cro_internal_test.tsv",
                     "--eval_data_path", "../data/croatian/cro_val.tsv",
                     "--output_dir", "../models/mbert_croatian1",
                     "--data_column", "text_a",
                     "--label_column", "label",
                     "--config_file", "../models/mbert_en_finetune/config.json",
                     "--model_file", "../models/mbert_en_finetune/pytorch_model.bin",
                     "--random_seed", "42"])
    subprocess.call(["python", "incremental_learning.py",
                     "--train_data_path", "../data/slovenian/slo_train_binarized.tsv",
                    "--test_data_path", "../data/slovenian/slo_internal_test_binarized.tsv",
                     "--eval_data_path", "../data/slovenian/slo_val_binarized.tsv",
                     "--output_dir", "../models/mbert_slovenian1",
                     "--data_column", "data",
                     "--label_column", "label",
                     "--config_file", "../models/mbert_en_finetune/config.json",
                     "--model_file", "../models/mbert_en_finetune/pytorch_model.bin",
                     "--random_seed", "42"])
    subprocess.call(["python", "incremental_learning.py",
                     "--train_data_path", "../data/croatian/cro_train.tsv",
                    "--test_data_path", "../data/croatian/cro_internal_test.tsv",
                     "--eval_data_path", "../data/croatian/cro_val.tsv",
                     "--output_dir", "../models/mbert_croatian2",
                     "--data_column", "text_a",
                     "--label_column", "label",
                     "--config_file", "../models/mbert_en_finetune/config.json",
                     "--model_file", "../models/mbert_en_finetune/pytorch_model.bin",
                     "--random_seed", "84"])
    subprocess.call(["python", "incremental_learning.py",
                     "--train_data_path", "../data/slovenian/slo_train_binarized.tsv",
                    "--test_data_path", "../data/slovenian/slo_internal_test_binarized.tsv",
                     "--eval_data_path", "../data/slovenian/slo_val_binarized.tsv",
                     "--output_dir", "../models/mbert_slovenian2",
                     "--data_column", "data",
                     "--label_column", "label",
                     "--config_file", "../models/mbert_en_finetune/config.json",
                     "--model_file", "../models/mbert_en_finetune/pytorch_model.bin",
                     "--random_seed", "84"])
    subprocess.call(["python", "incremental_learning.py",
                     "--train_data_path", "../data/croatian/cro_train.tsv",
                    "--test_data_path", "../data/croatian/cro_internal_test.tsv",
                     "--eval_data_path", "../data/croatian/cro_val.tsv",
                     "--output_dir", "../models/mbert_croatian3",
                     "--data_column", "text_a",
                     "--label_column", "label",
                     "--config_file", "../models/mbert_en_finetune/config.json",
                     "--model_file", "../models/mbert_en_finetune/pytorch_model.bin",
                     "--random_seed", "126"])
    subprocess.call(["python", "incremental_learning.py",
                     "--train_data_path", "../data/slovenian/slo_train_binarized.tsv",
                    "--test_data_path", "../data/slovenian/slo_internal_test_binarized.tsv",
                     "--eval_data_path", "../data/slovenian/slo_val_binarized.tsv",
                     "--output_dir", "../models/mbert_slovenian3",
                     "--data_column", "data",
                     "--label_column", "label",
                     "--config_file", "../models/mbert_en_finetune/config.json",
                     "--model_file", "../models/mbert_en_finetune/pytorch_model.bin",
                     "--random_seed", "126"])


if __name__ == "__main__":
    run()