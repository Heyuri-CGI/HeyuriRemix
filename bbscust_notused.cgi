#! /usr/bin/perl

#
#	�����͂�����Ղ� Final Beta #2 pl0.3
#	 (�l�p���ݒ��ʗp)
#


###############################################################################
#  ���ݒ��ʕ\��
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
<head><title>$bbstitle �l�p���ݒ�</title></head>
$body
<h3>$bbstitle �l�p���ݒ�</h3>
<br>
<form method="post" action="$cgiurl\?$FORM{'code'}">
<input type="hidden" name="mode" value="customset">
<ul>
<li><strong>�\\���ݒ�</strong><br> <br>
<table border="0" cellspacing="0" cellpadding="0">
<tr><td>�����F�@�@�@</td><td><input type="text" name="textc" size="7" value="$textc"></td>
<td>�@�w�i�F</td><td><input type="text" name="bgc" size="7" value="$bgc"></td><tr>
<tr><td>�����N�F</td><td><input type="text" name="linkc" size="7" value="$linkc"></td>
<td>�@�K��σ����N�F </td><td><input type="text" name="vlinkc" size="7" value="$vlinkc"></td><tr>
</table>
</ul>
<ul>
<li><strong>�t�H���[��ʂ̕\\�����@</strong><br> <br>
<input type="radio" name="followwin" value="0" $follow[0]>�V�K�E�B���h�E���J���ĕ\\��<br>
<input type="radio" name="followwin" value="1" $follow[1]>�V�K�E�B���h�E���J�����ɕ\\��<br>
</ul>
<br>
�u�o�^�v����������ɕ\\�������URL���u�b�N�}�[�N�ɓo�^���܂��傤�B<br>
��L�̐ݒ�Ōf����K�₷�邱�Ƃ��ł��܂��B<br> <br>
<input type="hidden" name="autolink" value="$FORM{'autolink'}">
<input type="hidden" name="code" value="$FORM{'code'}">
<input type="submit" name="btnname" value="�o�^">
<input type="reset" name="btnname" value="���ɖ߂�">
<input type="submit" name="btnname" value="�K��l�ɖ߂�">
</form>
</body>
</html>
__EOF__
}


###############################################################################
#  ���ݒ茋�ʉ�ʕ\��
###############################################################################

sub setcustom {
	
	my ( $i, $custom );
	
	if ( $FORM{'btnname'} ne '�K��l�ɖ߂�' ) {
		$i = $FORM{'followwin'} * 2;
		$custom = "?code=$FORM{'code'}&autolink=$FORM{'autolink'}&custom=$FORM{'textc'}$FORM{'bgc'}$FORM{'linkc'}$FORM{'vlinkc'}$i";
	}
	
	print "Location: $cgiurl$custom\n\n";
}


1;
