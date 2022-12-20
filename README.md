# call_API

APIを呼び出すためのコード

## 使い方
本ディレクトリ上で次のコマンドを入力することによりパッケージがインストールされる．

```sh
pip install .
```


### API呼び出し

```call_API/__main__.py``` にコマンドラインから試しに実行するためのコード．
なお，コマンドラインからは下記のとおりに実行すると情報取得を表示．
※現状，コマンドラインに辞書型を渡せなくて--queryだけdefaultの値で実行

```sh
python3 -m call_API --url <呼び出したいURL，'https://xxxx'> --apikey <APIKey(入力がなければNone)> --query <クエリ，{'key1':'value1'}のように>
```

### 実装
CallAPI を継承した新規クラスを作成する．