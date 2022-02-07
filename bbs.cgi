#! /usr/bin/perl
#
#	KuzuhaScript Final Beta #2 pl0.3 Remix β1.012
#	 (main bulletin board component)
#
#(2000/1/06 update ---- make the post forms on the topic list and latest post pages only display the title
#
#       ...is what RNS Remix 4.0 is based on

# Modified by HeyuriRemix TL in 2021/10

###############################################################################
#  Settings
###############################################################################

# Root URL of the bulletin board installation
## original ## $urltop = 'http://www.acc.ne.jp/~remix/remix2/';
$urltop = './';

# URL of the bulletin board CGI
## original ## $cgiurl = 'http://www.acc.ne.jp/~remix/remix2/bbs.cgi';
$cgiurl = './bbs.cgi';

# jcode.pl path
$jcode = './jcode.pl';

# Call jcode.pl
require $jcode ;

# gzip path
#  (If you don't wish to use the gzip compression transfer feature, leave empty)
#$gzip = '/gzip/';

# Host address of where the CGI will be installed
## original ## $bbshost = 'www.acc.ne.jp';
$bbshost = '';

# Log file name
$logfilename = './bbs.log';

$totalfilename = $logfilename;

$totalist =  './list.log';


# Hit counter start date
## original ## $countdate = '2000/02/16';
$countdate = '2021/10/14'; # (TL note: set this to the date you launch your board)

# First part of the hit counter file name
## original ## $countfile = './count1/count';
$countfile = './count1/count'; # (TL note: I believe this is unused)

# Hit counter bulletproof level (TL note: number of count files used to ensure accurate readings; more count files = greater accuracy, at the cost of greater server load. I recommended not exceeding 3-5)
$countlevel = 3;

# Number of messages stored
$logsave = 300;

# Number of latest messages stored
$slogsave = 300;


# List view ###########

         # Maximum number of logs
             $max = 200; # This is disabled.

         # Default number of topics displayed on one page
              $lmaxdef = 50;

         # Menu color (TL note: title bar and table headers)
              $tcolor="4f7f7a";

         # Title menu color (TL note: unused)
              $dcolor="c0c0c0";

         # Highlight color
              $scolor="ffffff";

         # List menu color (TL note: alternate row color)
             $sbgc="005050";

         # Number of recently created topics displayed
             $hl="5";

# Number of messages displayed on one screen
#  (1 - Number of messages saved)
$msgdisp = 30;

# Delete topics that haven't received posts within this many days (please adjust appropriately)
## original ## $delete=8;
$delete=30;

$deletesec=$delete * 86400;

# How many posts required to extend a topic's life for one day?
## original # $enmei=30;
$enmei=1;

$enmeisec=int(86400/$enmei);



# Time difference between the server location and your location (TL note: the examples provided below are intended for admins located in Japan; if you're not in Japan, use whatever is appropriate for your installation instead)
#   Japan               :   0
#   Greenwich Mean Time :  -9
#   America             : -14 (Washington)
#                       : -20 (Midway Islands)
#   New Zealand         :   3
$difftime = 0;

# Bulletin board name
## original ## $bbstitle = 'RNS Remix4.02 Sample';
$bbstitle = 'HeyuriRemix';
$mainbbstitle=$bbstitle;

# Background color
$bgc    = '004040';
$bgk    = $bgc ;

# Text color
$textc  = 'ffffff';

# Link colors
$linkc  = 'eeffee';
$vlinkc = 'dddddd';
$alinkc = 'ff0000';

# Title color (TL note: wasn't being used, but I modified it back in)
## original ## $subjc  = 'fffffe';
$subjc  = 'ffffee';



# Log background color
## original ## $oldlogbgc = 'c0d0b0';
$oldlogbgc = $bgc;

# Directory name for saved logs
$oldlogfiledir = './log/';

# How to save logs
#   0 : Daily
#   1 : Monthly
$oldlogsavesw = 1;

# Number of days that logs are kept
$oldlogsaveday = 4;

# Maximum file size for logs
$maxoldlogsize = 10 * 1024 * 1024;

# Number of posts to check for double posts
$checkcount = 30;

# Maximum number of characters per line
$maxmsgcol = 192; # (TL note: you might be tempted to increase this, but without making a lot of changes to the HTML/CSS (i.e. replacing <pre> tags in posts to allow word wrapping while still keeping the Japanese monospace font), it's for the best that users just learn to preformat their posts with line breaks)

# Maximum number of lines per message
$maxmsgline = 100;

# Maximum message size (in bytes)
$maxmsgsize = 8400;


# Consecutive post provention code (must be changed)
$protect_a = 292529;	# 8-digit number
$protect_b = 43;		# 2-digit number

$pstime = 3;
$pltime = 3600;

# Default value of the auto-link function
#   0 : Disabled
#   1 : Enabled
$autolink = 1;

# Follow-up post screen
#   0 : Open and display a new window
#   1 : Display in the same window
$followwin = 0;

# Record poster IP addresses
#   0 : Do not record
#   1 : Record only anonymous proxies
#   2 : Record all
$iprec = 0;

# Record user agent (browser name)
#   0 : Disabled
#   1 : Enabled
$uarec = 0;

# URL of the PR Office (TL note: front page or site information page)
$infopage = 'http://www4.famille.ne.jp/~kuzuha/info.html'; # (TL note: unused)

# Administrator's name
## original ## $adminname = '管理人';
$adminname = 'Administrator';

# Administrator's email address
$adminmail = '';

# Password to post as admin (use the character string generated by crypt.cgi)
$adminpost = '';

# Form data submission method
$formmethod = 'post';

# Maximum length of the "latest post" previews on the topic list table
$bytes=30;

# Genre setting 1 (enter the genre names in order)

## original ## @genname=("地域","文芸","プロジェクト","スポーツ","音楽","\ソ\フト","ハード","社会","職業","団体","個人","ファン","アダルト","趣味","美容と健康","雰囲気","退避用","その他");
@genname=("Regional","Literature","Projects","Sports","Music","Software","Hardware","Society","Jobs","Groups","Personal","Fandom","Adult/Porn","Hobbies","Health & Beauty","Ambience","Refuge","Other"); # (TL note: these names can be modified freely at any time without breaking anything as long as they are in the same order as the genre IDs in the next setting below)


# Genre setting 2 (enter the genre IDs in order) 

## original ## @genid=(region,litera,project,sports,music,soft,hard,social,job,group,personal,fan,ero,hobby,health,air,refuge,other);
@genid=(region,litera,project,sports,music,soft,hard,social,job,group,personal,fan,ero,hobby,health,air,refuge,other); # (TL note: these are used for URLs and topic data files - avoid modifying a given genre id after it has been established unless you don't mind the headache it will surely provide)

# Genre setting 3 (number of genres)

$gens=18;



###############################################################################
#  Time format conversion
###############################################################################

sub getnowdate {
	
	( $sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdat )
		= localtime ( $_[0] );
	$year += 1900;
	$mon++;
## original ##	$nowdate = sprintf ( "%d/%02d/%02d(%s)%02d時%02d分%02d秒", 
	$nowdate = sprintf ( "%d/%02d/%02d(%s)%02d:%02d:%02d", 
		$year, $mon, $mday, 
## original ##		( '日', '月', '火', '水', '木', '金', '土' )[$wday],
		( 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' )[$wday],
		$hour, $min, $sec );
}


###############################################################################
#  Obtain form data
###############################################################################

sub getformdata {
	
	my ( $buf, $name, $value );
	
	if ( $ENV{'REQUEST_METHOD'} eq 'POST' ) {
		read ( STDIN, $buf, $ENV{'CONTENT_LENGTH'} );
	} else {
		$buf = $ENV{'QUERY_STRING'};
	}
	
	if ( $buf ne '' ) {
		
## original ##		&prterror ( '呼び出し元が不正です。' ) 
		&prterror ( 'Invalid caller.' ) 
		  if ( $ENV{'HTTP_HOST'} ne '' && ! ( $ENV{'HTTP_HOST'} =~ /$bbshost/i ) );
		
		$referer = $ENV{'HTTP_REFERER'};
		$referer =~ s/\+/ /g;
		$referer =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack ( "C", hex ( $1 ) )/eg;

#################################


		
		foreach ( split ( /&/, $buf ) ) {
			( $name, $value ) = split ( /=/ );
			$value =~ s/\+/ /g;
			$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack ( "C", hex ( $1 ) )/eg;	
			&jcode'convert ( *value, 'sjis' );
			$value =~ s/</&lt;/g;
			$value =~ s/>/&gt;/g;
			$value =~ s/\r\n/\r/g;
			$value =~ s/\n/\r/g;
			$value =~ s/\r$//;
			$value =~ s/\,/\0/g;
			$FORM{$name} = $value;


		}
	}


if ( $FORM{'bbsname'} eq '＠')

{$FORM{'bbsname'}="";}

## original ##		if ( $FORM{'area'} eq '' || $FORM{'area'} eq 'read' && $FORM{'code'} ne '' && $FORM{'code'} ne "最新投稿一覧") {
		if ( $FORM{'area'} eq '' || $FORM{'area'} eq 'read' && $FORM{'code'} ne '' && $FORM{'code'} ne "Latest posts list") {
#&codesearch;
$FORM{'area'}=$logname;
	}

## original ## #&prterror ( 'メッセージ読み込みに失敗しました' );
#&prterror ( 'Failed to read message' );

		if ( $FORM{'area'} ne '' ) 
{
$FORM{'area'}=~ s/\s//g;
$logfilename="./data/bbb.dat";
$logfilename =~ s/bbb/$FORM{'area'}/g;

}


		if ( $FORM{'area'} eq 'read' ) 
{
$logfilename=$totalfilename;
}




	}

###############################################################################
#  Obtain environment variables
###############################################################################

sub getenv {
	
	if ( $uarec ) {
		$agent = $ENV{'HTTP_USER_AGENT'};
		$agent =~ s/</&lt;/g;
		$agent =~ s/>/&gt;/g;
		$agent =~ s/,/./g;
	}
	
	if ( $iprec == 0 ) { return; }
	
	$addr = $ENV{'REMOTE_ADDR'};
	$host = $ENV{'REMOTE_HOST'};
	if ( $addr eq $host || $host eq '' ) {
		$host = gethostbyaddr ( pack ( 'C4', split ( /\./,$addr ) ), 2 ) || $addr;
	}
	
	$proxyflg = 0;
	
	if ( $ENV{'HTTP_CACHE_CONTROL'} ne '' )			{ $proxyflg = 1; }
	if ( $ENV{'HTTP_CACHE_INFO'} ne '' )			{ $proxyflg += 2; }
	if ( $ENV{'HTTP_CLIENT_IP'} ne '' )				{ $proxyflg += 4; }
	if ( $ENV{'HTTP_FORWARDED'} ne '' )				{ $proxyflg += 8; }
	if ( $ENV{'HTTP_FROM'} ne '' )					{ $proxyflg += 16; }
	if ( $ENV{'HTTP_PROXY_AUTHORIZATION'} ne '' )	{ $proxyflg += 32; }
	if ( $ENV{'HTTP_PROXY_CONNECTION'} ne '' )		{ $proxyflg += 64; }
	if ( $ENV{'HTTP_SP_HOST'} ne '' )				{ $proxyflg += 128; }
	if ( $ENV{'HTTP_VIA'} ne '' )					{ $proxyflg += 256; }
	if ( $ENV{'HTTP_X_FORWARDED_FOR'} ne '' )		{ $proxyflg += 512; }
	if ( $ENV{'HTTP_X_LOCKING'} ne '' )				{ $proxyflg += 1024; }
	if ( $agent =~ /cache|delegate|gateway|httpd|proxy|squid|www|via/i ) {
		$proxyflg += 2048;
	}
	if ( $host =~ /cache|^dns|dummy|^ns|firewall|gate|keep|mail|^news|pop|proxy|smtp|w3|^web|www/i ) {
		$proxyflg += 4096;
	}
	if ( $host eq $addr ) {
		$proxyflg += 8192;
	}
	
	$realaddr = '';
	$realhost = '';
	if ( $proxyflg > 0 ) {
		
		if ( $ENV{'HTTP_X_FORWARDED_FOR'} =~
		  s/^(\d+)\.(\d+)\.(\d+)\.(\d+).*/$1.$2.$3.$4/ ) {
			$realaddr = "$1.$2.$3.$4";
		} elsif ( $ENV{'HTTP_FORWARDED'} =~ 
		  s/.*\s(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/ ) {
			$realaddr = "$1.$2.$3.$4";
		} elsif ( $ENV{'HTTP_VIA'} =~
		  s/.*\s(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/ ) {
			$realaddr = "$1.$2.$3.$4";
		} elsif ( $ENV{'HTTP_CLIENT_IP'} =~
		  s/(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/ ) {
			$realaddr = "$1.$2.$3.$4";
		} elsif ( $ENV{'HTTP_SP_HOST'} =~
		  s/(\d+)\.(\d+)\.(\d+)\.(\d+)/$1.$2.$3.$4/ ) {
			$realaddr = "$1.$2.$3.$4";
		} elsif ( $ENV{'HTTP_FORWARDED'} =~ s/.*\sfor\s(.+)/$1/ ) {
			$realhost = "$1";
		} elsif ( $ENV{'HTTP_FROM'} =~ s/\-\@(.+)/$1/ ) {
			$realhost = "$1";
		}
		
		if ( $realaddr eq '' && $realhost ne '' ) {
			$realpackaddr = gethostbyname ( $realhost );
			( $a, $b, $c, $d ) = unpack ( 'C4', $realpackaddr );
			$realaddr = "$a.$b.$c.$d";
		}
		
		if ( $realaddr ne '' && $iprec != 2 ) {
			$host = '(leak)';
		}
	} else {
		$host = '(none)' if ( $iprec != 2 );
111	}
}


###############################################################################
#  Encode strings
###############################################################################

sub escstring {
	
	my ( $srcstr ) = $_[0];
	
	$srcstr =~ s/([^a-zA-Z0-9\s])/sprintf ( "%%%lx", ( unpack ( "C", $1 ) ) )/eg;
	$srcstr =~ s/ /\+/g;
	
	return $srcstr;
}


###############################################################################
#  Read messages
###############################################################################

sub loadmessage {

if (!-f $logfilename) { 

$deleteplease=yes;

#&dirread


}


close(STDIN);
	
## original ##	open ( READLOG, "$logfilename" ) || &prterror ( 'メッセージ読み込みに失敗しました' );
	open ( READLOG, "$logfilename" ) || &prterror ( 'Failed to read message' );
	eval 'flock ( READLOG, 1 )';
	seek ( READLOG, 0, 0 );
	@logdata =  <READLOG>;
	eval 'flock ( READLOG, 8 )';
	close ( READLOG );

	$ends=@logdata;
	$ends--;

}




###############################################################################
#  Obtain a message
###############################################################################

sub getmessage {
	
	( $ndate, $postid, $protect, $thread, $bbs, $area, $user, $mail, $title, $msg )
	  = split ( /\,/, $_[0] );
	$msg =~ s/\n$//;
	$wdate = &getnowdate ( $ndate );
}




###############################################################################
#  Output a message
###############################################################################

sub prtmessage {
	
	my $out = $_[0];
	my $printmode = $_[1];
	
	$title =~ s/\0/\,/g;
	$mail =~ s/\0/\,/g;
	$user =~ s/\0/\,/g;
	$msg =~ s/\0/\,/g;
	
	if ( $printmode == 0 ) {
		$msg =~ s/<a href=\"mode=follow\&search=(.*)\&ref=(.*)\">(.*)<\/a>/<a href=\"$cgiurl\?bgcolor=$bgc\&mode=follow\&search=$1\&ref=$2\">$3<\/a>/;
	} else {
		$msg =~ s/<a href=\"mode=follow\&search=.*\&ref=.*\">(.*)<\/a>/<font color=\"#$linkc\"><u>$1<\/u><\/font>/;
	}
	
## original ##	print $out "<font size=\"+1\" ><b>$title</b></font>\n&#160;&#160;投稿者：<b>";
	print $out "<font size=\"+1\" color=$subjc><b>$title</b></font>\n&#160;&#160;User:&#160;<b>";
	if ( $mail ne '' ) {
		print $out "<a href=\"mailto:$mail\">$user</a>";
	} else {
		print $out "$user";
	}
## original ##	print $out "</b></font>\n<font size=\"-1\">&#160;&#160;投稿日：$wdate\n";
	print $out "</b></font>\n<font size=\"-1\">&#160;&#160;Post date:&#160;$wdate\n";
	
	if ( $printmode == 0 ) {
		print $out "&#160;&#160;<a href=\"$cgiurl\?area\=$area\&mode\=follow\&username=",
		  &escstring ( $FORM{'username'} ),
		  "&msgdisp=$msgdisp&postid=$toppostid&search\=$postid\&autolink=$FORM{'autolink'}\&bgcolor\=$bgc\&",
		  "custom\=$FORM{'custom'}\"";
		if ( $followwin == 0 ) { print $out " target=\"link\""; }
		print $out ">■</a>\n&#160;&#160;<a href=\"$cgiurl\?area\=$area\&code\=$bbs\&mode\=search\&search\=",
		  &escstring ( $user ),
		  "\&autolink=$FORM{'autolink'}\&custom=$FORM{'custom'}\&bgcolor\=$bgc\" target=\"link\">★</a>\n";
		if ( $thread ne '' ) {
			print $out "&#160;&#160;<a href=\"$cgiurl\?area=$area\&code\=$bbs\&mode\=thread\&search\=$thread\&custom=$FORM{'custom'}\&autolink=$FORM{'autolink'}\&bgcolor\=$bgc\" target=\"link\">◆</a>\n";
		}
	}

if (($FORM{'area'}  eq 'read') || ($FORM{'area'}  eq '')) { print "&#160;&#160;<a href=\"$cgiurl\?area\=$area\&bgcolor\=$bgc\" target=\"$link\">$bbs</a>\n"; }

if($logmsg eq '1') { print "&#160;&#160;<a href=\"$cgiurl\?bgcolor\=$bgc\&action\=search3\&search\=$himage\&code\=$bbs\" target=\"$link\">$bbs</a>\n"; }



	print $out "</font><p>\n<blockquote><pre>$msg</pre></p>\n</blockquote></p>\n<hr>\n"
}



###############################################################################
#  Display footer section
#    If you wish to modify this script, please add a note stating that it is a 
#    modified version in the version description section below.
###############################################################################

sub prtfooter {
	



	print <<"__EOF__";
</form><br><br><div align=right><font size=\"-1\">
<!-- ## original ## <a href="http://www.acc.ne.jp/~remix/script.html">RNS Remix4.02</a> はフリーウェアです。<br>くずはすくりぷと Final Beta #2 pl0.3を改造しました。</div></font></b></body></html> -->
<a href="https://www.heyuri.net">HeyuriRemix</a> v1.0 is an English translation project.<br><a href="http://www.acc.ne.jp/~remix/script.html">RNS Remix4.02</a> is freeware (modified).<br>KuzuhaScript Final Beta #2 pl0.3 (modified).</div></font></b></body></html>
__EOF__

exit;
}


###############################################################################
#  Process bulletproof hit counter
###############################################################################

sub counter {



	
	my ( @count, @filenumber, @sortedcount, $maxcount, $mincount );
	
	for ( $i = 0 ; $i < $countlevel ; $i++ ) {
		open ( IN, "$countfile$i.dat" );
		$count[$i] = <IN>;
		$filenumber{$count[$i]} = $i;
		close ( IN );
	}
	
	@sortedcount = sort { $a <=> $b; } @count;
	$maxcount = $sortedcount[$countlevel-1];
	$mincount = $sortedcount[0];
	
	$maxcount++;
#	print $maxcount;
	
	open ( OUT, ">$countfile$filenumber{$mincount}.dat" );
	print OUT $maxcount;
	close ( OUT );

$count=$maxcount;

## original ## $defcount="$countdateから $maxcount";
$defcount="$maxcount page hits since $countdate";


}


###############################################################################
#  Display error message
###############################################################################

sub prterror {


# Header output

print "Content-type: text/html\n";


	
	my $error = $_[0];
	
	if ( $error eq 'xx' ) {
## original ##		$errmsg = 'かわいそう';
		$errmsg = 'What a pity!';
	} else {
		$errmsg = $error;
	}

	
	if ( $body eq '' ) {
$body='<body>';
	}
	
	print <<"__EOF__";


<!-- ## original ## <html><head><title>$bbstitle (error)</title></head> -->
<html lang="ja"><head><meta name="viewport" content="width=device-width, initial-scale=1"><META http-equiv="Content-Type" content="text/html; charset=Shift_JIS"><title>$bbstitle (error)</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>
$body
<h3>$errmsg</h3>$FORM{'code'}-$FORM{'area'}-$bbs-$logname
__EOF__
	

	
	print "</body></html>\n";
	exit;
}



###############################################################################
#  Display form section
###############################################################################

sub prtform {
	
	my $defaulttitle = $_[0];
	my $defaultmsg = $_[1];
	my $defaultlink = $_[2];
	
	print <<"__EOF__";
<form method="$formmethod" action="$cgiurl\?area\=$FORM{'area'}">
__EOF__
	
	
if ( $FORM{'create'} eq 'on' ) {
## original ##		print "<br>トピック名　<input type=\"text\" name=\"code\" size=\"30\" maxlength=\"40\" value=\"＠\">　ジャンル：<select name=areaname>\n ";
		print "<br><label for=\"code\">Topic name</label> <input type=\"text\" id=\"code\" name=\"code\" size=\"30\" maxlength=\"40\" value=\"＠\">　<label for=\"genre\">Genre</label>: <select id=\"genre\" name=areaname>\n ";

	foreach (0 .. $gens){
	print "<option value=$genid[$_]>$genname[$_]\n";
        	}

	print "</select><br><br>";}#if

    $gens++;

	print <<"__EOF__";
<input type="hidden" name="mode" value="post">
<!-- ## original ## 投稿者 <input type="text" name="username" size="20" maxlength="30" value="$FORM{'username'}"><br> -->
<label for="username">Name</label> <input id="username" type="text" name="username" size="20" maxlength="30" value="$FORM{'username'}"><br>
<!-- ## original ## メール <input type="text" name="mailaddr" size="30" maxlength="255" value="$FORM{'mailaddr'}"> -->
<label for="email">Email</label> <input id="email" type="text" name="mailaddr" size="30" maxlength="255" value="$FORM{'mailaddr'}">
<INPUT type="hidden" name="charchk" value="あ">&#160;&#160; 
__EOF__

if ( $FORM{'create'} ne 'on' ) {

## original ##	print "<input type\=\"hidden\" name\=\"code\" value\=$bbstitle><br>題名&#160;&#160; <input type=\"text\" name=\"title\" size=\"30\" maxlength=\"40\" value=$defaulttitle>&#160;&#160; ";}
	print "<input type\=\"hidden\" name\=\"code\" value\=$bbstitle><br><label for=\"title\">Title</lable>&#160;&#160; <input id=\"title\" type=\"text\" name=\"title\" size=\"30\" maxlength=\"40\" value=$defaulttitle>&#160;&#160; ";}


	print <<"__EOF__";
<!-- ## original ## <input type="submit" value="投稿／リロード"> -->
<input type="submit" value="Post/Reload">
<!-- ## original ## <input type="reset" value="消す"><p> -->
<input type="reset" value="Clear"><p>
<!-- ## original ## 内容<font size="-1"><i>（タグは使えません。長すぎる文章もだめ。内容を書かずに投稿するとリロードします。</i>）</font><br> -->
<label for="contents">Contents</label><font size="-1"><i> (Tags cannot be used. Don't write lines that are too long, use line breaks to format your posts. Posting while the contents field is empty will reload the page.</i>）</font><br>
<!-- ## original ## <textarea name="message" cols="70" rows="5"> -->
<textarea id="contents" name="message" cols="70" rows="5">
__EOF__
	
	if ( $defaultmsg ) {
		print "$defaultmsg\r";
	}
	
	print <<"__EOF__";
</textarea><p>
__EOF__


if ( $FORM{'create'} eq 'on' ) {
	print <<"__EOF__";
<!-- ## original ## <hr>好きなトピックの掲示板を作れます。他のBBSの宣伝や意味不明な一行投稿は<a href="http://nazoremix.virtualave.net/bbs.cgi">なぞRemix</a>にお願いします。 -->
<hr>Create a bulletin board for your favorite topic. If you want to advertise other BBSes or make unintelligible one-line posts, please go to <a href="http://nazoremix.virtualave.net/bbs.cgi">NazoRemix</a>.
__EOF__
				}



	$nowtime = time - $difftime * 60 * 60;
	my @hostbin = split ( /\./, $ENV{'REMOTE_ADDR'} );
	for ( $i = 0 ; $i < 4 ; $i++ ) {
		$hostbin[$i] = vec ( pack ( 'C4', $hostbin[$i] ), 0, 8 );
	}
	$protect_c = $hostbin[0] ^ $hostbin[1] ^ $hostbin[2] ^ $hostbin[3];
	my $pkey0 = ( $nowtime + $protect_a ) * $protect_b + $protect_c;
	my $pkey1 = $pkey0 - int ( rand ( 64 ) );
	my $pkey2 = $pkey1 + int ( rand ( 128 ) );
	
	my @pkeystr;
	$pkeystr[0] = "\n<input type=\"hidden\" name=\"protect\" value=\"$pkey0\">\n";
	$pkeystr[1] = "<!--\n<input type=\"hidden\" name=\"protect\" value=\"$pkey1\">\n-->";
	$pkeystr[2] = "<!--\n<input type=\"hidden\" name=\"protect\" value=\"$pkey2\">\n-->";
	
	my @apkey;
	push ( @apkey, splice ( @pkeystr, rand ( @pkeystr ), 1 ) ) while @pkeystr;
	@pkeystr = @apkey;
	
	print "$pkeystr[0]$pkeystr[1]$pkeystr[2]\n";
}


###############################################################################
#  Display follow-up post page
###############################################################################

sub prtfollow {



		if ( ($FORM{'area'} ne '' ) && ( $FORM{'area'} ne 'read' ) &&($FORM{'bbsname'} eq "")) {

	if (!open(STDIN,"$logfilename ")) 
{


print "$FORM{'area'} \n";

## original ## &prterror ( 'ファイル読み込みに失敗しました' ); }
&prterror ( 'Failed to load file' ); }

$set=<STDIN>;
close(STDIN);

( $ndate, $postid, $protect, $thread, $host, $agent, $user, $mail, $title, $msg )= split ( /\,/, $set); 

$bbstitle = $host;

}

	
	my $retry = $_[0];
	my $success = 0;
	
	&loadmessage;
	
	## original ## &prterror ( 'パラメータがありません。' ) if ( $FORM{'search'} eq '' );
	&prterror ( 'There are no parameters.' ) if ( $FORM{'search'} eq '' );
	
	print "",
## original ##	  "<html><head><title>$bbstitle</title><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"></head>\n$body\n\n";
	  "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>$bbstitle</title><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n$body\n\n";



	foreach ( 0 .. @logdata - 1 ) {
		&getmessage ( $logdata[$_] );
		if ( $postid eq $FORM{'search'} ) {
			$success = 1;
			last;
		}
		$i++;
	}
	
	if ( $success == 0 ) {
## original ##		print "<h3>指定されたメッセージが見つかりません。</h3><body></html>";
		print "<h3>The specified message could not be found.</h3><body></html>";
		exit;
	}
	
	my $formmsg;
	if ( $retry == 0 ) {
		$formmsg = $msg;
		$formmsg =~ s/\0/\,/g;
## original ##		$formmsg =~ s/\r\r\<a href\=\S+>参考：.*\<\/a\>//;
		$formmsg =~ s/\r\r\<a href\=\S+>Reference:.*\<\/a\>//;
		$formmsg =~ s/\<a href\=\S+ target\=\"link\"\>(\S+)\<\/a\>/$1/g;
		$formmsg =~ s/\r/\r&gt; /g;
		$formmsg = "&gt; $formmsg\r";
		$formmsg =~ s/&gt; &gt; &gt;.*?\r//g;
		$formmsg =~ s/\r&gt;\s+\r/\r/g;
	} else {
		$formmsg = $FORM{'message'};
	}
	
	&prtmessage ( 'STDOUT', 0 );
	
	if ( $thread eq '' ) {
		$thread = $postid;
	}
	
## original ##	print "フォロー記事投稿<br>";
	print "Follow-up post<br>";
	&prtform ( "＞$user", $formmsg, '' );
	
	print <<"__EOF__";
<p><input type=\"hidden\" name=\"msgdisp\" value=\"$msgdisp\">
<input type=\"hidden\" name=\"autolink\" value=\"checked\" $FORM{'autolink'}><br>
<input type=\"hidden\" name=\"custom\" value=\"$FORM{'custom'}\">
<input type=\"hidden\" name=\"postid\" value=\"$FORM{'postid'}\">
<input type=\"hidden\" name=\"search\" value=\"$FORM{'search'}\">
<input type=\"hidden\" name=\"area\" value=\"$FORM{'area'}\">
<input type=\"hidden\" name=\"thread\" value=\"$thread\">
<input type=\"hidden\" name=\"follow\" value=\"$postid:$wdate\">
</form>
</body></html>
__EOF__
	
	exit;
}


###############################################################################
#  Display entire bulletin board
###############################################################################

sub prtboard {



		if ( ($FORM{'area'} ne '' ) &&($FORM{'bbsname'} eq "")) {

	my $defaulttitle = $_[0];
	my $defaultmsg = $_[1];
	my $defaultlink = $_[2];
	&loadmessage;
	&getmessage ( $logdata[0] );
	$postnum=$postid;
	&getmessage ( $logdata[$ends] );
	$bbstitle =$bbs;
	$genre=$mail;

}


		if ( $FORM{'area'} eq 'read' ) 
## original ## {$bbstitle = "最新投稿一覧";}
{$bbstitle = "Latest posts";}

		if ( $FORM{'area'} eq '' ) 
## original ## {$bbstitle = "リスト一覧";}
{$bbstitle = "Topic list";}

		if ( $FORM{'create'} eq 'on' ) 
## original ## {$bbstitle = "トピック作成";}
{$bbstitle = "Create topic";}




## original ## print "<html><head><title>$bbstitle - $mainbbstitle</title><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"></head>\n$body\n";
print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>$bbstitle - $mainbbstitle</title><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n$body\n";



## original ## print "<form method=\"$formmethod\" action=\"$cgiurl\?area\=$FORM{'area'}\">";
print "<form method=\"$formmethod\" action=\"$cgiurl\?area\=$FORM{'area'}\" style=\"margin-bottom:0;\">";


################

$listfont=$linkc;
$saisinfont=$linkc;
$saisincolor=$tcolor;
$listcolor=$tcolor;
$resfont=$linkc;
$rescolor=$tcolor;
$createcolor=$tcolor;
$createfont=$linkc;
##############

		if ( $FORM{'area'} eq '' && $FORM{'create'} ne 'on' ) 
{
$listcolor=$scolor;
$listag='b';
$listfont=$bgc;
}

		if ( $FORM{'area'} eq 'read') 
{
$saisincolor=$scolor;
$saisintag='b';
$saisinfont=$bgc;
}

		if ( $FORM{'create'} eq 'on' ) 
{
$createcolor=$scolor;
$createtag='b';
$createfont=$bgc;
}

		if ( $FORM{'area'} eq '' ) 
{&dirread;
$end--;
}


	print <<"__EOF__";
<!-- ## original ## <table border="0" cellpadding="1" cellspacing="0"  bgcolor="#$tcolor" width=480> -->
<table border="0" cellpadding="1" cellspacing="0"  bgcolor="#$tcolor" width=480>
<tr><td nowrap width=99%>　<font size=+1><b>$mainbbstitle</b></font></td><td>
<table border="0" cellpadding="0" cellspacing="0"  bgcolor="#$tcolor" width=100%><tr><td nowrap>
<table border="0" cellpadding="1" cellspacing="1" bgcolor="#$tcolor" width=100%>

<tr>

<!-- ## original ## <td bgcolor=$listcolor  nowrap align=center>&#160;&#160;<font color=$listfont size=-1><a$listag href=\"$cgiurl\">リスト一覧</font></a>&#160;&#160;</td> -->
<td bgcolor=$listcolor  nowrap align=center>&#160;&#160;<font color=$listfont size=-1><a$listag href=\"$cgiurl\">Topic list</font></a>&#160;&#160;</td>

<!-- ## original ## <td bgcolor=$saisincolor nowrap  align=center>&#160;&#160;<a$saisintag href="$cgiurl?area=read\"><font color=$saisinfont size=-1>最新投稿</font></a></b>&#160;&#160;</td> -->
<td bgcolor=$saisincolor nowrap  align=center>&#160;&#160;<a$saisintag href="$cgiurl?area=read\"><font color=$saisinfont size=-1>Latest posts</font></a></b>&#160;&#160;</td>
	
<!-- ## original ## <td bgcolor=$createcolor nowrap  align=center>&#160;&#160;<a$createtag href="$cgiurl?create=on\"><font color=$createfont size=-1>トピック作成</font></a></b>&#160;&#160;</td> -->
<td bgcolor=$createcolor nowrap  align=center>&#160;&#160;<a$createtag href="$cgiurl?create=on\"><font color=$createfont size=-1>Create topic</font></a></b>&#160;&#160;</td>

<!-- ## original ## <td  nowrap  align=center bgcolor=$tcolor>&#160;&#160;<a href="getlog_m.cgi"><font size=-1>過去ログ検索</a></b>&#160;&#160;</td> -->
<td  nowrap  align=center bgcolor=$tcolor>&#160;&#160;<a href="getlog_m.cgi"><font size=-1>Log search</a></b>&#160;&#160;</td>
	
	
</tr></table></td>
</tr></table></td></tr></table></center><br>
__EOF__
		
				


if ( $FORM{'create'} eq 'on' ) 
{
	&prtform ( $defaulttitle, $defaultmsg, $defaultlink );
	&prtfooter;
}




# Banner goes here

## original ## #if ( $FORM{'area'} eq '' ) {print "<b>最新連絡(12/20)</b>：</font><hr>\n";}
#if ( $FORM{'area'} eq '' ) {print "<b>Latest announcement (2021/10/14)</b>: [your announcement here]</font><hr>\n";} # (TL note: uncomment this line to place an announcement on the topic list page)



		if ( $FORM{'ctr'} eq '') 
{
$FORM{'lists'}="on";
}


		if ( $FORM{'area'} eq '' || $FORM{'area'} eq 'read') 
{


	print <<"__EOF__";
<font size=-1>
<input type="hidden" name="msgdisp" size="6" value="$msgdisp">
<input type="hidden" name="bgcolor" size="6" value="$bgc">
<input type="hidden" name="autolink" value="checked" $FORM{'autolink'}>
<input type="hidden" name="custom" value="$FORM{'custom'}">
<input type="hidden" name="area" value="$FORM{'area'}">
<input type="hidden" name="postid" value="$toppostid">
<!-- <input type="hidden" name="thread" value="$thread">-->
__EOF__
	

}



		if ( $FORM{'area'} eq '') {
			
			
if($FORM{'saikin'} eq "checked")
{
	$saikincolor="bgcolor=$scolor";
    $saikinfont="color=$bgc";
	$FORM{'lists'} ="";
}
elsif($FORM{'res'} eq "checked"){
	$rescolor="bgcolor=$scolor";
    $resfont="color=$bgc";
	$FORM{'lists'} ="";
}
elsif($FORM{'ctr'} eq "")
{


$kousincolor="bgcolor=$scolor";
$kousinfont="color=$bgc";

}


else
{

#$kousincolor="bgcolor=$bgc";
$logcolor="bgcolor=$scolor";
$logfont="color=$bgc";

}


	

if($FORM{'ctr'} eq "" ||$FORM{'saikin'} eq "")
{$check="checked";}


}

#################
		if ( $FORM{'area'} eq '') {

	print <<"__EOF__";
</form>
__EOF__

&timelist;
&prtfooter;
exit;

	}
elsif( $FORM{'area'} eq '' && $FORM{'disp'} eq 'time')

{

&timelist;
&prtfooter;
exit;

}


##########  Add form ##########

		if ( $FORM{'area'} eq '' || $FORM{'area'} eq 'read') 
{
print "</font>\n";

}else
{
print "</font><font size=+1><b>$bbstitle</b></font><p>\n";

}


		if (( $FORM{'area'} ne 'read') && ($FORM{'area'} ne '')) 
{
	&prtform ( $defaulttitle, $defaultmsg, $defaultlink );
	
	$logdata[0] =~ /^.*,(.*),.*,.*,.*,.*,.*,.*,.*,.*/;
	$toppostid = $1;

 print "<input type=\"hidden\" name=\"area\" value=\"$FORM{'area'}\">";

}

##########999f

		if ($FORM{'area'} ne '' ) 
{


	print <<"__EOF__";
<font size=-1>
<!-- ## original ## 表\示件数 <input type="text" name="msgdisp" size="6" value="$msgdisp"> -->
<label for="msgdisp">Posts displayed</label> <input type="text" id="msgdisp" "name="msgdisp" size="2" value="$msgdisp">
<!-- ## original ## 背景色 <input type="text" name="bgcolor" size="6" value="$bgc"> -->
<label for="bgcolor">Background color</label> <input type="text" id="bgcolor" name="bgcolor" size="4" value="$bgc">
<!-- ## original ## 自動リンク <input type="checkbox" name="autolink" value="checked" $FORM{'autolink'}> -->
<label for="autolink">Auto-link URLs</label> <input type="checkbox" id="autolink" name="autolink" value="checked" $FORM{'autolink'}>
<input type="hidden" name="custom" value="$FORM{'custom'}">
<input type="hidden" name="area" value="$FORM{'area'}">
<input type="hidden" name="postid" value="$toppostid">
<!-- <input type="hidden" name="thread" value="$thread">-->
__EOF__
	
}




		if (( $FORM{'area'} ne 'read') && ($FORM{'area'} ne '')) 
{

## original ##	print "&#160;$postnum件の投稿があります。<a href=\"$cgiurl\?area=$FORM{'area'}\&msgdisp=$logsave\&custom\=$FORM{'custom'}\">全件表\示</a><br><br>\n";
	print "&#160;There are $postnum posts.&#160;<a href=\"$cgiurl\?area=$FORM{'area'}\&msgdisp=$logsave\&custom\=$FORM{'custom'}\">Show all</a><br><br>\n";

$g=$FORM{'area'};
$g=~s/[0-9]//g;
	foreach (0 .. $gens)

        	{

if($g eq $genid[$_])
{$genre=$genname[$_];
$gcode=$_;
}

}



## original ## print "<b>「<a href=\"$cgiurl\?disp=genre\&genre=$g\">$genre</a>」</b>";
print "In <b>\"<a href=\"$cgiurl\?disp=genre\&genre=$g\">$genre</a>\"</b>,";


&dirread;
&genre;

# Hit counter processing for individual topics
	
	$countlevel = 1;
    $odate=&getnowdate ($bbsodate );
    if($mon<10){$mon="0$mon";}
    if($mday<10){$mday="0$mday";}
    $odate="$year\/$mon\/$mday";
    $countdate=$odate;
    $odate=~s/\(^//g;
    
    
	$countfile = "./count/$FORM{'area'}";	
	&counter;

	print <<"__EOF__";
<!-- ## original ## に登録中のトピックは$gennum[$gcode]件。$defcount。<a href="getlog_m.cgi?bbsname=$bbstitle">このトピックの過去ログ</a><hr>$glinks -->
there are currently $gennum[$gcode] topics. $defcount.&#160;<a href="getlog_m.cgi?bbsname=$bbstitle">View logs for this topic</a><hr>$glinks
__EOF__


	}

		if ( $FORM{'area'} ne '' ) {
	print <<"__EOF__";
<!-- ## original ## <hr>最大登録件数 : $logsave件&#160;&#160;■ : 返信&#160;&#160;★ : 投稿者の発言サーチ&#160;&#160;◆ : スレッドを表\示</font><p><input type="submit" value="投稿／リロード"></form><hr> -->
<hr>Max posts stored: $logsave posts&#160;&#160;■ : Reply&#160;&#160;★ : Search by user&#160;&#160;◆ : Thread view</font><p><input type="submit" value="Post/Reload"></form><hr>
__EOF__

}

	
	my $msgrd;
	if ( $msgdisp == 0 ) {
		$msgrd = $toppostid - $FORM{'postid'};
		$newmsgonly = 1;
	} else {
		$msgrd = $msgdisp;
		$newmsgonly = 0;
	}
	
	my $msgcount = 0;
	$j = $bmsg + $msgrd;
	$j = @logdata if ( $j > @logdata );
	for ( $i = $bmsg ; $i < $j ; $i++ ) {
		&getmessage ( $logdata[$i] );

		&prtmessage ( 'STDOUT', 0 );
		$msgcount++;
	}
	
	$msgtop = $bmsg + $msgcount;
	$bmsg++;
	if ( $msgcount > 0 ) {
## original ##		print "<p><font size=\"-1\"><i>以上は、現在登録されている新着順$bmsg番目から$msgtop番目までの記事です。";
		print "<p><font size=\"-1\"><i>Shown above are posts $bmsg through $msgtop, in order of newest to oldest.";
	} else {
## original ##		print "<p><font size=\"-1\"><i>未読メッセージはありません。";
		print "<p><font size=\"-1\"><i>There are no unread messages.";
	}


	if ( $logdata[$msgtop] ne '' && $msgcount > 0 ) {
		print <<"__EOF__";
</i></font>
<table><tr><td><br></form>
<form method="post" action="$cgiurl\">
<input type="hidden" name="mode" value="page">
<input type="hidden" name="bmsg" value="$msgtop">
<input type="hidden" name="username" value="$FORM{'username'}">
__EOF__
		
		if ( $newmsgonly ) {
			print "<input type=\"hidden\" name=\"msgdisp\" value=\"30\">\n";
		} else {
			print "<input type=\"hidden\" name=\"msgdisp\" value=\"$msgdisp\">\n";
		}
		
		print <<"__EOF__";
<input type="hidden" name="bgcolor" value="$bgc">
<input type="hidden" name="custom" value="$FORM{'custom'}">
<input type="hidden" name="area" value="$FORM{'area'}">
<input type="hidden" name="autolink" value="$FORM{'autolink'}">
<!-- ## original ## <input type="submit" value="次のページ"></form> -->
<input type="submit" value="Next page"></form>
</td><td><br>
<form method="post" action="$cgiurl\">
<input type="hidden" name="username" value="$FORM{'username'}">
__EOF__
	
		if ( $newmsgonly ) {
			print "<input type=\"hidden\" name=\"msgdisp\" value=\"0\">\n",
			  "<input type=\"hidden\" name=\"postid\" value=\"$toppostid\">\n";
		} else {
			print "<input type=\"hidden\" name=\"msgdisp\" value=\"$msgdisp\">\n";
		}
		
		print <<"__EOF__";
<input type="hidden" name="bgcolor" value="$bgc">
<input type="hidden" name="custom" value="$FORM{'custom'}">
<input type="hidden" name="area" value="$FORM{'area'}">
<input type="hidden" name="autolink" value="$FORM{'autolink'}">
<!-- ## original ## <input type="submit" value="リロード"></form> -->
<input type="submit" value="Reload"></form>
</td></tr>
</table>
__EOF__
		
	} else {
## original ##		print 'これ以下の記事はありません。</i></font>';
		print ' There are no more posts below this point.</i></font>';
	}
	print '</p>';
	
	&prtfooter;
}

#########################################
# Read the latest list file

sub dirread{


## original ##	open ( READLOG, "$totalist" ) || &prterror ( 'メッセージ読み込みに失敗しました' );
	open ( READLOG, "$totalist" ) || &prterror ( 'Failed to read message' );
	eval 'flock ( READLOG, 1 )';
	seek ( READLOG, 0, 0 );
	@set =  <READLOG>;



	
	if ( $FORM{'ctr'} eq 'checked' )
{@set =sort { (split(/\,/,$b))[1] <=> (split(/\,/,$a))[1] } @set ;}

	if ( $FORM{'saikin'} eq 'checked' )
{@set =sort { (split(/\,/,$b))[3] <=> (split(/\,/,$a))[3] } @set ;}


@sot =sort { (split(/\,/,$b))[3] <=> (split(/\,/,$a))[3] } @set;


	if ( $FORM{'res'} eq 'checked' )
{@set=sort @set;
@set=reverse @set;}

	eval 'flock ( READLOG, 8 )';
	close ( READLOG );

	$end=@set;
	$gens--;
	
	$hl--;

		foreach (0 .. $hl)

	{
		
	( $ndate, $postid, $protect, $odate, $bbs, $logname, $user, $genre, $title, $msg )= split ( /\,/, $sot[$_]); 

if ($bbstitle ne $bbs){

     $recentbbs.="\<a href\=\"$cgiurl\?area\=$logname\"\>$bbs\<\/a\> ";

if ($_ ne $hl){$recentbbs.="|";}


}


	}#foreach

	foreach (0 .. $end)

	{

		
	( $ndate, $postid, $protect, $odate, $bbs, $logname, $user, $genre, $title, $msg )= split ( /\,/, $set[$_]); 

$logns=$logname;
$logname=~s/[0-9]//g;

	foreach (0 .. $gens)

        	{

         	  if ($logname eq $genid[$_])

         	  {push @{$genid[$_]},$set[$_]}


        	}# foreach
        		
        	
        	if ($FORM{'area'} ne "" && $FORM{'area'} eq $logns)
        		{ $bbsodate=$odate;
        		  $bbsgenre=$genre;
        		}


	} # foreach


	foreach (0 .. $gens)

        	{


$gennum[$_]=@{$genid[$_];

        	}

        	}

}

#########################################
# Create links of the same genre for individual topics
sub genre{


foreach (0 .. $end)

{

	( $ndate, $postid, $protect, $odate, $bbs , $logname, $user, $genre, $title, $msg)= split ( /\,/, $set[$_]); 


	$logn=$genre;


$zapbbs = $bbs;
$zapbbs=~ s/ぁゃιぃわ\Qー\Eるど//g;
$zapbbs=~ s/あやしいわ\Qー\Eるど//g;
$zapbbs=~ s/あやしいわ－るど//g;
$zapbbs=~ s/ぁゃιぃ//g;
$zapbbs=~ s/^＠//g;
$zapbbs=~ s/^\@//g;

if($logn eq $genid[$gcode])
{$glinks.=" <a href=\"$cgiurl\?area=$logname\">$zapbbs</a> ｜";


        	}

}


}

#########################################
# Create list of data files in order of recently updated
sub timelist{


$i=1;
$keywords = quotemeta($FORM{'keyword'});

# Plagiarizing Yui Note's page break processing

	$page = $FORM{page};
	$page=0 unless($page);
	$lmax = $FORM{lm};
	$lmax=$lmaxdef unless($lmax);# How much should be displayed on one page?
	$page2 = $page*$lmax;
	$page3 = $page2+$lmax-1;



	$total = @set;
	$count = int(($total-1)/$lmax);

unless ($FORM{'genre'} || $FORM{'keyword'}){

	for($i=0;$i<=$count;$i++){

$startdisp=$i*$lmax;
$startdisp++;
$t=$i+1;
$enddisp=$t*$lmax;


	        if($i eq $page){$disp = $i + 1; $prin.= " \[\<b\>$disp\<\/b\>\]";}else{
			$disp = $i + 1;

$startdisp=$i*$lmax;
$startdisp++;
$enddisp=$disp*$lmax;
	                $prin.="\ [\<A HREF\=\"$url\?page\=$i\&lm\=$lmax\"\>$disp<\/A\>\]";
	        }
	} # for

	} # unless

$i=0;

# End of plagiarization


$adaysec=1 * 86400;




#####　Putting the topic list into cells

        	if($FORM{'genre'}  ne ""){$page2=0;$page3=$total;}


	foreach ($page2 .. $page3)


{

	( $ndate, $postid, $protect, $odate, $bbs , $logname, $user, $genre, $title, $msg)= split ( /\,/, $set[$_]); 

         	 if($ndate eq ""){last;}

	$logn=$genre;

	foreach (0 .. $gens)

        	{

         	  if ($logn eq $genid[$_])

         	  {

         	  $n=$genname[$_];
         	  $z=$genid[$_];

         	  };


        	}



	$wodate = &getnowdate ( $odate );
	$omon=$mon;
	$omday=$mday;
	$odate4 = sprintf ( "%02d\:%02d", 

		$hour, $min, );
		

$mday2=$mday;
$wdate = &getnowdate ( $ndate );

	$wdate4 = sprintf ( "%02d\:%02d", 

		$hour, $min, );
		

$cdate= $nowtime - $ndate;
$codate= $nowtime - $odate;



if ($bgc ne $bgk ){
$cccc="\&custom\=$FORM{'custom'}\&autolink=$FORM{'autolink'}";
}

$startnum--;
$startnum--;
$lastnum--;
$lastnum--;




if(($keywords ne "")&&($bbs=~ /$keywords/))
{$keys=1;}
elsif(($FORM{'genre'}  eq "$logn") &&($FORM{'genre'} ne ""))
{$keys=1;}
elsif(($FORM{'keyword'} eq "")&&($FORM{'genre'} eq ""))
{$keys=1;}


if($keys eq 1){



$amari=$s%2;
if($amari==0){
$celcolor=$bgc;
}else{
$celcolor=$sbgc;}






if ($cdate < $adaysec)
{$wdates2= "<font size =-1 color=$scolor>$wdate4</font>\n";}
else{$wdates2= "<font size =-1>$mon\/$mday</font>\n";}


if ($codate < $adaysec)
{$odates2= "<font color=$scolor size =-1>$odate4</font>\n";}
else{$odates2= "<font size=-1>$omon\/$omday</font>\n";}


$bbsnames2= "<a href=\"$cgiurl\?area\=$logname\"><font size=-1>$bbs</a></font>\n";


$msgss2= "<font size=-1>$postid</font>\n";

$msgnames2= "<font size=-1>$msg</font>\n";

$genre2= "<font size=-1><a href=\"$cgiurl\?genre\=$z\">$n</font></a>\n";

$s++;
$keys=0;





$all.="<tr bgcolor=$celcolor><td nowrap align=right>$wdates2</td><td nowrap>$bbsnames2</td><td align=center nowrap>$msgss2</td><td nowrap>$msgnames2</td><td nowrap>$genre2</td><td nowrap>$odates2</td></tr>";



}#  if($keys eq 1) end



}# foreach end   # End of topic list cell creation

$i--;
$end--;


$lastnum--;


# Create cells for the "all genres" view

	foreach (0 .. $gens)


		{

        	if($FORM{'genre'}  eq $genid[$_]){

## original ##			$genlist.="<span style=\"background-color\: $scolor\"><font color=$bgc>$genname[$_]</font></span></b> <font color=$scolor>$gennum[$_]</font></b><font size=+1 color=$bgc>■</font>";
			$genlist.="<span style=\"background-color\: $scolor\"><font color=$bgc>$genname[$_]</font></span></b> <font color=$scolor style=\"margin-right:1.5em\">$gennum[$_]</font></b>";


					}else{
## original ##			$genlist.="<a href=$cgiurl?genre=$genid[$_]>$genname[$_]</a> <font color=$scolor>$gennum[$_]</font><font size=+1 color=$bgc>■</font>";}
			$genlist.="<div style='display:inline-block;line-height:1.7'><a href=$cgiurl?genre=$genid[$_]>$genname[$_]</a> <font style='margin-right:1.5em' color=$scolor>$gennum[$_]</font></div>";}



        	}

# Creation finished

        	if($FORM{'genre'}  eq ""){

## original ##			$allgen ="\<span style=\"background-color\: $scolor\">\<font color\=$bgc>全て\</font\>\<\/span\>";
			$allgen ="\<span style=\"background-color\: $scolor\">\<font color\=$bgc>All\</font\>\<\/span\>";


					}else{
## original ##			$allgen="\<a href=$cgiurl\>全て\<\/a\>  ";}
			$allgen="\<a href=$cgiurl\>All\<\/a\>  ";}




	print <<"__EOF__";
</font></font></font></font></font></center>
<table border=0 cellpadding=1 cellspacing=0  width=480><tr><td>
<!-- ## original ## <font size=-1>最近、作られたトピック<br>$recentbbs</font><br> -->
<font size=-1>Recently created topics<br>$recentbbs</font><br>
</td></tr></table><br>
<table border=0 cellpadding=1 cellspacing=0  width=480><tr><td bgcolor=$scolor><table border=0 cellpadding=4 cellspacing=0 bgcolor=$bgc width=100%><tr><td><font size=-1>
$genlist
$allgen
<font color=$scolor>$total</font>
</td><td>
</tr>
</table></td></tr></table>
<br>
<table border=0 cellpadding=0 cellspacing=0   width=480><tr><td ><table border=0 cellpadding=4 cellspacing=0 bgcolor=$bgc width=100%><tr><td>
<!-- ## original ## <tr><td nowrap> -->
<!-- ## original ## <form method="get" action="$cgiurl">トピック -->
<form method="get" action="$cgiurl" style="margin-bottom:0;"><label for="topicsearch">Topic</label>
<input id="topicsearch" type="text" name="keyword" value="$FORM{'keyword'}"  size="24">
<!-- ## original ## </font><input type="submit" value="検索／リロード"> -->
</font><input type="submit" value="Search/Reload">
</td><td>$prin
</td>
</tr>
</table></td></tr></table>
<br>
<table border=0 cellpadding=0 cellspacing=0  width=480><tr><td bgcolor=$scolor>
<table border=0 cellpadding=4 cellspacing=0  bgcolor=$bgc width=100%>
<!-- ## original ## <tr bgcolor=$tcolor><td nowrap align=center $kousincolor><a$FORM{'lists'}  href=\"$cgiurl?custom=$FORM{'custom'}&autolink=$FORM{'autolink'}\&genre=$FORM{'genre'}\"><font $kousinfont size=-1>更新時</font></a></b></td> -->
<tr bgcolor=$tcolor><td nowrap align=center $kousincolor><a$FORM{'lists'}  href=\"$cgiurl?custom=$FORM{'custom'}&autolink=$FORM{'autolink'}\&genre=$FORM{'genre'}\"><font $kousinfont size=-1>Updated</font></a></b></td>
<!-- ## original ## <td nowrap align=left><font size=-1>トピック名</td><td $logcolor nowrap align=center><a$FORM{'ctr'} href=\"$cgiurl\?ctr=checked\&custom\=$FORM{'custom'}\&genre=$FORM{'genre'}\"><font $logfont size=-1>投稿数</a></b></td><td nowrap align=center width=50%><font size=-1>最終投稿内容</td><td nowrap align=left width=50%><font size=-1>ジャンル</font></font></td><td nowrap align=center width=50%  $saikincolor><a$FORM{'saikin'} href=\"$cgiurl\?saikin=checked\&custom\=$FORM{'custom'}\&genre=$FORM{'genre'}\"><font $saikinfont size=-1>初投稿時</a></b></td></tr> -->
<td nowrap align=left><font size=-1>Topic name</td><td $logcolor nowrap align=center><a$FORM{'ctr'} href=\"$cgiurl\?ctr=checked\&custom\=$FORM{'custom'}\&genre=$FORM{'genre'}\"><font $logfont size=-1>Posts</a></b></td><td nowrap align=center width=50%><font size=-1>Latest post</td><td nowrap align=left width=50%><font size=-1>Genre</font></font></td><td nowrap align=center width=50%  $saikincolor><a$FORM{'saikin'} href=\"$cgiurl\?saikin=checked\&custom\=$FORM{'custom'}\&genre=$FORM{'genre'}\"><font $saikinfont size=-1>Created</a></b></td></tr>
$all
</table></td></tr></table></form><br><table border=0 cellpadding=1 cellspacing=0  width=88%><tr><td>
__EOF__



$end++;
$end++;

if ($FORM{'genre'} ne ""){



	foreach (0 .. $gens)

        	{

if($FORM{'genre'} eq $genid[$_])
{$genre=$genname[$_]}

}


## original ##	print "<font size=-1>ジャンル「$genre」に</font>";
	print "<font size=-1>In the &quot;$genre&quot; genre, </font>";

}
elsif ($FORM{'keyword'} ne ""){

## original ##	print "<font size=-1>「$FORM{'keyword'}」を含む</font>";
	print "<font size=-1>Regarding those that include the term &quot;$FORM{'keyword'}&quot;, </font>";

}
else{

$page2++;
$page4=$page2+$s-1;

## original ##	print "<font size=-1>$page2件から$page4件までを\表\示。現在、</font>";
	print "<font size=-1>Displaying items $page2 - $page4, </font>";

$s=$total;

}

$s=0 unless($s);

	
	$countfile = './count/count';	
	&counter;
	

## original ##	print "<font size=-1>登録されているトピックは$s件です。<br>$delete日以上書きこみがないと削除しますが、$enmei件の投稿につき1日延命します。<br>
	print "<font size=-1>there are currently $s registered topics.<br>Topics are automatically removed if they receive no new posts for $delete days. The time until removal will be extended by 1 day for every $enmei new posts received.<br>
$defcount
</font></td></tr>
</table></center>";



}




#########################################

###############################################################################
#  Main
###############################################################################

srand ( time | $$ );

&getformdata;
&getenv;

if ( $FORM{'mode'} eq 'customset' ) {
	require './bbscust.cgi';
	&setcustom;
	exit;
}
if ( $FORM{'custom'} ne '' ) {
	$FORM{'custom'} =~ /^(\w\w\w\w\w\w)(\w\w\w\w\w\w)(\w\w\w\w\w\w)(\w\w\w\w\w\w)(\d+)$/;
	$textc = $1;
	$bgc = $2;
	$linkc = $3;
	$vlinkc = $4;
	$i = $5;
	$followwin = int ( $i / 2 );
} else {
	$i = $followwin * 2;
	$FORM{'custom'} = "$textc$bgc$linkc$vlinkc$i";
	if ( ! $FORM{'autolink'} && $autolink eq '1' ) {
		$FORM{'autolink'} = 'checked';
	}
}

if ( $FORM{'bgcolor'} ne '' ) {		$bgc = $FORM{'bgcolor'};
	}



$body = "<body bgcolor=\"#$bgc\" $bkg text=\"#$textc\" link=\"#$linkc\" " .
		"vlink=\"#$vlinkc\" alink=\"#$alinkc\">";
## original ## if ( $FORM{'btnname'} eq '環境設定' ) {
if ( $FORM{'btnname'} eq 'Settings' ) {
	require './bbscust.cgi';
	&prtcustom;
	exit;
}



# Header output

print "Content-type: text/html\n";

if ( $gzip && ( $ENV{'HTTP_ACCEPT_ENCODING'} =~ /gzip/ ) ) {

	print "Content-encoding: gzip\n\n";

	open ( STDOUT, "| $gzip -1 -c" );

} else {

	print "\n";

}



if ( $FORM{'msgdisp'} ne '' ) {
	if ( $FORM{'msgdisp'} > $logsave ) {
		$msgdisp = $logsave;
	} else {
		$msgdisp = $FORM{'msgdisp'};
	}
}

$nowtime = time - $difftime * 60 * 60;

if ( $FORM{'mode'} eq 'post' && $FORM{'message'} ne '' ) {

$t=t;

if ( $FORM{'area'} eq '' ){
	

    # Hit counter bulletproof level (TL note: number of count files used to ensure accurate readings; more count files = greater accuracy, at the cost of greater server load. I recommended not exceeding 3-5)
    $countlevel = 3;
	
	$countfile = './bbsnum/count';
	
	&counter;
	

	$logfilename ="./data/$FORM{'areaname'}00$count.dat";
	$FORM{'area'}="$FORM{'areaname'}00$count";
	

}
    
	require './bbsreg.cgi';
	
	
## original ## #print "書きこみは$logfilenameにされました。";
#print "$logfilename has been written to.";
	
    $postid = 0;
	$posterr = 0;

	if ( $ENV{'CONTENT_TYPE'} eq 'application/x-www-form-urlencoded' ) {
		&chkmessage;
		&putmessage;
		&totalmessage;
		&totalist;

	} else {
		$posterr = 255;
	}
	if ( $FORM{'follow'} && $followwin == 0 ) {
		print <<"__EOF__";

<!-- ## original ## <html><head><META http-equiv="Content-Type" content="text/html; charset=Shift_JIS"><title>$bbstitle</title></head> -->
<html lang="ja"><head><meta name="viewport" content="width=device-width, initial-scale=1"><META http-equiv="Content-Type" content="text/html; charset=Shift_JIS"><title>$bbstitle</title><style>body{font-family:"MS PGothic",sans-serif;}pre{font-family:"MS Gothic",monospace;}@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>
$body
<!-- ## original ## <h3>書き込み完了</h3> -->
<h3>Write complete</h3>
__EOF__
#exit;
	}
} elsif ( $FORM{'mode'} eq 'follow' ) {
	&prtfollow ( 0 );
} elsif ( $FORM{'mode'} eq 'search' || $FORM{'mode'} eq 'thread' ) {
	require './bbssrc.cgi';
	&srcmessage;
} else {
	if ( $FORM{'mode'} eq 'page' ) {
		$bmsg = $FORM{'bmsg'};
		$msgdisp = $FORM{'msgdisp'};
	} else {
		$bmsg = 0;
	}
}

&prtboard ( '', '', '' );

exit;


__END__
