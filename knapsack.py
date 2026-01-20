import sys

def solve():
    # Use sys.stdin.read to handle large inputs quickly
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    # Get number of test cases
    try:
        T = int(next(iterator))
    except StopIteration:
        return

    for _ in range(T):
        # Read N (items) and W (capacity)
        N = int(next(iterator))
        W = int(next(iterator))
        
        items = []
        
        # Read all items
        for _ in range(N):
            val = int(next(iterator))
            wt = int(next(iterator))
            # Store as tuple: (value, weight, ratio)
            # We calculate ratio immediately for sorting
            items.append((val, wt, val / wt))
            
        # GREEDY STEP: Sort by ratio (index 2) in Descending order
        items.sort(key=lambda x: x[2], reverse=True)
        
        total_value = 0.0
        current_weight = 0
        
        for val, wt, ratio in items:
            if current_weight + wt <= W:
                # If we can take the whole item, take it
                current_weight += wt
                total_value += val
            else:
                # If we can't take the whole item, take a fraction
                remaining_capacity = W - current_weight
                total_value += val * (remaining_capacity / wt)
                break # Knapsack is full, we are done
        
        # Output formatted to exactly 6 decimal places
        print(f"{total_value:.6f}")

if __name__ == "__main__":
    solve()