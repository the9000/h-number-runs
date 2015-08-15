"""Detect runs (subsequences increasing or decreasing by 1)
of given length  in a sequence of integers.

Will also work with floats up to approximately 9e+15, assuming double-precision
IEEE 754 floats that CPython and Jython use. Not recommended.

Can work with sequences of unbounded length, as long as there's enough RAM
to store O(run_length) numbers.
"""

import itertools

import unittest


# The target function.


def findNumberRuns(input_sequence, run_length=3):
    """Find ascending or descending number runs in a sequence.

    Args:
      input_sequence: a sequence of integers.
      run_length: length of runs to detect; must be > 1.
    Returns:
      List of indices where runs begin in data.
    """
    assert run_length > 1, "Runs shorter that 2 make no sense."
    source = iter(input_sequence)  # ok with any iterables
    results = []
    index = 0
    while True: 
        potential_run = take(run_length, source)
        if len(potential_run) < run_length:
            break
        if isRun(potential_run):
            results.append(index)
        source = pushBack(potential_run[1:], source)
        index += 1
    return results


def isRun(potential_run):
    """returns True iff potential_run is an ascending or descending run."""
    # We allocate O(len(potential_run)) memory. If runs are huge,
    # this can be rewritten using index access or iterators to avoid it.
    diffs = (x - y for (x, y) in zip(potential_run, potential_run[1:]))
    delta = next(diffs)
    if delta not in (-1, 1):
        return False
    return all(next_delta == delta for next_delta in diffs)


def take(n, data):
    # We can replace [..] with (..) to make it lazy.
    return [x for (_, x) in zip(range(n), data)]

    
def pushBack(prefix_data, source):
    return itertools.chain(prefix_data, source)

    
## Tests.

    
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
        self.assertEquals(
            [2],
            findNumberRuns([4, 7, 1, 2, 3, 4, 5, 8], run_length=5))
        
        
if __name__ == '__main__':
    unittest.main()