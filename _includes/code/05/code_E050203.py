import random

def roll_dice(n):
    """Roll n six-sided dice and return the sum."""
    return sum(random.randint(1, 6) for _ in range(n))

def simulate_dice_expected_value(n, num_trials=10000):
    """
    Simulate rolling n dice many times and compute the average sum.

    Args:
        n: Number of dice to roll
        num_trials: Number of simulations to run

    Returns:
        The empirical average sum
    """
    total = sum(roll_dice(n) for _ in range(num_trials))
    return total / num_trials

# Test with different numbers of dice
print("Expected value of sum of n dice:")
print("=" * 50)

for num_dice in [1, 2, 5, 10, 20]:
    empirical_average = simulate_dice_expected_value(num_dice)
    theoretical_expected = 3.5 * num_dice

    print(f"n = {num_dice:2d} dice")
    print(f"  Theoretical: {theoretical_expected:.2f}")
    print(f"  Empirical:   {empirical_average:.2f}")
    print(f"  Difference:  {abs(empirical_average - theoretical_expected):.2f}")
    print()

# Single detailed example
print("=" * 50)
print("Detailed example with n = 10 dice:")
print("Rolling 10 times:")
for i in range(10):
    roll_result = roll_dice(10)
    print(f"  Roll {i+1:2d}: {roll_result}")

print(f"\nTheoretical expected value: {3.5 * 10:.1f}")
