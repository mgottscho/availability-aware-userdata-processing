while read p; do
  for f in ../data/*csv; do
  	outf="$f.$p"
	echo "Processing $outf ..."
	grep -e ".*;.*;.*;$p" $f > $outf
  done
done < patterns_interesting.txt
