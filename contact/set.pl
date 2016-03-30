;# ==========================
;# マルチフォーム 環境設定
;# ==========================
;# http://www.juni-web.com/
;# JuNi Web info@juni-web.com
;# ==========================

# ---- sendmail へのパス ----
$sendmail = '/usr/sbin/sendmail';

# ---- ログデータ へのパス ----
$data = "../../../cgi-bin/contact/data.csv";

# ---- 管理者パスワード ----
$key = "";

# ---- メールテンプレート へのパス ----
$b_mail = 'mail.txt';
# ---- 返信メールテンプレート へのパス ----
$r_mail = 'reply.txt';
# ---- 確認画面ファイル へのパス ----
$conf_html = "confirm.html";
# ---- エラー画面ファイル へのパス ----
$err_html = "err.html";

# ---- 送信完了後の画面 ----
$e_url = "thanks.html";

# ---- 送信元設定 ----
#$from = 'seisaku@artist-union.com';
$from = 'manaie@houselots.jp';

# ---- 送信先設定 ----
#$to = 'seisaku@artist-union.com';
$to = 'manaie@houselots.jp';

# ---- メール件名 ----
$subject = '【OH資料請求】資料請求・お問い合わせフォームからお問い合わせがありました';
# ---- 自動返信メール件名 ----
$r_sub = '【オーソリティーホームズ】資料請求・お問い合わせ いただきありがとうございました。';

# ---- 必須項目 ----
# '項目名'=>1 で追加
%check = ('inquiry'=>1,'name'=>1,'kana'=>1,'zip1'=>1,'zip2'=>1,'address1'=>1,'address2'=>1,'address3'=>1,'telephone'=>1,'mailaddress'=>1,'mailaddress2'=>1,'constructiontime'=>1,'land'=>1);

# ---- 必須項目未記入時のメッセージ ----
$ck_msg = '<span class="red">必須項目です</span>';

# ---- 確認画面 表示=1 非表示=0 ----
$v_check = 1;

# ---- データベース記録 する=1 しない=0 ----
$db_check = 0;

# ---- データ保存 並び順 ----
# ip=IPアドレス host=ホストアドレス date=時刻 sirial=シリアルNO
#@n_data = ('inquiry','document','name','kana','zip1','zip2','address1','address2','address3','mailaddress','mailaddress2','age','family','purpose','budget','request','constructiontime','land','trigger','contact');
# ---- データ名称 ----
#@v_data = ('問い合わせ種別','ご請求資料の種類','お名前','フリガナ','郵便番号1','郵便番号2','都道府県','市町村','番地・建物名','メールアドレス','メールアドレス(確認)','年齢','家族人数','建築目的','建物予算（税込）','ご要望','ご希望の建設時期','土地について','当サイトを訪れたきっかけ','お問合わせ内容・ご要望');
# ---- 入力チェック ----
# 1=ひらがなのみ
# 2=カタカナのチェック＆半角カタカナを全角への強制変換
# 3=英数字の半角への強制変換＆半角カタカナの全角への強制変換
# 4=メールアドレス(使用文字)チェック＆半角英数字へ強制変換
%i_ck = ('mailaddress'=>'4','mailaddress2'=>'4');

# ---- 戻るボタン 1=プログラム 0=history.back() ----
$cback = 0;

# ---- フォーム項目種類 未指定時は text ----
# 1=textarea 2=checkbox 3=radio 4=select
#%f_type = ('性別'=>'4','選択'=>'2');
#%f_type = ('after'=>'3');

# ---- フォーム項目種類 設定 checkbox radio select は設定 ----
# 選択肢を:区切りで設定
#%f_opt = ('性別'=>'男:女','選択'=>'ショッピング:住まい:ビジネス:音楽:スポーツ:旅行:アウトドア:投資');
# text入力欄 size
#%f_size = ('ふりがな'=>'30','フリガナ'=>'20','住所'=>'40');

# ---- メールアドレス2回入力チェック する=1 しない=0 ----
$c_mail = 1;

# ---- 自動返信 する=1 しない=0 ----
$reply = 1;

# ---- 管理者へ自動送信 する=1 しない=0 ----
$c_send = 1;

# ---- 利用禁止ホスト ----
@d_host = ();
# ---- 使用を許可するURL ----
# 設置するURL を記入しておくとそれ以外のURLからの送信を受付けなくする事が出来ます
@ref = ();
# ---- 利用禁止メッセージ ----
$d_msg = 'ご利用いただけません';


1;