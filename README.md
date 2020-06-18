# TimeTreeお知らせBot


## これは何
TimeTreeの予定を確認して通知するDiscord用Botスクリプトです。  
毎朝8:00にその日の予定数とタイトルをお知らせします。


## できること
- 毎朝8:00（ソースコードの編集で変更可）に予定を取得し、予定数とタイトル、開始〜終了時刻をお知らせ
- 予定開始10分前にお知らせ
- @everyoneで全員に通知（OFF可能）


## どうやって使うの
Discord Botよくわからないのでこういう配布方法になってます。いいやり方があったらぜひ教えてください。

1. このリポジトリをクローンする
1. main.pyがあるフォルダ内に「settings」というファイルを作る（カッコ、拡張子不要）
1. Discord Botアカウントを作り（[参考](https://qiita.com/1ntegrale9/items/cb285053f2fa5d0cccdf)）、トークンをsettingsの**1行目**に貼り付ける
1. Discord上でBotに発言してほしいチャンネルのIDをコピーし、settingsの**2行目**に貼り付ける
1. [ここ](https://timetreeapp.com/personal_access_tokens)からTimeTreeのパーソナルアクセストークンを作成し、トークンをsettingsの**3行目**に貼り付ける
1. TimeTreeのカレンダーID（URLのcalendars/〇〇 の部分）をsettingsの**4行目**に貼り付ける
1. 3.で作成したBotを招待する
1. main.pyを実行


## 設定ファイルについて
このスクリプトはスクリプトがあるフォルダ内にある、「settings」ファイルから設定を読み込みます。  
settingsは以下のように読み込まれます。

- 1行目 : Botアクセストークン
- 2行目 : チャンネルID
- 3行目 : TimeTree API キー
- 4行目 : TimeTree カレンダーID

5行目以降であれば、メモなどが書かれていても動作には影響しません。  


## コマンドライン引数
コマンドライン引数によって挙動を変えることが出来ます。  
対応している引数は以下のとおりです。
- -e [ --everyone-disable ] : @everyone をしないようになる
- -d [ --debug ]            : ターミナルにデバッグ表示を行う
- -h [ --help ]             : ヘルプ（設定ファイルについて、コマンドライン引数）を表示


## その他
Twitter (@Watasuke102) とGithubアカウントのフォロー、リポジトリのスターよろしくおねがいします〜！


---
© 2020 わたすけ (@Watasuke102)