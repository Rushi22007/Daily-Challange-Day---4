# Maximize Happiness of Selected Children

## Problem Description
You are given an array `happiness` of length `n`, and a positive integer `k`.

There are `n` children standing in a queue, where the ith child has happiness value `happiness[i]`. You want to select `k` children from these `n` children in `k` turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting `k` children.

### Example 1:

```plaintext
Input: happiness = [1,2,3], k = 2
Output: 4
```

**Explanation:**
- Pick the child with the happiness value `3`. The happiness value of the remaining children becomes `[0,1]`.
- Pick the child with the happiness value `1`. The happiness value of the remaining children becomes `[0]`.
The sum of the happiness values of the selected children is `3 + 1 = 4`.

### Example 2:

```plaintext
Input: happiness = [1,1,1,1], k = 2
Output: 1
```

**Explanation:**
- Pick any child with the happiness value `1`. The happiness value of the remaining children becomes `[0,0,0]`.
- Pick the child with the happiness value `0`. The happiness value of the remaining children becomes `[0,0]`.
The sum of the happiness values of the selected children is `1 + 0 = 1`.

### Example 3:

```plaintext
Input: happiness = [2,3,4,5], k = 1
Output: 5
```

**Explanation:**
- Pick the child with the happiness value `5`. The happiness value of the remaining children becomes `[1,2,3]`.
The sum of the happiness values of the selected children is `5`.

## Solution
The problem is solved via the following algorithm implemented in C:

1. **Sort the Happiness Array:**
   - The array is sorted in ascending order to focus on the highest values in the subsequent steps.

2. **Iterate and Select Children:**
   - Starting from the end of the sorted array (highest values), select the child with the current maximum happiness value.
   - Subtract the number of turns that have passed from the child's happiness value.
   - Add the resulting happiness value to the total sum, ensuring it is non-negative.
   - Stop the process once `k` children are selected.

## Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>

// Comparator function for qsort
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

long long maximumHappinessSum(int* happiness, int happinessSize, int k) {

    qsort(happiness, happinessSize, sizeof(int), compare);

    long long sum = 0;
    int turns = 0;

    for (int i = happinessSize - 1; i >= 0; i--) {
        int value = happiness[i] - turns;
        if (value > 0)
            sum += value;

        turns++;
        if (turns >= k)
            break;
    }

    return sum;
}
```

## Usage
- Copy the above code into a C file (e.g., `maximize_happiness.c`).
- Compile the file with a C compiler, for example:

```sh
gcc -o maximize_happiness maximize_happiness.c
```

- Run the executable with your input values, modifying the `happiness` array and `k` value in the code.

## Complexity
- **Time Complexity:** $O(n \log n)$ due to the sorting step.
- **Space Complexity:** $O(1)$ as the sorting is done in-place.

## License
This code is available for educational and personal use. You may modify and distribute it with proper attribution.