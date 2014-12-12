#! /usr/local/bin/perl -w

use strict;
use warnings;
use Date::Parse;


my $file = $ARGV[0];
open my $info, $file or die "Could not open $file: $!";

my $needle = qr/charger/;

my $data_of_interest = qr/power\|battery\|level/;

my $prev_val = "nothing";

my $matched_val = "unknown\n";

while( my $line = <$info>) {
	my ($uid, $elapset, $date, $key, $value) = split /;/, $line;
	if ($key =~ $needle) {
    	$matched_val = $value;
	} elsif($key =~ $data_of_interest) {
		chomp($value);
		#print str2time($date), ",", $value, ",", $matched_val;
		if($value ne $prev_val) {
			print $date, ",", $value, ",", $matched_val;
			$prev_val = $value;
		}
	}
}

close $info;