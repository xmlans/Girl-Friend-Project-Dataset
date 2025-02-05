from datasets import load_dataset

# 第一个框为格式，然后是输入文件名字，默认为train
dataset = load_dataset('json', data_files='train.jsonl', split='train')

print(dataset[0])

dataset.save_to_disk('processed_data')
