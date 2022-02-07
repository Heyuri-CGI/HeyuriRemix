#!/usr/bin/perl

# Test crypt in Perl
# by Zurubon(ずるぼん)<zurubon@MailAndNews.com>
# @Programmer(＠プログラマ)<http://zurubon.virtualave.net/>
# last modified 2000/09/12

# Translated and slightly modified by HeyuriRemix TL on 2021/10/14

$url = './crypt.cgi';
$count_file = './crypt.cnt';

$buffer = $ENV{'QUERY_STRING'};
if(!$buffer){&html; exit;}
else{
## original ##	if($ENV{'CONTENT_LENGTH'} > 1024){$error='これは酷いね ﾜﾗ(^^;'; &html; exit;}
	if($ENV{'CONTENT_LENGTH'} > 1024){$error='That\'s not good ﾜﾗ(^^;'; &html; exit;}
	@pairs = split(/&/,$buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$FORM{$name} = $value;
	}
	if(!$FORM{input} || !$FORM{seed}){&html; exit;}
	$pass = crypt($FORM{input}, $FORM{seed});
	&html;
	&exit;
}

sub html{
	$count = &count;
	print "Content-type: text/html\n\n";
	$perlver = &GetPerlVer;
	$osver = &GetBSDVer;
	print <<"HEADER";
<!-- ## original ##<html><head><title>crypt</title></head><body bgcolor="#fffff2"> -->
<html lang="ja">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<title>crypt</title>
<style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style>
</head>
<body bgcolor="#fffff2">
<h1 style="font-size:1.333em">Test crypt in Perl</h1>
<!-- ## original ## <pre>
<b><font size="+1" color="blue">crypt</font>
`crypt(PLAINTEXT,SALT)' 
     文字列を C ライブラリの crypt() と全く同じように encrypt する。 
     パスワードファイル中のくだらないパスワードをチェックするのに便
     利である。 白い帽子を被った奴だけがこれをするべきだ。(?) (Only
     the guys wearing white hats should do this.)</b>
     -----------------------------------------日本語 perl texinfoより</pre> -->

<div style="margin-bottom:1em;max-width:640px;font-weight:bold;">
	<h2 style="color:blue;font-size:1.1667em">crypt</h2>
	<dl>
		<dt>`crypt(PLAINTEXT,SALT)'</dt>
		<dd>Encrypts a string just like the C library's crypt(). Useful for checking crappy passwords in password files. Only guys wearing white hats should do that.<dd>
	</dl>
	- From the Japanese Perl texinfo
</div>
<form action="$url" method="GET">
<center>
<table>
<td bgcolor="#000000">
<font size="-1" color="white">
#!/usr/bin/perl<br>
<br>
\$input = \$ARGV[0];<br>
\$seed = \$ARGV[1];<br>
\$val = crypt(<input type="text" size="15" name="input" maxlength="15">,<input type="text" size="5" name="seed" maxlength="5">);<br>
print "Input: \$input\nSeed: \$seed; Out: \$val\\n";<br>
exit;<br>
</font>
</td>
</table>
<input type="submit" value="execute">
</form></center>
HEADER

if($pass){
	print <<"ANS";
<center>
<p>
<font size="+1">Input:</font> <font size="+2" color="blue">$FORM{input}</font><br>
<font size="+1">Seed:</font> <font size="+2" color="blue">$FORM{seed}</font><br>
<font size="+1">Out:</font> <font size="+2" color="blue">$pass</font>
</p>
</center>
ANS
}

if($error){
	print <<"ERROR";
<center>
<p>
<font size="+1">Error:</font> <font size="+2" color="red">$error</font> 
</p>
</center>
ERROR
}

	print <<"FOOTER";
<div style="max-width:600px">
	<p>
		To generate an admin password for <b>Heyuri<wbr>Remix</b>:
		<ol>
			<li>Put your desired password in the leftmost field</li>
			<li>Put "r7" (without quotes) in the rightmost field</li>
			<li>Hit "execute"</li>
			<li>Copy the result seen next to "Out:"</li>
			<li>Open up <b>bbs.cgi</b> in a text editor</li>
			<li>Find the <b>\$adminpost</b> setting and paste the result in there</li>
		</ol>
		You should then be able to put your password into the name field when posting, which will activate the administor's capcode (you can customize the capcode with the "\$adminname" setting). This seems like as good a time as any to remind you that this is all pre-millennium web technology, and none of it is safe or secure in the slightest. ﾜﾗ(^^;
	</p>
</div>
<div align="right">
<table>
<tr><th colspan=2>Server Info</th></tr>
<tr><th>Perl:</th><td>$perlver</td></tr>
<tr><th>OS:</th><td>$osver</td></tr>
</table>
<hr>
<address>
<small>
<a href="https://www.heyuri.net">HeyuriRemix</a><br>
<a href="http://zurubon.virtualave.net/crypt.txt">Zurubon(ずるぼん)</a>
</small>
</div>
</address>
<div align="right">$count</div>
<br>
<br>
<!--VirtualAvenueBanner-->
</body></html>
FOOTER
}

sub count{
	local($counter);
	open(DATA,"$count_file");
	$counter = <DATA>;
	close (DATA);
	$counter++;
	open(DATA,">$count_file");
	eval { flock DATA, 2; };
	print DATA $counter;
	eval { flock DATA, 8; };
	close (DATA);
	return $counter;
}

sub GetPerlVer{
	local($out);

	open PERL, "/usr/bin/perl -v | grep 'This is' |";
	$out = <PERL>;
	close PERL;
	$ver = (split(/version/,$out))[1];

	return $ver;
}

sub GetBSDVer{
	local($out);

	open UNAME, "/usr/bin/uname -smr |";
	$out = <UNAME>;
	close UNAME;

	return $out;
}
