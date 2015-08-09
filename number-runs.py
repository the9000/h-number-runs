def findNumberRuns(data, run_length=3):
    """Find ascending or descending number runs in a sequence.

    Args:
      data: a sequence of integers (can work with floats in reasonable range).
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
    diffs = (x - y for (x, y) in zip(potential_run, potential_run[1:]))
    delta = diffs.next()
    if delta not in (-1, 1):
        return False
    return all(next_delta == delta for next_delta in diffs)
