#! /usr/bin/perl
# Thank you so much, Pasowota-san of Hajiaya@Famille


#--------------------

$body = '<body bgcolor="004040" text="#ffffff" link="#eeffee" vlink="#dddddd" alink="#ff0000">';
## original ## $bbstitle ="���₵����[���Remix";
$bbstitle ="HeyuriRemix";


$logdir = './log/';
##original## $bbsurl = 'index.cgi';
$bbsurl = 'bbs.cgi';
$cgiurl = 'getlog_m.cgi';
$action ='getlog';


# Path to jcode.pl, the Japanese character encoding conversion library
require './jcode.pl';

# Keyword character limit (half-width)
$keylength = 64;

# Time difference - used when the server's clock is off, or when you want to set it to something other than Japan time
$tim = 0;

# KuzuhaScript
## original ## $string = '<font size="-1">�@���e���F';
$string = '<font size="-1">�@Post date:';
$locate = 38;
$back = 2;

$\ = "\n";
#--------------------
#if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
#else { $buffer = $ENV{'QUERY_STRING'}; }


$buffer = $ENV{'QUERY_STRING'};


@argv = split(/&/,$buffer);
foreach (@argv) {
	($name, $value) = split(/=/);
	$value =~ tr/+/ /;

	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	&jcode'convert(*value,'sjis');

	$COMMAND{$name} = $value;
}


&error(2) if (length($COMMAND{'keyword'}) > $keylength);
&viewlog if ($COMMAND{'action'} eq "$action");


&list;
	
sub list {

	&error(0) if(!opendir(DIR, $logdir));

	@files=readdir(DIR);
	closedir(DIR);

               @files = sort by_number @files;
               $end = @files;
               $end--; 

	print "Content-type: text/html\n\n";
## original ##	print "<html><head><title>$bbstitle �ߋ����O</title></head>\n";
	print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>$bbstitle Logs</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n";
	print "$body\n";

## original ##	print "<center><font size=\"+1\"><b>$bbstitle �ߋ����O</b></font>\n",
	print "<center><font size=\"+1\"><b>$bbstitle Logs</b></font>\n",
## original ##	  "�@<font size=\"-1\"><b><a href=\"$bbsurl\">�ꗗ</a>\n ",
	  "�@<font size=\"-1\"><b><a href=\"$bbsurl\">Topic list</a>\n ",
## original ##	  "�@<a href=\"$bbsurl\?area\=read\">�ŐV</a>\n ",
	  "�@<a href=\"$bbsurl\?area\=read\">Latest posts</a>\n ",
## original ##	  "�@<a href=\"$bbsurl\?create\=on\">�쐬</a>\n ",
	  "�@<a href=\"$bbsurl\?create\=on\">Create topic</a>\n ",
	  "\n";


	print "<form method=get action=\"$cgiurl\">";
	print "<input type=hidden name=\"action\" value=\"$action\">";
	print "<table>";
## original ##	print "<tr><td></td><td>�t�@�C����</td><td align=right>�T�C�Y</td><td align=center>���t</td></tr>";
	print "<tr><td></td><td>File name</td><td align=right>Size</td><td align=center>Date</td></tr>";
	foreach (0 .. $end) {
		if (!($files[$_] eq "." or $files[$_] eq "..")) {
			($dev,$ino,$mode,$nlink,$uid,$gid,$rdev,$size,$atime,$mtime,$ctime,$blksize,$blocks) = stat "$logdir$files[$_]";
			($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime($mtime + 32400 + $tim);
			$mon++;
			$mon = "0$mon" if ($mon < 10);
			if ($mday < 10)  { $mday  = "0$mday";  }
			if ($min < 10)  { $min =  "0$min";  }
			if ($hour < 10) { $hour = "0$hour"; }
			$checked = ' checked' if ($_ == $end);
			print "<tr><td><input type=\"radio\" name=\"logfile\" value=\"$files[$_]\"$checked></td>";
			print "<td><a href=\"$logdir$files[$_]\">$files[$_]</a></td>";
			print "<td align=right>$size</td><td align=center>$mon/$mday $hour:$min</td></tr>";
		}
	}

## original ##	print "<tr><td></td></tr><tr><td colspan=4>�����W�I�{�^���Ńt�@�C�������w�肵�Ă��������B</td></tr><tr><td></td></tr>\n";
	print "<tr><td></td></tr><tr><td colspan=4>* Use the radio buttons to specify which file you wish to search.</td></tr><tr><td></td></tr>\n";
## original ##	print "<tr><td colspan=4>�����w��F<select name=\"day1\">";
	print "<tr><td colspan=4>Time range: From day <select name=\"day1\">";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
	print "<option value=\"24\">24";
	print "<option value=\"25\">25";
	print "<option value=\"26\">26";
	print "<option value=\"27\">27";
	print "<option value=\"28\">28";
	print "<option value=\"29\">29";
	print "<option value=\"30\">30";
	print "<option value=\"31\">31";
## original ##	print "</select>��<select name=\"hour1\">";
	print "</select> hour <select name=\"hour1\">";
	print "<option value=\"00\">00";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
## original ##	print "</select>������";
	print "</select> to ";

	print "day <select name=\"day2\">";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
	print "<option value=\"24\">24";
	print "<option value=\"25\">25";
	print "<option value=\"26\">26";
	print "<option value=\"27\">27";
	print "<option value=\"28\">28";
	print "<option value=\"29\">29";
	print "<option value=\"30\">30";
	print "<option value=\"31\" selected>31";
## original ##	print "</select>��<select name=\"hour2\">";
	print "</select> hour <select name=\"hour2\">";
	print "<option value=\"24\">24";
	print "<option value=\"00\">00";
	print "<option value=\"01\">01";
	print "<option value=\"02\">02";
	print "<option value=\"03\">03";
	print "<option value=\"04\">04";
	print "<option value=\"05\">05";
	print "<option value=\"06\">06";
	print "<option value=\"07\">07";
	print "<option value=\"08\">08";
	print "<option value=\"09\">09";
	print "<option value=\"10\">10";
	print "<option value=\"11\">11";
	print "<option value=\"12\">12";
	print "<option value=\"13\">13";
	print "<option value=\"14\">14";
	print "<option value=\"15\">15";
	print "<option value=\"16\">16";
	print "<option value=\"17\">17";
	print "<option value=\"18\">18";
	print "<option value=\"19\">19";
	print "<option value=\"20\">20";
	print "<option value=\"21\">21";
	print "<option value=\"22\">22";
	print "<option value=\"23\">23";
## original ##	print "</select>���܂�";
	print "</select>";

if ($COMMAND{'bbsname'} ne ""){
$sl="selected";
}

	print "</td></tr><br>";
## original ##	print " <tr><td colspan=4>�@�����@�F<select name=\"searchmode\">";
	print " <tr><td colspan=4><label for=\"keyword\">Search</label>: <select name=\"searchmode\">";
## original ##	print "<option value=\"keyword\">�S��";
	print "<option value=\"keyword\">Full text";
## original ##	print "<option value=\"bbs\" $sl>�f����";
	print "<option value=\"bbs\" $sl>BBS name";
## original ##	print "<option value=\"name\">���e�Җ�";
	print "<option value=\"name\">User";
## original ##	print "<option value=\"subject\">�薼\n</select>";
	print "<option value=\"subject\">Title\n</select>";
	print "<input type=text id=\"keyword\" name=\"keyword\" size=\"24\" maxlength=$keylength value=\"$COMMAND{'bbsname'}\"></td></tr>";
	print "<tr><td colspan=4 align=center><input type=submit value=\"Get / Search\"></form></td></tr><br>";
	print "</table>";
	print "<hr>";

## original ##	print "</b><div align=right>Getlog Ver0.3b4 ���P�ʕۑ����O�Ή��� remixed by <a href=\"http://www.acc.ne.jp/~remix/\">�܂�</a> 2002/3/15<div>";
	print "</b><div align=right><a href=\"https://www.heyuri.net\">HeyuriRemix</a> v1.0 English translation project<br>Getlog Ver0.3b4 monthly storage log support version, remixed by <a href=\"http://www.acc.ne.jp/~remix/\">Mana</a> 2002/3/15<div>";
	print "</body></html>";
}




sub viewlog {

$COMMAND{'logfile'}=~ /^([\w.]*)$/;

	if (!open(DB,"$logdir$COMMAND{'logfile'}")) { &error(1); }
	@lines = <DB>;
	close(DB);

	$COMMAND{'last'} = $COMMAND{'first'} + 1 if ($COMMAND{'first'} >= $COMMAND{'last'});
## original ##	$first = "$COMMAND{'day1'}$COMMAND{'hour1'}��";
	$first = "$COMMAND{'day1'} Hour $COMMAND{'hour1'}";
	$last = "$COMMAND{'day2'} Hour $COMMAND{'hour2'}";

	$keyword = quotemeta($COMMAND{'keyword'});

## original ##	if ($COMMAND{'searchmode'} eq 'name') { $keyword = "���e�ҁF<b>$keyword</b>"; }
	if ($COMMAND{'searchmode'} eq 'name') { $keyword = "User: <b>$keyword</b>"; }
	elsif ($COMMAND{'searchmode'} eq 'subject') { $keyword = "<b>$keyword</b>"; }

	elsif ($COMMAND{'searchmode'} eq 'bbs') { $keyword = "target=\"\">$keyword</a>"; }

	print "Content-type: text/html\n";
## original ##	print "<html><head><title>$bbstitle �ߋ����O $COMMAND{'logfile'}</title></head>";
	print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>$bbstitle Logs $COMMAND{'logfile'}</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>";
	print "$body";
## original ##	print "<h1>$COMMAND{'logfile'} $COMMAND{'day1'}��$COMMAND{'hour1'}���`$COMMAND{'day2'}��$COMMAND{'hour2'}��</h1>";
	print "<h1>$COMMAND{'logfile'} Day $COMMAND{'day1'} Hour $COMMAND{'hour1'} - Day $COMMAND{'day2'} Hour $COMMAND{'hour2'}</h1>";

	$end = @lines;
	$end--;


	foreach (0 .. $end) {



## original ##		if ($lines[$_] =~ /<font size="-1">&#160;&#160;���e���F/) {
		if ($lines[$_] =~ /<font size="-1">&#160;&#160;Post date:/) {
			substr( $hour = substr( $lines[$_], 44, 7 ), 2, 4 ) = "" ;
			last if ($hour ge "$first");
		}
		$skip++;
	}
	$skip -= 2;
#	print"<hr>";
	$\ = '';
	foreach ($skip .. $end) {
## original ##		if ($lines[$_] =~ /<font size="-1">&#160;&#160;���e���F/) {
		if ($lines[$_] =~ /<font size="-1">&#160;&#160;Post date:/) {
			substr( $hour = substr( $lines[$_], 44, 7 ), 2, 4 ) = "" ;

			last if ($hour ge "$last");
		}
		

		if ($keyword ne '') {
			if ($lines[$_] =~ /$keyword/) {
				$flag = 1;
				$hit++; 
			}
			push( @article, $lines[$_] );
			if ($lines[$_] =~ /<\/blockquote>/) {
				print @article if ($flag > 0);  
				splice( @article, 0 );
				$flag = 0;
			}
		}
		else { print $lines[$_]; }

	}
	$\ = "\n";
	if ($COMMAND{'keyword'} ne '') {
		print "<hr>";
## original ##		if ( $hit > 0 ) { print "<h3>�u$COMMAND{'keyword'}�v�� $hit��������܂����B</h3>"; }
		if ( $hit > 0 ) { print "<h3>$hit instance of \"$COMMAND{'keyword'}\" was found.</h3>"; }
## original ##		else { print "<h3>�u$COMMAND{'keyword'}�v�͌�����܂���ł����B</h3>"; }
		else { print "<h3>No instances of \"$COMMAND{'keyword'}\" found.</h3>"; }
	}
	print "</body></html>";

	exit;

}

sub error {

	$error = $_[0];
## original ##	if ($error == 0) { $errmsg = '�f�B���N�g�����J���܂���ł����B'; }
	if ($error == 0) { $errmsg = 'The directory could not be opened.'; }
## original ##	if ($error == 1) { $errmsg = '�t�@�C�����J���܂���ł����B'; }
	if ($error == 1) { $errmsg = 'The file could not be opened.'; }
## original ##	if ($error == 2) { $errmsg = '�L�[���[�h���������܂��B'; }
	if ($error == 2) { $errmsg = 'The keyword is too long.'; }

	print "Content-type: text/html\n";
## original ##	print "<html><head><title>�G���[</title></head>";
	print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>Error</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>";
	print "$body";
	print "<h1>$errmsg</h1>";
	print "</body></html>";
	exit;
}




sub by_number {
	$a <=> $b;
}
