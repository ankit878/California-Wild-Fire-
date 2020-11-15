import eazyml
import json
import csv

global username
global password
global api_key
global filepath_test
global auth_token
global dataset_id
global model_id
global prediction_dataset_id

def ez_auth():
    try:
        global auth_token
        response = eazyml.ez_auth(username, password=None, api_key = api_key)
        auth_token = response["token"]
    except Exception as e:
        print('The function ez_auth was not executed properly', e)

def ez_predict():
    try:
        global auth_token
        global model_id
        global prediction_dataset_id
        options = {}
        response = eazyml.ez_predict(auth_token, model_id, filepath_test, options)
        prediction_dataset_id = response['prediction_dataset_id']
    except Exception as e:
        print('The function ez_predict was not executed properly', e)
        
def ez_explain():
    try:
        global auth_token
        global model_id
        global prediction_dataset_id
        input_file = open(filepath_test,encoding="utf8")
        reader_file = csv.reader(input_file)
        value = len(list(reader_file))
        options = {'record_number':[i for i in range(1,value+1)]}
        response = eazyml.ez_explain(auth_token, model_id, prediction_dataset_id, options)
        return response
    except Exception as e:
        print('The function ez_explain was not executed properly', e)

if __name__ == '__main__':
    global username
    global api_key
    global filepath_test
    global model_id
    username = input("Please enter the username\n")
    api_key = input("Please enter the API KEY\n")
    filepath_test = input("Please enter the testing file path\n")
    model_id = 12449
    ez_auth()
    ez_predict()
    with open('explanation.json', 'w') as json_file:
        json.dump(ez_explain(), json_file)