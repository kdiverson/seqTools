#/path/to/samtools pileup in.bam | awk '{print $4}' | perl meanCoverageBAM.pl
#/path/to/samtools view -b in.bam <genomic region> | /path/to/samtools pileup - | awk '{print $4}' | perl meanCoverageBAM.pl
($num,$den)=(0,0);
while ($cov=<STDIN>) {
    $num=$num+$cov;
    $den++;
}
$cov=$num/$den;
print "Mean Coverage = $cov\n";
