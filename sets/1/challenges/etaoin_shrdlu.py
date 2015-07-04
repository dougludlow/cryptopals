"""Methods that calculate a score based on letter frequency"""

from collections import defaultdict

def score(text):

    counts = __char_counts(text)
    score = 0

    for s,v in __scores().iteritems():
        if counts.has_key(s):
            score += counts[s] * v

    return score

def __char_counts(text):

    counts = defaultdict(int)

    for c in text:
        counts[c.lower()] += 1

    return counts

def __scores():
    common = 'etaoin shrdlu'
    scores = {}
    score = len(common)

    for c in common:
        score -= 1
        scores[c] = score

    return scores

