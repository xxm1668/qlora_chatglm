from datasets import load_dataset

data = dataset = load_dataset("json", data_files="./data/estate_qa.json")
print(data)


def format_example(examples):  # support question with a single answer or multiple answers
    examples2 = {}
    prefix = ''
    if examples["instruction"] and examples["output"]:
        query, answer = examples["instruction"], examples["output"]
        if examples["input"]:
            query += examples["input"]
        if examples["history"]:
            prompt = ""
            history = examples["history"]
            for j, (old_query, response) in enumerate(history):
                prompt += "[Round {}]\n问：{}\n答：{}\n".format(j, old_query, response)
            prompt += "[Round {}]\n问：{}\n答：".format(len(history), query)
        else:
            prompt = query
        prompt = prefix + prompt
        examples2['instruction'] = prompt
        examples2["input"] = ''
        examples2["output"] = answer
    return examples2


examples2 = {'instruction': '谢谢！非常好', 'input': '', 'output': '', 'history': [
    ['清荷园北园能买吗？是什么学校，未来有发展空间吗？孩子准备上学了',
     '是清荷园安置房，学区是清润小学和莲花实验中学，这个学校基本都是附近安置房的学区。\n安置房后期升值空间有限，不过如果资金较为紧缺的话，又想住在建邺区的话，自住也是没什么问题的。\n但是如果可以的话，还是比较建议您买其他区域的商品房']]}
format_example(examples2)