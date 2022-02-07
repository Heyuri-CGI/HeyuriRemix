#! /usr/bin/perl

#
#	くずはすくりぷと Final Beta #2 pl0.3
#	 (個人用環境設定画面用)
#


###############################################################################
#  環境設定画面表示
###############################################################################

sub prtcustom {
	
	my @follow;
	$follow[$followwin] = 'checked';

		if ( ($FORM{'code'} ne '' )&&( $FORM{'code'} ne 'read' ) ) {
		$bbstitle = $FORM{'code'} ;
	}
	
	print <<"__EOF__";
Content-Type: text/html

<html>
<head><title>$bbstitle 個人用環境設定</title></head>
$body
<h3>$bbstitle 個人用環境設定</h3>
<br>
<form method="post" action="$cgiurl\?$FORM{'code'}">
<input type="hidden" name="mode" value="customset">
<ul>
<li><strong>表\示設定</strong><br> <br>
<table border="0" cellspacing="0" cellpadding="0">
<tr><td>文字色　　　</td><td><input type="text" name="textc" size="7" value="$textc"></td>
<td>　背景色</td><td><input type="text" name="bgc" size="7" value="$bgc"></td><tr>
<tr><td>リンク色</td><td><input type="text" name="linkc" size="7" value="$linkc"></td>
<td>　訪問済リンク色 </td><td><input type="text" name="vlinkc" size="7" value="$vlinkc"></td><tr>
</table>
</ul>
<ul>
<li><strong>フォロー画面の表\示方法</strong><br> <br>
<input type="radio" name="followwin" value="0" $follow[0]>新規ウィンドウを開いて表\示<br>
<input type="radio" name="followwin" value="1" $follow[1]>新規ウィンドウを開かずに表\示<br>
</ul>
<br>
「登録」を押した後に表\示されるURLをブックマークに登録しましょう。<br>
上記の設定で掲示板を訪問することができます。<br> <br>
<input type="hidden" name="autolink" value="$FORM{'autolink'}">
<input type="hidden" name="code" value="$FORM{'code'}">
<input type="submit" name="btnname" value="登録">
<input type="reset" name="btnname" value="元に戻す">
<input type="submit" name="btnname" value="規定値に戻す">
</form>
</body>
</html>
__EOF__
}


###############################################################################
#  環境設定結果画面表示
###############################################################################

sub setcustom {
	
	my ( $i, $custom );
	
	if ( $FORM{'btnname'} ne '規定値に戻す' ) {
		$i = $FORM{'followwin'} * 2;
		$custom = "?code=$FORM{'code'}&autolink=$FORM{'autolink'}&custom=$FORM{'textc'}$FORM{'bgc'}$FORM{'linkc'}$FORM{'vlinkc'}$i";
	}
	
	print "Location: $cgiurl$custom\n\n";
}


1;
