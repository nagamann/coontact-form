;# ==========================
;# �}���`�t�H�[�� ���ݒ�
;# ==========================
;# http://www.juni-web.com/
;# JuNi Web info@juni-web.com
;# ==========================

# ---- sendmail �ւ̃p�X ----
$sendmail = '/usr/sbin/sendmail';

# ---- ���O�f�[�^ �ւ̃p�X ----
$data = "../../../cgi-bin/contact/data.csv";

# ---- �Ǘ��҃p�X���[�h ----
$key = "";

# ---- ���[���e���v���[�g �ւ̃p�X ----
$b_mail = 'mail.txt';
# ---- �ԐM���[���e���v���[�g �ւ̃p�X ----
$r_mail = 'reply.txt';
# ---- �m�F��ʃt�@�C�� �ւ̃p�X ----
$conf_html = "confirm.html";
# ---- �G���[��ʃt�@�C�� �ւ̃p�X ----
$err_html = "err.html";

# ---- ���M������̉�� ----
$e_url = "thanks.html";

# ---- ���M���ݒ� ----
#$from = 'seisaku@artist-union.com';
$from = 'manaie@houselots.jp';

# ---- ���M��ݒ� ----
#$to = 'seisaku@artist-union.com';
$to = 'manaie@houselots.jp';

# ---- ���[������ ----
$subject = '�yOH���������z���������E���₢���킹�t�H�[�����炨�₢���킹������܂���';
# ---- �����ԐM���[������ ----
$r_sub = '�y�I�[�\���e�B�[�z�[���Y�z���������E���₢���킹 �����������肪�Ƃ��������܂����B';

# ---- �K�{���� ----
# '���ږ�'=>1 �Œǉ�
%check = ('inquiry'=>1,'name'=>1,'kana'=>1,'zip1'=>1,'zip2'=>1,'address1'=>1,'address2'=>1,'address3'=>1,'telephone'=>1,'mailaddress'=>1,'mailaddress2'=>1,'constructiontime'=>1,'land'=>1);

# ---- �K�{���ږ��L�����̃��b�Z�[�W ----
$ck_msg = '<span class="red">�K�{���ڂł�</span>';

# ---- �m�F��� �\��=1 ��\��=0 ----
$v_check = 1;

# ---- �f�[�^�x�[�X�L�^ ����=1 ���Ȃ�=0 ----
$db_check = 0;

# ---- �f�[�^�ۑ� ���я� ----
# ip=IP�A�h���X host=�z�X�g�A�h���X date=���� sirial=�V���A��NO
#@n_data = ('inquiry','document','name','kana','zip1','zip2','address1','address2','address3','mailaddress','mailaddress2','age','family','purpose','budget','request','constructiontime','land','trigger','contact');
# ---- �f�[�^���� ----
#@v_data = ('�₢���킹���','�����������̎��','�����O','�t���K�i','�X�֔ԍ�1','�X�֔ԍ�2','�s���{��','�s����','�Ԓn�E������','���[���A�h���X','���[���A�h���X(�m�F)','�N��','�Ƒ��l��','���z�ړI','�����\�Z�i�ō��j','���v�]','����]�̌��ݎ���','�y�n�ɂ���','���T�C�g��K�ꂽ��������','���⍇�킹���e�E���v�]');
# ---- ���̓`�F�b�N ----
# 1=�Ђ炪�Ȃ̂�
# 2=�J�^�J�i�̃`�F�b�N�����p�J�^�J�i��S�p�ւ̋����ϊ�
# 3=�p�����̔��p�ւ̋����ϊ������p�J�^�J�i�̑S�p�ւ̋����ϊ�
# 4=���[���A�h���X(�g�p����)�`�F�b�N�����p�p�����֋����ϊ�
%i_ck = ('mailaddress'=>'4','mailaddress2'=>'4');

# ---- �߂�{�^�� 1=�v���O���� 0=history.back() ----
$cback = 0;

# ---- �t�H�[�����ڎ�� ���w�莞�� text ----
# 1=textarea 2=checkbox 3=radio 4=select
#%f_type = ('����'=>'4','�I��'=>'2');
#%f_type = ('after'=>'3');

# ---- �t�H�[�����ڎ�� �ݒ� checkbox radio select �͐ݒ� ----
# �I������:��؂�Őݒ�
#%f_opt = ('����'=>'�j:��','�I��'=>'�V���b�s���O:�Z�܂�:�r�W�l�X:���y:�X�|�[�c:���s:�A�E�g�h�A:����');
# text���͗� size
#%f_size = ('�ӂ肪��'=>'30','�t���K�i'=>'20','�Z��'=>'40');

# ---- ���[���A�h���X2����̓`�F�b�N ����=1 ���Ȃ�=0 ----
$c_mail = 1;

# ---- �����ԐM ����=1 ���Ȃ�=0 ----
$reply = 1;

# ---- �Ǘ��҂֎������M ����=1 ���Ȃ�=0 ----
$c_send = 1;

# ---- ���p�֎~�z�X�g ----
@d_host = ();
# ---- �g�p��������URL ----
# �ݒu����URL ���L�����Ă����Ƃ���ȊO��URL����̑��M����t���Ȃ����鎖���o���܂�
@ref = ();
# ---- ���p�֎~���b�Z�[�W ----
$d_msg = '�����p���������܂���';


1;