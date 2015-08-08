"""Detect ascending or descending number runs in a sequence."""

def findNumberRuns(data, run_length=3):
    results = []
    index = 0
    while len(data) >= run_length: 
        potential_run = data[:run_length]
        if isRun(potential_run):
            results.append(index)
        index += 1
        data = data[1:]
    return results


def isRun(potential_run):
    assert potential_run, "Empty runs make no sense."
    diffs = (x - y for (x, y) in zip(potential_run, potential_run[1:]))
    delta = diffs.next()
    for next_delta in diffs:
        if next_delta != delta:
            return False
    return True