# 開発ルール

## Gitについて
### クローンする

```
git clone https://github.com/discordbot
```

### ブランチを切る

```
git branch {ブランチ名}
git checkout {ブランチ名}
```

### ステージング,コミット,プッシュする

```
git add {コミットしたいファイル}
git commit -m "{コミットメッセージ}"
git push origin {ブランチ名}
```

### コードレビュー

コードレビューを依頼する.

## herokuについて

このプロジェクトはgithubのmasterブランチにpushすることでHerokuのサーバーに自動デプロイされるようになっている.

## 必要なライブラリのインストール

### discord.py

```
pip install discord.py
```

## Tokenの扱いについて

tokenはHerokuの環境変数としてあるためosモジュールの関数で取得している.
ローカル環境でテストする際にはconfig.pyを作成しその中にtokenを記述する.
