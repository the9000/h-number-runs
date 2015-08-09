{-
Detect runs (subsequences increasing or decreasing by 1)
of 3 numbers in input list.

Here we exploit the fact that run length is fixed in the problem statement
to use pattern-matching.
-}


findNumberRuns :: Integral a => [a] -> [a]
findNumberRuns xs = reverse $ findRuns (zip [0..] xs) []

-- Pattern-matching here is used a bit too heavily, but is still readable.
findRuns ((i1, v1) : pair2@(i2, v2) : pair3@(i3, v3) : rest) acc =
  findRuns (pair2 : pair3 : rest) (if isRun v1 v2 v3 then i1:acc else acc) 
  where isRun v1 v2 v3 = (v1 - v2) `elem` [-1, 1] && (v2 - v3 == v1 - v2)

findRuns _ acc = acc
