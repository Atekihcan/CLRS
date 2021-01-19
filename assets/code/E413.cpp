#include <iostream>
#include <climits>
#include <chrono>

/* structure to store the result */
typedef struct {
    int left;
    int right;
    int sum;

} MaxSubarray; 

/* brute force method */
MaxSubarray FindMaxSubarrayBruteForce(int A[], int low, int high) {
    int tempSum;
    MaxSubarray ret = {0, 0, INT_MIN};
    
    for (auto i = low; i < high; i++) {
        tempSum = 0;
        for (auto j = i; j < high; j++) {
            tempSum += A[j];
            if (tempSum > ret.sum) {
                ret.sum = tempSum;
                ret.left = i;
                ret.right = j;
            }
        }
    }
    return ret;
}

/* function for finding crossing maximum sub-array */
MaxSubarray FindMaxCrossingSubarray(int A[], int low, int mid, int high) {
    MaxSubarray ret = {0, 0, 0};
    int leftSum = INT_MIN;
    int rightSum = INT_MIN;
    int sum = 0;
    for (auto i = mid - 1; i >= low; i--) {
        sum += A[i];
        if (sum > leftSum) {
            leftSum = sum;
            ret.left = i;
        }
    }
    sum = 0;
    for (auto j = mid; j < high; j++) {
        sum += A[j];
        if (sum > rightSum) {
            rightSum = sum;
            ret.right = j;
        }
    }
    ret.sum = leftSum + rightSum;
    return ret;
}

/* recursive method */
MaxSubarray FindMaxSubarrayRecursive(int A[], int low, int high) {
    if (low + 1 == high) {
        MaxSubarray ret = {low, low, A[low]};
        return ret;
    }

    int mid = (low + high) / 2;
    MaxSubarray left = FindMaxSubarrayRecursive(A, low, mid);
    MaxSubarray right = FindMaxSubarrayRecursive(A, mid, high);
    MaxSubarray cross = FindMaxCrossingSubarray(A, low, mid, high);
    if (left.sum >= right.sum && left.sum >= cross.sum)
        return left;
    else if (right.sum >= left.sum && right.sum >= cross.sum)
        return right;
    else
        return cross;
}

/* modified mixed method */
MaxSubarray FindMaxSubarrayMixed(int A[], int low, int high, int n0) {
    if (high - low < n0) {
        return FindMaxSubarrayBruteForce(A, low, high);
    }

    int mid = (low + high) / 2;
    MaxSubarray left = FindMaxSubarrayRecursive(A, low, mid);
    MaxSubarray right = FindMaxSubarrayRecursive(A, mid, high);
    MaxSubarray cross = FindMaxCrossingSubarray(A, low, mid, high);
    if (left.sum >= right.sum && left.sum >= cross.sum)
        return left;
    else if (right.sum >= left.sum && right.sum >= cross.sum)
        return right;
    else
        return cross;
}

/* driver code to measure performance */
int main() {
    // Following variable used to set number of times we'll call each functions
    // and find average running time. Taking run time for a single run is not that useful
    // as there are many factors that can affect this (overall system load etc.)
    // Taking average run time is always a better option
    // The larger this number is more time it will take to get the result, but we'll have better accuracy
    static const int NUM_ITERATIONS = 1000000;

    // Input array which will be used to do all the tests
    // Ideally we should be using a randomly generated array based on input size
    int Arr[100] = {20, -21, 43, -23, -92, 45, -56, -5, 34, -17,
                    34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49,
                    3, -45, 34, 76, 32, -76, -2, 3, -45, 44, 34, 67,
                    -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34,
                    88, 56, -6, -89, -90, -34, -56, 23, 29, 2, 6, 9,
                    2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55,
                    23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56,
                    -34, 45, 32, 20, -87, 39, 82, 95, -67, -45, 88,
                    -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76};
    
    // Iterate over input size, to take more elements
    // I'm starting with 20 to skip some initial sizes, as brute force will be faster for those
    // If in your machine, this code directly jumps to mixed part, then you'll need to reduce this starting point
    auto inputSize = 20;

    // To store the cross over input size
    auto crossOverInputSize = 0;

    // This flag will be used to terminate the loop
    auto done = false;

    printf("Size \t BruteForce \t Recursive \t Mixed\n");
    printf("----------------------------------------------\n");
    while (!done) {
        // Calculate run time for the brute force method
        auto start = std::chrono::high_resolution_clock::now();
        for (auto i = 0; i < NUM_ITERATIONS; i++) {
            MaxSubarray R1 = FindMaxSubarrayBruteForce(Arr, 0, inputSize);
        }
        auto stop = std::chrono::high_resolution_clock::now();
        auto timeBruteForce = (float) std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() / (float) NUM_ITERATIONS;
        
        // Calculate run time for the recursive method
        start = std::chrono::high_resolution_clock::now();
        for (auto i = 0; i < NUM_ITERATIONS; i++) {
            MaxSubarray R1 = FindMaxSubarrayRecursive(Arr, 0, inputSize);
        }
        stop = std::chrono::high_resolution_clock::now();
        auto timeRecursive = (float) std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() / (float) NUM_ITERATIONS;

        // If brute force method took more time than recursive method, we have found the cross over point
        if (timeBruteForce > timeRecursive) {
            if (crossOverInputSize == 0) {
                // We are interested in the first time cross over only
                crossOverInputSize = inputSize;
            }
        } else {
            // Otherwise increment loop counter and repeat the loop
            // We don't have a cross over yet, cannot run mixed method
            printf("%d \t %8.4f \t %7.4f \t   --\n", inputSize, timeBruteForce, timeRecursive);
            inputSize += 1;
            // Reset crossover point in case we got one earlier
            // This is due to fluctuation in system load
            crossOverInputSize = 0;
            continue;
        }

        // Calculate run time for the mixed method
        start = std::chrono::high_resolution_clock::now();
        for (auto i = 0; i < NUM_ITERATIONS; i++) {
            MaxSubarray R1 = FindMaxSubarrayMixed(Arr, 0, inputSize, crossOverInputSize);
        }
        stop = std::chrono::high_resolution_clock::now();
        auto timeMixed = (float) std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() / (float) NUM_ITERATIONS;
        printf("%d \t %8.4f \t %7.4f \t %6.4f\n", inputSize, timeBruteForce, timeRecursive, timeMixed);

        // Increment loop counter
        inputSize += 1;

        // Just for curiosity, want to run 4 extra loops after finding crossover point
        if (inputSize > crossOverInputSize + 4) {
            done = true;
        }
    }

    return 0;
}
