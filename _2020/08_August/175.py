"""
You are given a starting state start, a list of transition probabilities for a
Markov chain, and a number of steps num_steps. Run the Markov chain starting
from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the
following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012,
'b': 1656, 'c': 332 }.
"""
import random
from collections import defaultdict


def count_states(states: list, num_steps: int, start_state: str) -> dict:
    """Given transition properties, return the number of times in each state"""
    d = defaultdict(int)
    while num_steps > 0:
        r = random.random()
        base_random = 0  # Random number offset. 0.8, 0.15 -> 0.8, 0.95
        for x, y, z in states:
            if x == start_state:
                if base_random <= r < z + base_random:
                    d[y] += 1
                    start_state = y
                    num_steps -= 1
                base_random += z

    return d


if __name__ == '__main__':
    states = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
    print(count_states(states, 5000, "a"))
    # defaultdict(<class 'int'>, {'a': 3174, 'b': 1563, 'c': 263})
