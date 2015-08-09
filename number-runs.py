"""Detect runs (subsequences increasing or decreasing by 1)
of given length  in a sequence of integers.

Will also work with floats up to approximately 9e+15, assuming double-precision
IEEE 754 floats that CPython and Jython use.
"""

import unittest


# The target function.


def findNumberRuns(data, run_length=3):
    """Find ascending or descending number runs in a sequence.

    Args:
      data: a sequence of integers.
      run_length: length of runs to detect; must be > 1.
    Returns:
      List of indices where runs begin in data.
    """
    assert run_length > 1, "Runs shorter that 2 make no sense."
    results = []
    index = 0
    while len(data) - index >= run_length: 
        potential_run = data[index : index + run_length]
        if isRun(potential_run):
            results.append(index)
        index += 1
    return results


def isRun(potential_run):
    """Return True iff potential_run is an ascending or descending run."""
    diffs = (x - y for (x, y) in zip(potential_run, potential_run[1:]))
    delta = diffs.next()
    if delta not in (-1, 1):
        return False
    return all(next_delta == delta for next_delta in diffs)


class RunsTest(unittest.TestCase):

    def testSequenceFromProblemStatementWorks(self):
        self.assertEquals([0, 4, 6, 7],
                          findNumberRuns([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7]))

    def testInputShorterThanRunLengthResultsInEmptyList(self):
        self.assertEquals([], findNumberRuns(range(10), run_length=11))

    def testEmbeddedSequentialRunsAreDetected(self):
        self.assertEquals([0, 1, 2],
                          findNumberRuns([1, 2, 3, 4, 5]))

    def testNonDefaultRunLengthWorks(self):
        self.assertEquals([2],
                          findNumberRuns([4, 7, 1, 2, 3, 4, 5, 8], run_length=5))
        
        
if __name__ == '__main__':
    unittest.main()