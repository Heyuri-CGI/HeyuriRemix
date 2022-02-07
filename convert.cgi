#! /usr/bin/perl

$dir='data';

 if(!opendir(DIR, $dir)) {exit;}

	@dfiles=readdir(DIR);

               $end = @dfiles;



	foreach  (1 .. $end){


$logname="./data/bbb";
$logname =~ s/bbb/$dfiles[$_]/g;

$recordlogname=$logname;
$recordlogname =~ s/\.dat//g;

	if (!open(STDIN,"$logname")) {
 }
	$set=<STDIN>;
	close(STDIN);


##########　Heavy processing　#######

## original ##	open ( READLOG, "$logname" ) || &prterror ( 'メッセージ読み込みに失敗しました' );
	open ( READLOG, "$logname" ) || &prterror ( 'Failed to read message' );
	eval 'flock ( READLOG, 1 )';
	seek ( READLOG, 0, 0 );
	@logdata =  <READLOG>;
	eval 'flock ( READLOG, 8 )';
	close ( READLOG );

        @logdata=reverse @logdata;
        $fset=$logdata[0];






	( $ndate, $postid, $protect, $thread, $bbs, $agent, $user, $mail, $title, $msg)= split ( /\,/,$set); 

	( $odate, $opostid, $oprotect, $tohread, $bbos, $agoent, $usoer, $omail, $titole, $mosg)= split ( /\,/,$fset); 




#############　Wrap processing
$bytes=30;

$msg="$user\:$msg";


	if (  length ( $msg ) > $bytes ) {$plus2="\.\.\.";}

	$msg2= substr($msg, 0, $bytes);

	unless ($msg2=~ /^([\x00-\x7f]|[\x81-\x9f\xe0-\xfc][\x40-\x7e\x80-\xfc])*$/) {
      $bytes ++;
      $msg2= substr($msg, 0, $bytes);
      }

$msg2 =~ s/</&lt;/g;
$msg2 =~ s/>/&gt;/g;
$msg2=~s/\n//g;
$msg="$msg2$plus2\n";


#############　End of wrapping


#############　Ayashii prohibition

$bbs=~ s/ぁゃιぃわ\Qー\Eるど//g;
$bbs=~ s/あやしいわ\Qー\Eるど//g;
$bbs=~ s/あやしいわ－るど//g;
$bbs=~ s/ぁゃιぃ//g;
$bbs=~ s/^＠//g;
$bbs=~ s/^\@//g;

#############　End of Ayashii prohibition

$genre=$dfiles[$_];
$genre=~s/\.dat//g;
$lognnn=$genre;
$genre=~s/[0-9]//g;

$set="$ndate,$postid,$protect,$odate,$bbs,$lognnn,$user,$genre,$title,$msg";

if ($ndate ne ""){push (@set,$set); }

}


@oldset=@set;


@set= reverse @set;


open(OUT,">list.log");
print OUT @set;
close(OUT);


	closedir(DIR);

print "Content-type: text/html\n\n";

print <<"_HTML_";

<!-- ## original ## <HTML>リスト\表\示用ファイルの作成が終了しました。
## original ## <a href="list.txt">このファイルを見てみる</a> -->
<html>Creation of the list display file is complete.
<a href="list.txt">Please take a look at this file</a>
_HTML_

exit;