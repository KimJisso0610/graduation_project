import numpy as np
import pandas as pd


class Loss:

    def __init__(self, country, model, data):
        self.country = country
        self.model = model
        self.data = data


def get_data(file_path):
    loss_dict_list = []
    with open(file_path, 'r') as file:
        for line in file:
            loss_dict = eval(line.strip())
            loss_dict_list.append(loss_dict)
    return loss_dict_list


def get_loss_dict():
    global loss_list
    global country_set
    global model_set
    for i in range(0, len(loss_dict_list), 4):
        loss_with_k = loss_dict_list[i:i + 4]
        country = ''
        model = ''
        for temp_elem in loss_with_k[0].keys():
            country = eval(temp_elem)['country'][:-4]
            model = eval(temp_elem)['model name']
        temp_list = []
        for elem in loss_with_k:
            for v in elem.values():
                temp_list.append(v)

        # print(country, model, sum(loss_list) / 4)
        loss = Loss(country, model, sum(temp_list) / 4)
        loss_list.append(loss)

        if country not in country_set:
            country_set.append(country)

        if model not in model_set:
            model_set.append(model)


def get_df_dict(loss_list, model_set):
    df_dict = {}
    for model in model_set:
        df_dict[model] = []
    for loss in loss_list:
        value = loss.data
        df_dict[loss.model].append(value)

    for key in df_dict.keys():
        value = df_dict[key]
        average = np.array(value).mean()
        df_dict[key].append(average)

    return df_dict


if __name__ == '__main__':
    path = './loss_log.txt'
    loss_dict_list = get_data(path)
    loss_list = []
    country_set = []
    model_set = []
    get_loss_dict()
    country_set += ['Average']
    df_dict = get_df_dict(loss_list, model_set)
    df = pd.DataFrame(df_dict, index=country_set)
    print(df)
    df.to_csv('./model_loss.csv')

