# Number runs

The algorithm needs to spend _O(n*k)_ time, where _n_ is the length of the sequence,
and _k_ is the length of the run to detect. _O(k)_ RAM is strictly enough,
provided that we stream in the sequence and stream out the results.

Possibly there is an algorithm that spends less than _O(n*k)_ time by determining
sub-runs within runs being analyzed. I did not delve into this. Maybe that algorithm
could make use of the fact that the numbers are strictly positive; my simplistic
algorithm ignores this and should happily work with zeros and negatve numbers.

The Python implementation plays with iterators and should cope well with very long
input sequences without allocating much RAM.

The Haskell implementation plays with pattern matching; it also should run
in constant RAM space. It lacks tests, though.

I wish I had time to write a Go implementation playing with channels, or at least
avoiding copying with slices.
