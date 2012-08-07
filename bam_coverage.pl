#!/usr/bin/env perl

use strict;
use warnings;

# Usage: samtools pileup file.bam | bam_coverage.pl

my $num;        # per residue coverage
my $len;        # sequence length counter 
my $min = 1000; # minimum coverage
my $max = 0;    # maximum coverage

while (<>) {
    my @a = split /\t/;
    $num += $a[3];
    $min = $a[3] if $min > $a[3];
    $max = $a[3] if $max < $a[3];
    $len++;
}

printf  "Mean coverage  : %.1f\n", $num/$len;
printf  "Coverage range : %d - %d\n", $min, $max;
