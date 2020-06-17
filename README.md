# TimeTreeお知らせBot
## これは何
TimeTreeの予定を確認して通知するDiscord用Botスクリプトです。  
毎朝8:00にその日の予定数とタイトルをお知らせします。

## できること
- 毎朝8:00（ソースコードの編集で変更可）に予定を取得し、予定数とタイトルをお知らせ

## 追加予定機能
- 朝の通知でタイトル+開始〜終了時刻を表示
- 予定開始10分前にお知らせ

## どうやって使うの
Discord Botよくわからないのでこういう配布方法になってます。いいやり方があったらぜひ教えてください。  
1. このリポジトリをクローンする
1. main.pyと同じフォルダに「settings」というファイルを作る（カッコ、拡張子不要）
1. Discord Botアカウントを作り（[参考](https://qiita.com/1ntegrale9/items/cb285053f2fa5d0cccdf)）、トークンをsettingsの**1行目**に貼り付ける
1. Discord上でBotに発言してほしいチャンネルのIDをコピーし、settingsの**2行目**に貼り付ける
1. [ここ](https://timetreeapp.com/personal_access_tokens)からTimeTreeのパーソナルアクセストークンを作成し、トークンをsettingsの**3行目**に貼り付ける
1. TimeTreeのカレンダーID（URLのcalendars/〇〇 の部分）をsettingsの**4行目**に貼り付ける
1. 3.で作成したBotを招待する
1. main.pyを実行

### その他
Twitter (@Watasuke102) とGithubアカウントのフォロー、リポジトリのスターよろしくおねがいします〜！

---
© 2020 わたすけ (@Watasuke102)