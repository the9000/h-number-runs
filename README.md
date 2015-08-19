# Number runs

The algorithm needs to spend _O(n*k)_ time, where _n_ is the length of the sequence,
and _k_ is the length of the run to detect. _O(k)_ RAM is strictly enough,
provided that we stream in the sequence and stream out the results.

The Python implementation plays with iterators and should well with very long
input sequences without allocating much RAM.

The Haskell implementation plays with pattern matching; it also should run
in constant RAM space. It lacks tests, though.

I wish I had time to write a Go implementation playing with channels, or at least
avoiding copying with slices.
