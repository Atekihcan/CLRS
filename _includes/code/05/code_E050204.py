import random

def hat_check_simulation(n):
    """
    Simulate the hat-check problem for n customers.

    Returns the number of customers who get their own hat back.
    """
    # Create hats numbered 1 to n
    hats = list(range(1, n + 1))

    # Shuffle the hats randomly
    random.shuffle(hats)

    # Count how many customers get their own hat
    # Customer i gets their own hat if hats[i-1] == i
    matches = sum(1 for i in range(1, n + 1) if hats[i - 1] == i)

    return matches

def simulate_expected_matches(n, num_trials=10000):
    """
    Simulate the hat-check problem many times and compute average matches.

    Args:
        n: Number of customers/hats
        num_trials: Number of simulations to run

    Returns:
        The empirical average number of matches
    """
    total_matches = sum(hat_check_simulation(n) for _ in range(num_trials))
    return total_matches / num_trials

# Test with different numbers of customers
print("Hat-Check Problem: Expected number of matches")
print("=" * 60)

for num_customers in [3, 5, 10, 50, 100, 1000]:
    empirical_average = simulate_expected_matches(num_customers)
    theoretical_expected = 1.0  # Always 1!

    print(f"n = {num_customers:4d} customers")
    print(f"  Theoretical: {theoretical_expected:.4f}")
    print(f"  Empirical:   {empirical_average:.4f}")
    print(f"  Difference:  {abs(empirical_average - theoretical_expected):.4f}")
    print()

# Detailed example
print("=" * 60)
print("Detailed example with n = 10 customers:")
print("Running 10 simulations:")

for trial in range(10):
    matches = hat_check_simulation(10)
    print(f"  Trial {trial + 1:2d}: {matches} customer(s) got their own hat")

print(f"\nTheoretical expected value: 1 (regardless of n!)")
