#! /usr/bin/perl
#
#	KuzuhaScripr Final Beta #2 pl0.3
#	 (Registration functions)
#

###############################################################################
#  Message check
###############################################################################

sub chkmessage {

	if ( ! ( $referer =~ /$cgiurl/i ) ) {
## original ##		&chkerror ( "投稿画面のＵＲＬが<br>$cgiurl<br>" .
## original ##		  '以外からの投稿はできません。',  3 );
		&chkerror ( "Posting is only possible if the<br>" .
		  "post form's URL is $cgiurl",  3 );
	}
	
	$i = 0;
	foreach ( split ( /\r/, $FORM{'message'} ) ) {
		if ( length ( $_ ) > $maxmsgcol ) {
			$i++;
		}

	}

## original ##	if ( $i != 0 ) { &chkerror ( '投稿内容の桁数が大きすぎます。', 10 ); }
	if ( $i != 0 ) { &chkerror ( 'One or more lines of your post are too long, please use line breaks to format your post.', 10 ); }
	if ( ( $FORM{'message'} =~ tr/\r/\r/ ) > ( $maxmsgline - 1 ) ) {
## original ##		&chkerror ( '投稿内容の行数が大きすぎます。', 11 );
		&chkerror ( 'There are too many lines in your post.', 11 );

	}



#if  ( $FORM{'area'} eq  '' || $FORM{'code'} eq '') {

## original ## #		&chkerror ( '題名は必ず記入してください。', 14 );
#		&chkerror ( 'Please enter a title, it is a required field.', 14 );

#	}

	if ( length ( $FORM{'message'} ) > $maxmsgsize ) {
## original ##		&chkerror ( '投稿内容が大きすぎます。', 12 );
		&chkerror ( "The content of the post is too large.", 12 );
	}

	if ( $FORM{'protect'} ne '' ) {

		my @hostbin = split ( /\./, $ENV{'REMOTE_ADDR'} );
		for ( $i = 0 ; $i < 4 ; $i++ ) {
			$hostbin[$i] = vec ( pack ( 'C4', $hostbin[$i] ), 0, 8 );

		}

		$protect_c = $hostbin[0] ^ $hostbin[1] ^ $hostbin[2] ^ $hostbin[3];

		$pcheck = ( $FORM{'protect'} - $protect_c ) / $protect_b - $protect_a;

		&getnowdate ( $pcheck );

		if ( ( $sec  < 0 ) || ( $sec  > 60 ) || 
		  ( $min  < 0 ) || ( $min  > 60 ) ||
		  ( $hour < 0 ) || ( $hour > 24 ) ) {

			&chkerror ( '', 32 );

		}

		if ( ( $nowtime - $pcheck ) < $pstime ) {
## original ##			&chkerror ( 'もう一度やり直して下さい。', 30 );
			&chkerror ( 'Please try again.', 30 );
		}

		if ( ( $nowtime - $pcheck ) > $pltime ) {

			&chkerror ( '', 31 );

			if ( $FORM{'follow'} ne '' ) {
				&prtfollow ( 1 );
			} else {

				&prtboard ( $FORM{'title'}, $FORM{'message'}, $FORM{'linkurl'} );
			}

			exit;

		}

	} else {

## original ##		&chkerror ( 'フォームデータの一部に欠落があります。もう一度やり直して下さい。', 33 );
		&chkerror ( 'There are one or more faults in the form data. Please try again.', 33 );

	}

	

	if ( $FORM{'mailaddr'} =~ / /i ) {

		$FORM{'mailaddr'} = '';

	}

	if ( $FORM{'mailaddr'} ne '' ) {

		if ( ! ( $FORM{'mailaddr'} =~ /(.*)\@(.*)\.(.*)/ ) ) {

## original ##			&chkerror ( 'メールアドレスが正しく入力されていません。', 20 );
			&chkerror ( 'Your email address has not been entered correctly.', 20 );

		} elsif ( $FORM{'mailaddr'} =~ /,/ ) {

## original			&chkerror ( 'メールアドレスは複数指定できません。', 21 );
			&chkerror ( 'You cannot specify multiple email addresses', 21 );

		}

	}

	

	if ( $FORM{'title'} eq '' ) {

		$FORM{'title'} = '　';

	}

	

	if ( $FORM{'username'} eq '' ) {

		$FORM{'username'} = '　';

	}

	
## original## if ( crypt ( "[$FORM{'username'}]", 'r7' ) eq $adminpost ) {
	if ( crypt ( $FORM{'username'}, 'r7' ) eq $adminpost ) {

		$FORM{'username'} = $adminname;
		$FORM{'mailaddr'} = $adminmail;

	} else {

		if ( $FORM{'username'} eq $adminpost ) {
## original ##			$FORM{'username'} = "$adminname（ハカー）";
			$FORM{'username'} = "$adminname (hacker)";

		}

		if ( $FORM{'username'} =~ /$adminname/i ) {

			my $admincheck = $FORM{'username'};
			$admincheck =~ s/ //g;
			$admincheck =~ s/　//g;
			$admincheck =~ s/_//g;

			if ( $admincheck eq $adminname ) {

# original ##				$FORM{'username'} =~ s/$adminname/$adminname（騙り）/;
				$FORM{'username'} =~ s/$adminname/$adminname (fraudster)/;

			}

		}

	}

	

	if ( $autolink eq '1' ) {

		$FORM{'message'} =~ s#((https?|ftp|gopher|telnet|whois|news)://(=[\x21-\xfc]+|[\x21-\x7e])+)#<a href="$1" target="link">$1</a>#ig;

	}

	

	if ( $FORM{'linkurl'} =~ '^\w+\:\/\/$' || $FORM{'linkurl'} =~ /\s+/ || $FORM{'linkurl'} eq '' ) {

		$FORM{'linkurl'} = '';

	} else {

		$FORM{'linkurl'} =~ s/http:\/\/http:\/\//http:\/\//;

		$FORM{'message'} .= "\r\r<a href=\"$FORM{'linkurl'}\" target=\"link\">$FORM{'linkurl'}</a>";

	}

	if ( $FORM{'follow'} ne '' ) {
		( $i, $j ) = split ( /:/, $FORM{'follow'} );
## original ##		$FORM{'message'} .= "\r\r<a href=\"$cgiurl\?mode=follow\&code=$FORM{'code'}\&search=$i\&ref=$j\">参考：$j</a>";
		$FORM{'message'} .= "\r\r<a href=\"$cgiurl\?mode=follow\&code=$FORM{'code'}\&search=$i\&ref=$j\">Reference: $j</a>";
	}


#######	

@lines=split(/\r/,$FORM{'message'});

if ($lines[0] eq ""){$lines[0] =0;}
if ($lines[1] eq ""){$lines[1]= 1;}
if ($lines[2] eq ""){$lines[2] =2;}

if ( $lines[0] eq $lines[1] ||  $lines[1] eq $lines[2] ||  $lines[1] eq $lines[3]) { 

## original ## &chkerror ( "エラーが発生しました。", 100 );
&chkerror ( "An error has occurred.", 100 );

 }

#######	
}

###############################################################################

#  Message check error handling

###############################################################################



sub chkerror {

	

	my $errstr = $_[0];
	$posterr = $_[1];

	&prterror ( $errstr ) if ( $errstr ne '' );

}

###############################################################################

#  Registering a message

###############################################################################



sub putmessage {


	open ( FLOG, "+<$logfilename" ) || &create;
	eval 'flock ( FLOG, 2 )';
	seek ( FLOG, 0, 0 );
	@logdata = <FLOG>;
	

	$i = 0;
	$posterr = 0;

	while ( $i < $logsave && $posterr == 0 ) {
		@items = split ( /\,/, $logdata[$i] );
		$items[9] =~ s/\n$//;
		$posterr = 1 if ( $i < $checkcount && $FORM{'message'} eq $items[9] );
		$posterr = 2 if ( $FORM{'protect'} eq $items[2] );
		$i++;

	}

	if ( $posterr == 0 ) {


		
		@items = split ( /\,/, $logdata[0] );
		$newpostid = $items[1] + 1;
		$msgdata = "$nowtime,$newpostid,$FORM{'protect'},$FORM{'thread'},$FORM{'code'},$FORM{'area'},$FORM{'username'},$FORM{'mailaddr'},$FORM{'title'},$FORM{'message'}\n";

		

		@logdata = @logdata[0 .. $logsave - 2] if ( @logdata >= $logsave );

		unshift ( @logdata, $msgdata );
		$oldstream = select ( FLOG );
		$| = 1;
		seek ( FLOG, 0, 0 );
		truncate ( FLOG, 0 );
		print FLOG @logdata;
		eval 'flock ( FLOG, 8 )';
		close ( FLOG );
		select ( $oldstream );
		
		$wdate = &getnowdate ( $nowtime );
		&prtoldlog;
		

	} else {

		eval 'flock ( FLOG, 8 )';

		close ( FLOG );

		

		if ( $posterr == 2 ) {
			&chkerror ( '', $posterr );
			if ( $FORM{'follow'} ne '' ) {
				&prtfollow ( 1 );

			} else {

				&prtboard ( $FORM{'title'}, $FORM{'message'}, $FORM{'linkurl'} );

			}
			exit;
		}

	}

}



# Update data file ######################################################


sub totalmessage {

	
## original ##	open ( FLOG, "+<$totalfilename" ) || &prterror ( 'メッセージ読み込みに失敗しました' );
	open ( FLOG, "+<$totalfilename" ) || &prterror ( 'Failed to read message.' );


	eval 'flock ( FLOG, 2 )';
	seek ( FLOG, 0, 0 );
	@lines = <FLOG>;

		@lines = @lines[0 .. $slogsave - 2] if ( @lines >= $logsave );
		unshift ( @lines, $msgdata );

		seek ( FLOG, 0, 0 );
		truncate ( FLOG, 0 );
		print FLOG @lines ;
		eval 'flock ( FLOG, 8 )';


		close ( FLOG );


}

# Update database ##############################################################

sub totalist {





## original ##	open ( TLOG, "+<$totalist" ) || &prterror ( 'メッセージ読み込みに失敗しました' );
	open ( TLOG, "+<$totalist" ) || &prterror ( 'Failed to read message' );

	eval 'flock ( TLOG, 2 )';
	seek ( TLOG, 0, 0 );
	@motodata = <TLOG>;

	$i = 0;
	$posterr = 0;

	$mota=@motodata;
	$mota++;


	while ( $i < $mota ) {
		@items = split ( /\,/, $motodata[$i] );
		if ( $FORM{'area'} ne $items[5] ) { push(@listdata,@motodata[$i] );}else{ 
$ftime=$items[3];
$btitle=$items[4];
$bjunre=$items[7];
$kizon=1;
}


		$i++;
	}

###################
# Forcibly shorten $msg content to fit within $bytes
###################

$bytes=30;
$sbytes=20;

	$msg=$FORM{'message'};
	$msg=~s/<[^<>]*>//ig;
        $msg =~ s/&gt;.*?\r//g;
## original ##        $msg =~ s/参考.*?$//g;
        $msg =~ s/Reference:.*?$//g;


	if (  $postid eq 1 ) {
$title="";
}

#	if (  $FORM{'title'} ne "　") {
#$title="$FORM{'title'} :";
#}else{$title="";}

	if (  $FORM{'username'} ne "　") {
$user="$FORM{'username'} :";}else{$user="";}




	$msg="$user$msg";


	if (  length ( $msg ) > $bytes ) {
	$plus2="\.\.\.";
	}

	$msg2= substr($msg, 0, $bytes);

	unless ($msg2=~ /^([\x00-\x7f]|[\x81-\x9f\xe0-\xfc][\x40-\x7e\x80-\xfc])*$/) {
	$bytes ++;
	$msg2= substr($msg, 0, $bytes);
      }

	$msg2 =~ s/</&lt;/g;
	$msg2 =~ s/>/&gt;/g;
	$msg2 ="$msg2$plus2";



$zapbbs = $FORM{'code'};

$zapbbs=~ s/ぁゃιぃわ\Qー\Eるど//g;
$zapbbs=~ s/あやしいわ\Qー\Eるど//g;
$zapbbs=~ s/あやしいわ－るど//g;
$zapbbs=~ s/ぁゃιぃ//g;
$zapbbs=~ s/^＠//g;
$zapbbs=~ s/^\@//g;



# Wrap $str in $bytes bytes

$str=$zapbbs;

	if (  length ( $str ) > $sbytes ) {
	$plus="\.\.\.";
	}

	$str= substr($str, 0, $sbytes);

	unless ($str=~ /^([\x00-\x7f]|[\x81-\x9f\xe0-\xfc][\x40-\x7e\x80-\xfc])*$/) {
	$bytes ++;
	$str2= substr($str, 0, $sbytes);
      }



$zapbbs="$str$plus";




###################



if($kizon eq 1){

		$msgdata2  = "$nowtime,$newpostid,$FORM{'protect'},$ftime,$btitle,$FORM{'area'},$FORM{'username'},$bjunre,$FORM{'title'},$msg2\n";




}else{


		$msgdata2 = "$nowtime,$newpostid,$FORM{'protect'},$nowtime,$zapbbs,$FORM{'area'},$FORM{'username'},$FORM{'areaname'},,$msg2\n";


}


####　It's a process to delete a topic! #######
	$nowtime = time - $difftime * 60 * 60;




	foreach (0 ..  $mota )

        	{

	@nitems = split ( /\,/, $listdata[$_] );
	$ndate=$nitems[0];
	$cdate= $nowtime - $ndate;
	$deletesec=$deletesec+$nitems[1]*$enmeisec;


	if ($cdate < $deletesec){
        push(@nlistdata,@listdata[$_] );
	}else{

	unlink "data\/$nitems[5]\.dat" ;
	unlink "count1\/$nitems[5]\0.dat" ;
	}


	}

########　up to this point　#######


		@nlistdata= @nlistdata[0 .. $slogsave - 2] if ( @nlistdata >= $logsave );



	if ( $posterr == 0 ) {

		@items = split ( /\,/, @nlistdata[0] );
		$newpostid = $items[1] + 1;
		@nlistdata = @nlistdata[0 .. $logsave - 2] if ( @nlistdata>= $logsave );


		unshift ( @nlistdata, $msgdata2 );
		$oldstream = select (TLOG );
		$| = 1;
		seek ( TLOG, 0, 0 );
		truncate ( TLOG, 0 );
		print TLOG @nlistdata;
		eval 'flock ( TLOG, 8 )';
		close ( TLOG );
		select ( $oldstream );

}
		close ( TLOG );


}

# Create new data file #########################################################

sub create {


## original ##	open ( FLOG, "$totalist" ) || &prterror ( 'メッセージ読み込みに失敗しました' );
	open ( FLOG, "$totalist" ) || &prterror ( 'Failed to read message' );


	eval 'flock ( FLOG, 2 )';
	seek ( FLOG, 0, 0 );
	@checklines = <FLOG>;

	$i = 0;
	$posterr = 0;
	$maxfact = 0;

	while ( $i < $logsave && $posterr == 0 ) {
		@items = split ( /\,/, $checklines[$i] );
		$items[9] =~ s/\n$//;
		$posterr = 1 if ( $i < $checkcount && $FORM{'message'} eq $items[9] );
		$posterr = 2 if ( $FORM{'protect'} eq $items[2] );
		$posterr = 3 if ( $FORM{'code'} eq $items[4] );
		$i++;
	}

$maxfact ++;

		close(FLOG);
		eval 'flock ( FLOG, 8 )';


	if ( $posterr == 0 ) {

		open(OUT,">$logfilename");
		print OUT $none;
		close(OUT);

		open ( FLOG, "+<$logfilename" ) ;
		}else{
## original ##		&prterror ( 'エラーが発生しました。同じ名前の掲示板がないか確認してくだい。' );
		&prterror ( 'An error has occurred. Please check if there\'s another topic with the same name.' );
}



}


###############################################################################

#  Log output

###############################################################################



sub prtoldlog {

	

	if ( $oldlogfiledir ne '' ) {

		$user = $FORM{'username'};
		$mail = $FORM{'mailaddr'};
		$link = $FORM{'linkurl'};
		$title = $FORM{'title'};
		$msg = $FORM{'message'};
	        $bbs = $FORM{'code'};

		if ( $oldlogsavesw == 0 ) {

			$oldlogfilename = sprintf ( "%s/%d%02d%02d.html",
				$oldlogfiledir, $year, $mon, $mday );

		} else {

			$oldlogfilename = sprintf ( "%s%d%02d.html",
				$oldlogfiledir, $year, $mon );

		}

		

## original ##		open ( CLOG, ">>$oldlogfilename" ) || &prterror ( '過去ログ出力に失敗しました' );
		open ( CLOG, ">>$oldlogfilename" ) || &prterror ( 'Failed to output log' );

		eval 'flock ( CLOG, 2 )';

		

		$oldstream = select ( CLOG );

		$| = 1;

		

		if ( -z CLOG ) {

## original ##			print CLOG "<html>\n<head><title>$pagetitle</title>\n</head>\n",
			print CLOG "<html lang=\"ja\">\n<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>$pagetitle</title>\n<style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style>\n</head>\n",
			  "<body bgcolor=\"#$oldlogbgc\" text=\"#$textc\" link=\"#$linkc\"",
			  " vlink=\"#$vlinkc\" alink=\"#$alinkc\">\n<hr>";
		}
		

                $logmsg =1;
		&prtmessage ( 'CLOG', 1 );
                $logmsg =0;
		
		eval 'flock ( CLOG, 8 )';
		close ( CLOG );
		select ( $oldstream );

		

		chmod 0400, $logfilename if ( ( -s $oldlogfilename ) > $maxoldlogsize );

		

		&getnowdate ( time + $difftime - $oldlogsaveday * 60 * 60 * 24 );

		$oldlogfilename = sprintf (  "%s/%d%02d%02d.html",
			$oldlogfiledir, $year, $mon, $mday );
		unlink $oldlogfilename;
	}

}



1;


__END__

