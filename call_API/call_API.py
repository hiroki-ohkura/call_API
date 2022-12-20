import requests


class CallAPI:
    def __init__(self, url: str, apikey: str, query: dict):
        self._url = url
        self._headers = {'x-api-key': apikey}
        self._params = query
        self._data = None
    
    def get_all_data(self):
        self._data = requests.get(self._url, headers=self._headers, params=self._params)
        return self._data
    
    def get_json_data(self):
        if self._data is None:
            self._data = self.get_all_data()
        return self._data.json()
    
    def get_status_code(self):
        if self._data is None:
            self._data = self.get_all_data()
        return self._data.status_code
    
    def get_error_code(self):
        error_code = self.get_json_data()['errors']
        return error_code


# テスト用コード
if __name__ == '__main__':

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    apikey = None
    query = {'city': 130010}

    test = CallAPI(url=url, apikey=apikey, query=query)
    print(test.get_status_code())
