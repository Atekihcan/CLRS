import random


def BiasedRandom(p):
    """
    Simulates BIASED-RANDOM with probability p of returning 1

    Args:
        p: probability of returning 1 (between 0 and 1)

    Returns:
        1 with probability p, 0 with probability (1-p)
    """
    return 1 if random.random() < p else 0


def UnbiasedRandom(p):
    """
    Generates an unbiased random bit using a biased source

    Args:
        p: bias of the source (probability of 1)

    Returns:
        0 or 1, each with probability 1/2
    """
    while True:
        x = BiasedRandom(p)
        y = BiasedRandom(p)

        if x == 0 and y == 1:
            return 0
        if x == 1 and y == 0:
            return 1
        # If (0,0) or (1,1), discard and try again


# Test with different bias values
print("Testing Unbiased-Random with various bias values:\n")

for p in [0.1, 0.3, 0.5, 0.7, 0.9]:
    print(f"Bias p = {p}")

    # Count number of calls to BiasedRandom
    call_count = 0
    original_biased = BiasedRandom

    def counted_biased(bias):
        global call_count
        call_count += 1
        return original_biased(bias)

    # Generate samples and count calls
    BiasedRandom = counted_biased
    samples = 1000
    zeros = 0
    ones = 0

    for _ in range(samples):
        result = UnbiasedRandom(p)
        if result == 0:
            zeros += 1
        else:
            ones += 1

    BiasedRandom = original_biased

    avg_calls = call_count / samples
    theoretical = 1 / (p * (1 - p))

    print(f"  Results: 0's = {zeros}, 1's = {ones}")
    print(f"  Average calls per output: {avg_calls:.2f}")
    print(f"  Theoretical expectation:  {theoretical:.2f}")
    print()

print("As expected, when p = 0.5, we need the fewest calls (~4).")
print("When p is extreme (close to 0 or 1), we need many more calls.")
