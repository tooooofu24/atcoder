# Atcoder 勉強用リポジトリ

## セットアップ

[`atcoder-tools`](https://github.com/kyuridenamida/atcoder-tools)をインストールしておく

```bash
$ pip3 install atcoder-tools
```

各種設定

```bash
$ vim ~/.atcodertools.toml
```

```toml
[codestyle]
workspace_dir='/Users/xxx/xxx/atcoder/contests'
lang='python'

[etc]
download_without_login=false
```

## 使い方

コンテストの作成

```bash
$ atcoder-tools gen {コンテストID}
```

テスト

```bash
$ atcoder-tools test
```

提出

```bash
$ atcoder-tools submit
```
