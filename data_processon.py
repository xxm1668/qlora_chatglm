import json

filename = r'/home/xxm/下载/qlora/data/estate_qa.json'
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        example = json.loads(line)
        content = example['output']
        if content == '':
            print(example)
