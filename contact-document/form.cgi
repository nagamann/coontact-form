#!/usr/bin/perl

;# ==========================
;# マルチフォーム
;# ==========================
;# http://www.juni-web.com/
;# JuNi Web info@juni-web.com
;# ==========================

require 'jcode.pl';
require 'mimew.pl';
require '../../../cgi-bin/contact/set.pl';

	d_check();
	$sirial = time();dec();
	if($v_check && ($in{'btn'} ne '' || !$snd)){
		conf();
	}elsif(keys(%in) > 0 && (!$v_check || $snd)){
		smail();
	}

sub err {
	my $err = shift;

	print "Content-Type: text/html\n\n";
	open(DAT,$err_html) or die "Cannot Open File";
	while(<DAT>){
		s/\$error\$/$err/g;
		print $_;
	}
	close(DAT);
	exit;
}


sub d_check {
	my $ck;

	$host = $ENV{'REMOTE_HOST'};
	$ip = $ENV{'REMOTE_ADDR'};
	if($host eq '' || $host eq $ip){
		$host = gethostbyaddr(pack('C4',split(/\./,$ip)),2) || $ip;
	}

	foreach(@d_host){ err($d_msg) if($host =~ /$_/); }
	foreach(@ref){ $ck=1 if($ENV{'HTTP_REFERER'} !~ /$_/); }
	err($d_msg) if($ck);
}

sub conf {
	my($html,$hidden,$ck);

	open(DAT,$conf_html) or err("Conf File Error");
	binmode(DAT);
	sysread(DAT,$html,-s $conf_html);
	close(DAT);
	jcode::convert(\$html,'euc');
	jcode::convert(\$ck_msg,'euc');

	foreach(keys(%in)){
		$in{$_} =~ s/</&lt;/g;
		$in{$_} =~ s/>/&gt;/g;
		$in{$_} =~ s/"/&quot;/g;

		my $s = $_;jcode::convert(\$s,'sjis');

		my $err;
		$err = conv(\$in{$_},$i_ck{$s}) if($i_ck{$s} ne '');
		$err = '<br><font color=red>メールアドレスをご確認下さい</font>' if($c_mail && $_ eq 'mailaddress2' && $in{'mailaddress'} ne $in{'mailaddress2'});
		jcode::convert(\$in{$_},'euc');
		$ck = 1 if $err ne '';

		$hidden .= '<input type=hidden name="'.$_.'" value="'.$in{$_}.'">' if($in{'btn'} eq '');
		if($in{'btn'} ne ''){
			if($f_type{$s} == 1){
				$html =~ s/\$$_\$/<textarea name=\"$_\">$in{$_}<\/textarea>/g;
				delete $f_type{$s};
			}elsif($f_type{$s} == 2){
				my($_opt,$op);
				foreach $op (split/:/,$f_opt{$s}){
					jcode::convert(\$op,'euc');
					if($op eq $in{$_}){
						$_opt .= ' <input type=checkbox name="'.$_.'" value="'.$op.'" checked>'.$op;
					}else{
						$_opt .= ' <input type=checkbox name="'.$_.'" value="'.$op.'">'.$op;
					}
				}
				$html =~ s/\$$_\$/$_opt/g;
				delete $f_type{$s};
			}elsif($f_type{$s} == 3){
				my($_opt,$op);
				foreach $op (split/:/,$f_opt{$s}){
					jcode::convert(\$op,'euc');
					if($op eq $in{$_}){
						$_opt .= ' <input type=radio name="'.$_.'" value="'.$op.'" checked>'.$op;
					}else{
						$_opt .= ' <input type=radio name="'.$_.'" value="'.$op.'">'.$op;
					}
				}
				$html =~ s/\$$_\$/$_opt/g;
				delete $f_type{$s};
			}elsif($f_type{$s} == 4){
				my($_opt,$op);
				foreach $op (split/:/,$f_opt{$s}){
					jcode::convert(\$op,'euc');
					if($op eq $in{$_}){
						$_opt .= ' <option value="'.$op.'" selected>'.$op;
					}else{
						$_opt .= ' <option value="'.$op.'">'.$op;
					}
				}
				$html =~ s/\$$_\$/<select name=\"$_\">$_opt<\/select>/g;
				delete $f_type{$s};
			}else{
				if($f_size{$s} eq ''){
					$html =~ s/\$$_\$/<input type=text name=\"$_\" value=\"$in{$_}\">/g;
				}else{
					$html =~ s/\$$_\$/<input type=text name=\"$_\" value=\"$in{$_}\" size=$f_size{$s}>/g;
				}
			}
			delete $f_type{$s};
		}elsif($in{'btn'} eq '' && (($check{$s} && $in{$_} eq "") || ($reply && $_ eq "mailaddress" && $in{$_} eq ""))){
			$html =~ s/\$$_\$/$ck_msg/g;$ck = 1;delete $check{$s};
		}else{
			if($in{$_} eq ""){
				$html =~ s/\$$_\$/&nbsp;/g;
			}else{
				$html =~ s/\$$_\$/$in{$_}$err/g;
			}
			delete $check{$s};
		}
	}
	if($in{'btn'} eq ''){
		foreach(keys(%check)){ jcode::convert(\$_,'euc');$html =~ s/\$$_\$/$ck_msg/g;$ck = 1; };
	}

	foreach(keys(%f_type)){
		my $s = $_;
		jcode::convert(\$s,'euc');
		if($f_type{$_} == 1){
			$html =~ s/\$$_\$/<textarea name=\"$_\">$in{$s}<\/textarea>/g;
		}elsif($f_type{$_} == 2){
			my($_opt,$op);
			foreach $op (split/:/,$f_opt{$_}){
				jcode::convert(\$op,'euc');
				if($op eq $in{$_}){
					$_opt .= ' <input type=checkbox name="'.$s.'" value="'.$op.'" checked>'.$op;
				}else{
					$_opt .= ' <input type=checkbox name="'.$s.'" value="'.$op.'">'.$op;
				}
			}
			$html =~ s/\$$s\$/$_opt/g;
		}elsif($f_type{$_} == 3){
			my($_opt,$op);
			foreach $op (split/:/,$f_opt{$_}){
				jcode::convert(\$op,'euc');
				if($op eq $in{$_}){
					$_opt .= ' <input type=radio name="'.$s.'" value="'.$op.'" checked>'.$op;
				}else{
					$_opt .= ' <input type=radio name="'.$s.'" value="'.$op.'">'.$op;
				}
			}
			$html =~ s/\$$s\$/$_opt/g;
		}elsif($f_type{$_} == 4){
			my($_opt,$op);
			foreach $op (split/:/,$f_opt{$_}){
				jcode::convert(\$op,'euc');
				if($op eq $in{$_}){
					$_opt .= ' <option value="'.$op.'" selected>'.$op;
				}else{
					$_opt .= ' <option value="'.$op.'">'.$op;
				}
			}
			$html =~ s/\$$s\$/<select name=\"$s\">$_opt<\/select>/g;
		}
	}

	$hidden .= "<input type=hidden name=m value=snd>" if $in{'btn'} eq '';
	$html =~ s/\$hidden\$/$hidden/g;
	jcode::convert(\$html,'sjis','euc');
	if($in{'btn'} ne ''){
		$html =~ s/\$button\$/<input type=submit value=" 送 信 ">/g;
	}elsif($ck){
		if($cback){
			$html =~ s/\$button\$/<input type=submit name=btn value=" 戻 る ">/g;
		}else{
			$html =~ s/\$button\$/<input type=button value=" 戻 る " onClick=history.back()>/g;
		}
	}else{
		if($cback){
			$html =~ s/\$button\$/<input type=submit name=btn value=" 戻 る "> <input type=submit value=" 送 信 ">/g;
		}else{
			$html =~ s/\$button\$/<input type=button value=" 戻 る " onClick=history.back()> <input type=submit value=" 送 信 ">/g;
		}
	}
	$html =~ s/\$[^\$]+\$/&nbsp;/g;
	print "Content-Type: text/html\n\n";
	print $html;
	exit;
}

sub conv {
	local *txt = shift;my $flg = shift;

	if($flg == 1){
		my $ck = 0;

		foreach(unpack('C*',$txt)){
			next if $_ == 130;
			if($_ < 159 || 241 < $_){ $ck=1;last; }
		}
		$ck ? (return '<br><font color=red>ひらがなのみで入力して下さい</font>') : (return '');
	}elsif($flg == 2){
		h2z(\$txt);
		my($ck,$t) = (0);

		foreach(unpack('C*',$txt)){
			if($_ == 131){
				$t = 131;
			}elsif($t != 131){
				$ck=1;last;
			}else{
				if($_ < 64 || 150 < $_){ $ck=1;last; }
				$t = '';
			}
		}
		$ck ? (return '<br><font color=red>カタカナのみで入力して下さい</font>') : (return '');
	}elsif($flg == 3){
		my @z = ("\x82\x4f","\x82\x50","\x82\x51","\x82\x52","\x82\x53","\x82\x54","\x82\x55","\x82\x56","\x82\x57","\x82\x58","\Q\x81\x7c\E");
		my @h = ("\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x2d");

		my $i;
		for($i=0;$i<11;$i++){
			$txt =~ s/$z[$i]/$h[$i]/g;
		}
		my $z = '－０-９';
		my $h = '-0-9';
		jcode::convert(\$txt,'euc');jcode::convert(\$z,'euc');jcode::convert(\$h,'euc');
		jcode::tr(\$txt,$z,$h);
		jcode::convert(\$txt,'sjis');
		h2z(\$txt);
		return '';
	}elsif($flg == 4){
		my @z = ("\x82\x4f","\x82\x50","\x82\x51","\x82\x52","\x82\x53","\x82\x54","\x82\x55","\x82\x56","\x82\x57","\x82\x58","\Q\x81\x7c\E");
		my @h = ("\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39","\x2d");

		my $i;
		for($i=0;$i<11;$i++){
			$txt =~ s/$z[$i]/$h[$i]/g;
		}
		my $z = '－．：＿／～＠０-９Ａ-Ｚａ-ｚ';
		my $h = '-.:_/~@0-9A-Za-z';
		jcode::convert(\$txt,'euc');jcode::convert(\$z,'euc');jcode::convert(\$h,'euc');
		jcode::tr(\$txt,$z,$h);
		jcode::convert(\$txt,'sjis');
		my $ck = 1 if($txt !~ /[_\w\/\.\-]+\@[\w\.\-]+/);
		$ck ? (return '<br><font color=red>メールアドレスが不正です</font>') : (return '');
	}
}

sub h2z {
	local *txt = shift;

	my @h = ("\xb6\xde","\xb7\xde","\xb8\xde","\xb9\xde","\xba\xde","\xbb\xde","\xbc\xde","\xbd\xde",
"\xbe\xde","\xbf\xde","\xc0\xde","\xc1\xde","\xc2\xde","\xc3\xde","\xc4\xde","\xca\xde","\xca\xdf",
"\xcb\xde","\xcb\xdf","\xcc\xde","\xcc\xdf","\xcd\xde","\xcd\xdf","\xce\xde","\xce\xdf","\xb3\xde",
"\xa7","\xb1","\xa8","\xb2","\xa9","\xb3","\xaa","\xb4","\xab","\xb5","\xb6","\xb7","\xb8","\xb9",
"\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xaf","\xc2","\xc3","\xc4","\xc5","\xc6",
"\xc7","\xc8","\xc9","\xca","\xcb","\xcc","\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4",
"\xad","\xd5","\xae","\xd6","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xa6","\xdd");

	my @z = ("\x83\x4b","\x83\x4d","\x83\x4f","\x83\x51","\x83\x53","\x83\x55","\x83\x57","\x83\x59",
"\x83\x5b","\x83\x5d","\x83\x5f","\x83\x61","\x83\x64","\x83\x66","\x83\x68","\x83\x6f","\x83\x70",
"\x83\x72","\x83\x73","\x83\x75","\x83\x76","\x83\x78","\x83\x79","\x83\x7b","\x83\x7c","\x83\x94",
"\x83\x40","\x83\x41","\x83\x42","\x83\x43","\x83\x44","\x83\x45","\x83\x46","\x83\x47","\x83\x48",
"\x83\x49","\x83\x4a","\x83\x4c","\x83\x4e","\x83\x50","\x83\x52","\x83\x54","\x83\x56","\x83\x58",
"\x83\x5a","\x83\x5c","\x83\x5e","\x83\x60","\x83\x62","\x83\x63","\x83\x65","\x83\x67","\x83\x69",
"\x83\x6a","\x83\x6b","\x83\x6c","\x83\x6d","\x83\x6e","\x83\x71","\x83\x74","\x83\x77","\x83\x7a",
"\x83\x7d","\x83\x7e","\x83\x80","\x83\x81","\x83\x82","\x83\x83","\x83\x84","\x83\x85","\x83\x86",
"\x83\x87","\x83\x88","\x83\x89","\x83\x8a","\x83\x8b","\x83\x8c","\x83\x8d","\x83\x8f","\x83\x92",
"\x83\x93");

	my($w,$tx,$_w,$tx2,$_tx);
	foreach(split//,$txt){
		if($w ne ''){
			$tx .= $w.$_;$w='';
		}elsif(/[\x81-\x9f|\xe0-\xef]/){
			$w = $_;
		}else{
			my $k = 1;my $i;
			for($i=0;$i<81;$i++){
				if($h[$i] eq $_){ $_tx = $z[$i];$k=0;last; }
				if($_ eq "\xde" && $_w."\xde" eq $h[$i]){ $tx2='';$tx .= $z[$i];$k=0;last; }
				if($_ eq "\xdf" && $_w."\xdf" eq $h[$i]){ $tx2='';$tx .= $z[$i];$k=0;last; }
			}
			if($k){ $tx .= $_; }else{ $tx .= $tx2;$tx2=''; }
			$tx2=$_tx;$_tx='';
		}
		$_w = $_;
	}
	$txt = $tx.$tx2;
}

sub db_save {
	my $new;

	foreach(@n_data){
		jcode::convert(\$_,'euc');
		if($_ eq "ip"){
			$new .= $ip.",";
		}elsif($_ eq "host"){
			$new .= $host.",";
		}elsif($_ eq "date"){
			$new .= $date.",";
		}elsif($_ eq "sirial"){
			$new .= $sirial.",";
		}else{
			$in{$_} =~ s/\x0d//g;$in{$_} =~ s/\x0a//g;$in{$_} =~ s/,//g;
			$new .= $in{$_}.",";
		}
	}

	jcode::convert(\$new,'sjis');
	open(DAT,">>".$data) or err("Database Error");
	print DAT $new."\n";
	close(DAT);

}

sub smail {
	my($txt);

	open(DAT,$b_mail) or err("Mail Error");
	binmode(DAT);
	sysread(DAT,$txt,-s $b_mail);
	close(DAT);
	jcode::convert(\$txt,'euc');

	foreach(keys(%in)){
		jcode::convert(\$in{$_},'euc');
		$txt =~ s/\$$_\$/$in{$_}/g;
	}

	if($c_send){
		$ENV{'TZ'} = "JST-9";
		my($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime($sirial);
		my @week = ('日','月','火','水','木','金','土');
		$date = sprintf("%.2d/%.2d/%.2d(%s) %.2d:%.2d:%.2d",
			substr($year+1900,2,2),++$mon,$mday,$week[$wday],$hour,$min,$sec);

		$txt =~ s/\$USER_AGENT\$/$ENV{'HTTP_USER_AGENT'}/g;
		$txt =~ s/\$REMOTE_ADDR\$/$ip/g;
		$txt =~ s/\$REMOTE_HOST\$/$host/g;
		$txt =~ s/\$DATE\$/$date/g;
		$txt =~ s/\$SIRIAL\$/$sirial/g;
		$txt =~ s/\x0d\x0a/\x0a/g;
		$txt =~ s/\x0d/\x0a/g;

		$subject = $in{'subject'} if($in{'subject'} ne "");
		my $sub = &mimeencode($subject);
		jcode::convert(\$txt,'sjis');
		jcode::convert(\$txt,'jis');
		my $from = $in{'mailaddress'} if($in{'mailaddress'} ne "");

		open(MAIL,"| $sendmail -t") or err("メール送信の失敗");
		print MAIL "To: ".$to."\n";
		print MAIL "From: ".$from."\n";
		print MAIL "Subject: ".$sub."\n";
		print MAIL "MIME-Version: 1.0\n";
		print MAIL "Content-Type: text/plain; charset=iso-2022-jp\n";
		print MAIL "Content-Transfer-Encoding: 7bit\n\n";
		print MAIL $txt."\n";
		close(MAIL);
	}

	db_save() if($db_check);
	reply() if($reply);

	print "Location: ".$e_url."\n\n";
	exit;
}

sub reply {
	my($txt);

	open(DAT,$r_mail) or err("Mail Error");
	binmode(DAT);
	sysread(DAT,$txt,-s $r_mail);
	close(DAT);
	jcode::convert(\$txt,'euc');

	foreach(keys(%in)){ $txt =~ s/\$$_\$/$in{$_}/g; }

	$txt =~ s/\$USER_AGENT\$/$ENV{'HTTP_USER_AGENT'}/g;
	$txt =~ s/\$REMOTE_ADDR\$/$ip/g;
	$txt =~ s/\$REMOTE_HOST\$/$host/g;
	$txt =~ s/\$DATE\$/$date/g;
	$txt =~ s/\$SIRIAL\$/$sirial/g;
	$txt =~ s/\x0d\x0a/\x0a/g;
	$txt =~ s/\x0d/\x0a/g;

	$r_sub = $in{'subject'} if($in{'subject'} ne "");
	my $sub = &mimeencode($r_sub);
	jcode::convert(\$txt,'sjis');
	jcode::convert(\$txt,'jis');

	open(MAIL,"| $sendmail -t") or err("メール送信の失敗");
	print MAIL "To: ".$in{'mailaddress'}."\n";
	print MAIL "From: ".$from."\n";
	print MAIL "Subject: ".$sub."\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-Type: text/plain; charset=iso-2022-jp\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n\n";
	print MAIL $txt."\n";
	close(MAIL);

}

sub dec {
	my $buf;

	binmode(STDIN);
	if($ENV{'REQUEST_METHOD'} eq "POST"){
		read(STDIN,$buf,$ENV{'CONTENT_LENGTH'});
		$buf =~ s/\x0d\x0a/\x0a/g;$buf =~ s/\x0d/\x0a/g;
		if(substr($ENV{'CONTENT_TYPE'},0,30) eq "multipart/form-data; boundary="){
			return if(multi($buf)==1);
		}
	}else{
		$buf = $ENV{'QUERY_STRING'};
		$buf =~ s/\x0d\x0a/\x0a/g;$buf =~ s/\x0d/\x0a/g;
	}
	foreach(split(/&/,$buf)){
		$_ =~ tr/+/ /;
		$_ =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2",$1)/eg;
		my($key,$val) = split(/=/);
		jcode::convert(\$key,'euc');
		if($key eq "m" && $val eq "snd"){
			$snd = 1;
		}else{
			($in{$key} eq "") ? ($in{$key}=$val) : ($in{$key}.=" ".$val);
		}
	}
}

sub multi {
	my($buf,$i,$deli,$key,$val,$mode)=(shift,0);

	$deli ="--".substr($ENV{'CONTENT_TYPE'},30);

	foreach(split(/\n/,$buf)){
		return 0 if($i==0 && $_ ne $deli && $_ ne $deli."--");
		if($deli eq $_){
			if($mode==2 && $key ne ""){
				chop($val);
				if($key eq "m" && $val eq "snd"){
					$snd = 1;
				}else{
					jcode::convert(\$key,'euc');
					($in{$key} eq "") ? ($in{$key}=$val) : ($in{$key}.=" ".$val);
				}
			}
			$mode=1;($key,$val) = ();
		}elsif($deli."--" eq $_){
			if($mode==2 && $key ne ""){
				chop($val);
				if($key eq "m" && $val eq "snd"){
					$snd = 1;
				}else{
					jcode::convert(\$key,'euc');
					($in{$key} eq "") ? ($in{$key}=$val) : ($in{$key}.=" ".$val);
				}
			}
			return 1;
		}elsif($mode==2){
			$val .= $_."\n";
		}elsif($mode==1 && $_ =~ /^Content\-Disposition: form\-data; name=\"([^\"]*)\".*/){
			$key = $1;
		}elsif($_ eq "" && $mode==1){
			$mode = 2;
		}
		$i++;
	}
	return 1;
}