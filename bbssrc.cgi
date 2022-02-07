#! /usr/bin/perl

#

#	KuzuhaScript Final Beta #2 pl0.3

#	 (Post search functions)

#



###############################################################################

#  Display search results

###############################################################################



sub srcmessage {

	

	my $success = 0;

	

	&loadmessage;

	

## original ##	&prterror ( 'パラメータがありません。' ) if ( $FORM{'search'} eq '' );
	&prterror ( 'There are no parameters.' ) if ( $FORM{'search'} eq '' );

	

#	print "Content-type: text/html\n\n",



## original ##	  	print "<html><head><title>$bbstitle</title></head>\n$body\n\n";
	  	print "<html><head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><META http-equiv=\"Content-Type\" content=\"text/html; charset=Shift_JIS\"><title>$bbstitle</title><style>body{font-family:\"MS PGothic\",sans-serif;}pre{font-family:\"MS Gothic\",monospace;}\@media only screen and (max-width:640px){pre{font-size:10pt}}</style></head>\n$body\n\n";

	

	foreach ( 0 .. @logdata - 1 ) {

		&getmessage ( $logdata[$_] );

		if ( $FORM{'mode'} eq 'search' ) {

			if ( $FORM{'search'} eq $user ) {

				$success++;

				&prtmessage ( 'STDOUT', 0 );

			}

		} elsif ( $FORM{'mode'} eq 'thread' ) {

			if ( $FORM{'search'} eq $thread || $FORM{'search'} eq $postid ) {

				$success++;

				&prtmessage ( 'STDOUT', 0 );

			}

		}

		$i++;

	}

	

	if ( $success == 0 ) {

## original ##		print "<h3>指定されたメッセージが見つかりません。</h3><body></html>";
		print "<h3>The specified message could not be found.</h3><body></html>";

		exit;

	}

	

	print "</body></html>";

	exit;

}



1;





__END__

                                                     