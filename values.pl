#!/usr/bin/perl -w    
while(<>) {
    while (/(.*(0-9)*\n)/g) {      
    	print $1 
    }
}
