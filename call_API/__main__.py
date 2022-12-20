from . import CallAPI
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--apikey', type=str, default=None)
    parser.add_argument('--query', type=dict, default={'lat': '43.0620','lon': '141.3544'})
    args = parser.parse_args()


    call_api = CallAPI(url=args.url, apikey=args.apikey, query=args.query)
    status_code = call_api.get_status_code()
    if status_code == 200:
        print('Succesed!')
        print(call_api.get_json_data())
    else:
        print('Failed: status code is', status_code)
        print('Error code:', call_api.get_error_code())
