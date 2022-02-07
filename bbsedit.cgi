#! /usr/bin/perl
###################################################################################
#
#  General-purpose bulletin board data editing script  bbsedit.cgi
#
#    bbsedit.cgi ---- (705)
#
#    REQUIRED jcode.pl (Japanese character encoding conversion library) 
#
####################################################################################

require   './jcode.pl';     #----- Japanese character encoding conversion library
$reload   = 'bbsedit.cgi';  #----- URL of your script
$method   = 'post';         #----- Set the input formatting, post or get
##original## $amp      = 'sakuraiasahi';     #----- システムパスワード
$amp      = 'pass';         #----- System password

#------------------------------------------
# Fetch sent data
#------------------------------------------

#----- Import POST (or GET) data into $postdata
if( $ENV{'REQUEST_METHOD'} eq "POST" ) { 
	read( STDIN, $postdata, $ENV{'CONTENT_LENGTH'} ); 
}
else { 
	$postdata = $ENV{'QUERY_STRING'}; 
}

#----- Disassemble $postdata
@parms = split(/&/,$postdata);
foreach $parm (@parms) {

	($name, $value) = split(/=/, $parm);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ s/\n//g;

	#-----Unify data with S-JIS
	&jcode'convert(*value,'sjis');

	$FORM{$name} = $value;
}

#-----For control
$action   = $FORM{'action'};
$pword    = $FORM{'pword'};

#-----Other
$fname    = $FORM{'fname'}; 
$kcode    = $FORM{'kcode'}; 
$recno    = $FORM{'recno'}; 
$wtext    = $FORM{'wtext'}; 

#-----Password check
if( $action ne "" ) {
	if( $pword eq ""   ) { &error( 3 ); }
	if( $pword ne $amp ) { &error( 4 ); }
}

#----- If $action is empty, put strt in it
if( $action eq '' ) { $action = 'strt'; }

#------------------------------------------
# Process branching
#------------------------------------------

if( $action eq 'strt' ) { &bbsedit; }
if( $action eq 'edit' ) { &edit_file; }
if( $action eq 'updt' ) { &updt_file; }

if( $action eq 'list' ) { &list_file; }

exit;

#-----------------------------------------------------------------------------
#
# Start screen
#
#-----------------------------------------------------------------------------
sub bbsedit {

	#-----Start HTML output
	print "Content-type: text/html\n\n";
	## original ## print "<html><head><title>BBS-EDIT</title></head>\n";
	print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>BBS-EDIT</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n";
	print "<body bgcolor=#F0F0C0 text=#000000>\n";
	print "<font size=6>BBS EDIT</font><hr><pre>";
	$html = 1;
	
	#-----Form
	print "<form method=$method action=\"$reload\">\n";

	print "<input type=hidden name=\"action\" value=\"list\">";
## original ##	print "システムパスワード　：<input type=text name=\"pword\" value=\"$pword\" size=20>\n";
	print "<label for=\"pword\">System password</label>:　　　　　　<input type=text id=\"pword\" name=\"pword\" value=\"$pword\" size=20> (set password in bbsedit.cgi)\n";
## original ##	print "相対パスとファイル名：<input type=text name=\"fname\" value=\"$fname\" size=50>\n";
	print "<label for=\"fname\">Relative path and file name</label>:<input type=text id=\"fname\" name=\"fname\" value=\"$fname\" size=50> (e.g. \"./data/other0064.dat\")\n";
## original ##	print "データの漢字コード　：";
	print "<label for=\"kcode\">Character encoding of data</label>: ";
		print "<select id=\"kcode\" name=\"kcode\" >";
## original ##		print "<option value=1 "; if( $kcode == 1 ) { print "selected"; } print ">ＥＵＣ";
		print "<option value=1 "; if( $kcode == 1 ) { print "selected"; } print ">EUC-JP";
## original ##		print "<option value=2 "; if( $kcode == 2 ) { print "selected"; } print ">ＪＩＳ";
		print "<option value=2 "; if( $kcode == 2 ) { print "selected"; } print ">JIS";
## original ##		print "<option value=3 "; if( $kcode == 3 ) { print "selected"; } print ">ＳＪＩＳ";
		print "<option value=3 "; if( $kcode == 3 ) { print "selected"; } print ">Shift JIS";
## original ##		print "</select>\n";
		print "</select> (most likely Shift JIS)\n";
## original ##	print "<input type=submit value=\"  編集  \">\n";
	print "<input type=submit value=\"Edit\">\n";
	print "</form>";

	print "</pre></body></html>";

	exit;
}

#-----------------------------------------------------------------------------
# Display list of records
#-----------------------------------------------------------------------------
sub list_file {

	#-----Start HTML output
	print "Content-type: text/html\n\n";
	## original ## print "<html><head><title>BBS-EDIT</title></head>\n";
	print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>BBS-EDIT</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n";
	print "<body bgcolor=#F0F0C0 text=#000000>\n";
	print "<font size=6>BBS EDIT</font><hr>";
	$html = 1;

	#-----Guidance
	print "<table><tr>";
	print "<td><pre>";
	print "File being edited　　　　 : $fname \n";
	print "Source character encoding : ";
	## original '' if( $kcode == 1 ) { print "ＥＵＣ"; }
	if( $kcode == 1 ) { print "EUC-JP"; }
	## original ## if( $kcode == 2 ) { print "ＪＩＳ"; }
	if( $kcode == 2 ) { print "JIS"; }
	## original ## if( $kcode == 3 ) { print "ＳＨＩＦＴ－ＪＩＳ"; }
	if( $kcode == 3 ) { print "Shift JIS"; }
	print "</pre></td>";

	#-----Return button
	print "<td>";
	print "<form method=$method action=\"$reload\">";
	print "<input type=hidden name=\"action\" value=\"strt\">";
	print "<input type=hidden name=\"pword\"  value=\"$pword\">";
	print "<input type=hidden name=\"fname\"  value=\"$fname\">";
	print "<input type=hidden name=\"kcode\"  value=\"$kcode\">";
	## original ## print "<input type=submit value=\"  戻る  \">\n";
	print "<input type=submit value=\"Return\">\n";
	print "</form>\n";
	print "</td>";
	print "</tr></table>";

	#-----Read file
	if( !open( DB,"$fname" )) { &error( 1 ); }
	flock( DB, 2 );
	@recs = <DB>;
	flock( DB, 8 );
	close( DB );

	#-----Display
	print "<table>";
	$recno = 1;
	foreach $rec ( @recs ) {

		$rdata = $rec;

		#-----Character encoding conversion
		&jcode'convert( *rdata, 'sjis' );

		#-----Control code conversion
		$rdata =~ s/\0/\(_NULL_\)/g;
		$rdata =~ s/</&lt;/g;
		$rdata =~ s/>/&gt;/g;

		print "<tr>";
		print "<td bgcolor=#FFC0C0>";
		print "<a href=\"$reload".'?'."action=edit&pword=$pword&";
		$a = $fname; $a =~ s/\./%2e/g;
## original ##		print "fname=$a&kcode=$kcode&recno=$recno\">EDIT\n($recno)</a>";
		print "fname=$a&kcode=$kcode&recno=$recno\">Edit\n($recno)</a>";
		print "</td>";
		print "<td bgcolor=#C0C0FF>";
		print "<pre>$rdata</pre>";
		print "</td>";
		print "</tr>";

		$recno ++;
	}

	print "</table>";

}

#-----------------------------------------------------------------------------
# Editing
#-----------------------------------------------------------------------------
sub edit_file {

	#-----Start HTML output
	print "Content-type: text/html\n\n";
	## original ## print "<html><head><title>BBS-EDIT</title></head>\n";
	print "<html lang=\"ja\"><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>BBS-EDIT</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n";
	print "<body bgcolor=#F0F0C0 text=#000000>\n";
	print "<font size=6>BBS EDIT</font><hr>";
	$html = 1;

	#-----Guidance
	print "<table><tr>";
	print "<td><pre>";
## original ##	print "編集対象ファイル : $fname \n";
	print "File being edited　　　　 : $fname \n";
## original ##	print "元の漢字コード   : ";
	print "Source character encoding : ";
## original ##	if( $kcode == 1 ) { print "ＥＵＣ"; }
	if( $kcode == 1 ) { print "EUC-JP"; }
## original ##	if( $kcode == 2 ) { print "JIS"; }
	if( $kcode == 2 ) { print "ＪＩＳ"; }
## original ##	if( $kcode == 3 ) { print "ＳＨＩＦＴ－ＪＩＳ"; }
	if( $kcode == 3 ) { print "Shift JIS"; }
	print "\n";
	print "Target record number : $recno";
	print "\n";
	print "To go back, use the \"Back\" button on your browser.";
	print "\n";
	print "</pre></td>";

	print "</tr></table>";

	#-----Read file
	if( !open( DB,"$fname" )) { &error( 1 ); }
	flock( DB, 2 );
	@recs = <DB>;
	flock( DB, 8 );
	close( DB );

	#-----Extract from record
	$wtext = $recs[ $recno - 1 ];

	#-----Character encoding conversion
	&jcode'convert( *wtext, 'sjis' );

	#-----Control code conversion
	$wtext =~ s/\0/\(_NULL_\)/g;
	$wtext =~ s/\t/\(_TAB_\)/g;
	$wtext =~ s/\r/\(_LF_\)/g;
	$wtext =~ s/\n/\(_CRLF_\)/g;
	$wtext =~ s/</\(_&LT_\)/g;
	$wtext =~ s/>/\(_&GT_\)/g;

	#-----Editing area
	print "<form method=$method action=\"$reload\">";
	print "<input type=hidden name=\"action\" value=\"updt\">";
	print "<input type=hidden name=\"pword\"  value=\"$pword\">";
	print "<input type=hidden name=\"fname\"  value=\"$fname\">";
	print "<input type=hidden name=\"kcode\"  value=\"$kcode\">";
	print "<input type=hidden name=\"recno\"  value=\"$recno\">";
	print "<textarea name=\"wtext\" rows=10 cols=80>$wtext</textarea>";
## original ##	print "<input type=submit value=\"  更新  \">\n";
	print "<input type=submit value=\"Update\">\n";
	print "</form>\n";

	#-----Operating guide
	print "<hr><pre>";
## original ##	print "○ 編集上の注意\n";
	print "○ Notes on editing\n";
	print "   \n";
## original ##	print "   以下の制御文字は表\示/更新で相互変換されます。相互変換用文字列が記事の中に含まれ\n";
	print "   The following control characters are converted to each other when updating.\n";
## original ##	print "   ていないかどうかに注意して下さい。(普通は無いと思います)\n";
	print "   Please note whether the string for mutual conversion is included in the post or not. (Usually they aren\'t.)\n";
	print "   \n";
	print "   \\0   ←→ (_NULL_)             \n";
	print "   \\t   ←→ (_TAB_)              \n";
	print "   \\r   ←→ (_LF_)               \n";
	print "   \\n   ←→ (_CRLF_)             \n";
	print "   \n";
## original ##	print "   ブラウザによる差異を吸収するため、タグ文字も相互変換されます。\n";
	print "   Tag characters are also converted to each other to absorb the differences between browsers.\n";
	print "   \n";
	print "   &lt;  ←→　(_&LT_)             \n";
	print "   &gt;  ←→　(_&GT_)             \n";
	print "   \n";
## original ##	print "   これらの特殊文字を入力する場合は、相互変換文字列を入力すれば記録できます。\n";
	print "   If you want to enter these special characters, you can write them by entering a mutual conversion string.\n";
	print "   \n";
## original ##	print "   BBSでの表\示を改行させたい場合(\\r)は (_LF_) を、レコード区切りとしての改行(\\n)\n";
	print "   Enter (_LF_) if you want to start a new line on the BBS page (\\r), \n";
## original ##	print "   を入れる場合は (_CRLF_) を入力して下さい。\n";
	print "   or enter (_CRLF_) if you want to insert a line break (\\n) as a record delimiter.\n";
	print "   \n";
	print "</pre></body></html>";

	exit;
}
#-----------------------------------------------------------------------------
#
# Updating
#
#-----------------------------------------------------------------------------
sub updt_file {

	#-----Character encoding conversion
	if( $kcode == 1 ) { &jcode'convert( *wtext, 'euc' ); }
	if( $kcode == 2 ) { &jcode'convert( *wtext, 'jis' ); }
	if( $kcode == 3 ) { &jcode'convert( *wtext, 'sjis' ); }

	#-----Control code conversion
	$wtext =~ s/\(_NULL_\)/\0/g;
	$wtext =~ s/\(_TAB_\)/\t/g;
	$wtext =~ s/\(_LF_\)/\r/g;
	$wtext =~ s/\(_CRLF_\)/\n/g;
	$wtext =~ s/\(_&LT_\)/</g;
	$wtext =~ s/\(_&GT_\)/>/g;

	#-----Read file
	if( !open( DB,"$fname" )) { &error( 1 ); }
	flock( DB, 2 );
	@recs = <DB>;
	flock( DB, 8 );
	close( DB );

	#-----Set
	$recs[ $recno - 1 ] = $wtext;

	#-----Write
	if( !open( DB,">$fname" )) { &error( 2 ); }
	flock( DB, 2 );
	print DB @recs;
	flock( DB, 8 );
	close( DB );
	
	#-----Go to list view
	$action = "list";
	return;

}
#-----------------------------------------------------------------------
# Error handling
#
#   in : Error code in argument
#
#-----------------------------------------------------------------------
sub error {

	$erc = $_[0];

## original ##	if ($erc eq "1") { $e_msg = '対象ファイルの読込エラー'; }
	if ($erc eq "1") { $e_msg = 'Error reading the target file'; }
	if ($erc eq "2") { $e_msg = 'Error writing to the target file'; }
	if ($erc eq "3") { $e_msg = 'Password not entered'; }
	if ($erc eq "4") { $e_msg = 'Password incorrect'; }

	if( $html == 0 ) {
		print "Content-type: text/html\n\n";
## original ##		print "<html><head><title>BBS-EDIT</title></head>";
		print "<html lang=\"ja\"><head><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>BBS-EDIT</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n";
		print "<body bgcolor=#F0F0C0>\n";
	}

	print "<font size=6>Error : $e_msg</font><br>";
	print "</body>";
	print "</html>\n";
	exit;
}

#############################################################################
# End_of_script
#############################################################################

