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

/* linear run-time method */
MaxSubarray FindMaxSubarrayLinear(int A[], int low, int high) {
    MaxSubarray best = {0, 0, 0};
    MaxSubarray current = {0, 0, 0};
    for (auto i = 0; i < high; i++) {
        current.sum += A[i];        
        // Update best sum if required
        if (current.sum > best.sum) {
            best.sum = current.sum;
            best.left = current.left;
            best.right = i;
        }

        // Reset current sum if required
        if (current.sum < 0) {
            current.sum = 0;
            current.left = i + 1;
        }
    }
    return best;
}

// Driver code to measure performance
int main() {
    // Following variable used to set number of times we'll call each functions
    // and find average running time. Taking run time for a single run is not that useful
    // as there are many factors that can affect this (overall system load etc.)
    // Taking average run time is always a better option
    // The larger this number is more time it will take to get the result, but we'll have better accuracy
    static const int NUM_ITERATIONS = 1000000;
    
    // Iterate over input size, to take more elements
    // I'm starting with 20 to skip some initial sizes, as brute force will be faster for those
    auto inputSize = 20;

    // To store the cross over input size
    auto crossOverInputSize = 0;

    // This flag will be used to terminate the loop
    auto done = false;

    printf("Size \t BruteForce \t Recursive \t Linear\n");
    printf("------------------------------------------------\n");
    while (!done) {
        // Create an array with random integers in the range of -100 to 100
        int* arr = new int[inputSize];
        for (auto i = 0; i < inputSize; i++) {
            arr[i] = (rand() % 201) - 100;
        }

        /***********************************************
         *     Verify Correctness of the Algorithms    *
         * *********************************************/
        auto brute = FindMaxSubarrayBruteForce(arr, 0, inputSize);
        auto recursive = FindMaxSubarrayRecursive(arr, 0, inputSize);
        auto linear = FindMaxSubarrayLinear(arr, 0, inputSize);

        // Compare results, only the sum as indices might be different if there are more than one correct answers
        if (brute.sum != recursive.sum && brute.sum != linear.sum) {
            printf("Error : Different results for the following array:\n");
            printf("    arr = [");
            for (auto i= 0; i < inputSize; i++) {
                if (i == inputSize - 1) {
                    printf("%d]\n", arr[i]);
                } else {
                    printf("%d, ", arr[i]);
                }
            }
            printf("Brute force method returned sum = %d [%d, %d]\n", brute.sum, brute.left, brute.right);
            printf("Recursive method returned sum = %d [%d, %d]\n", recursive.sum, recursive.left, recursive.right);
            printf("Linear method returned sum = %d [%d, %d]\n", linear.sum, linear.left, linear.right);
            // Also return from here, as clearly something is wrong with our work
            return -1;
        }

        /***********************************************
         *             Compare Running Times           *
         * *********************************************/
        // Calculate run time for the brute force method
        auto start = std::chrono::high_resolution_clock::now();
        for (auto i = 0; i < NUM_ITERATIONS; i++) {
            FindMaxSubarrayBruteForce(arr, 0, inputSize);
        }
        auto stop = std::chrono::high_resolution_clock::now();
        auto timeBruteForce = (float) std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() / (float) NUM_ITERATIONS;
        
        // Calculate run time for the recursive method
        start = std::chrono::high_resolution_clock::now();
        for (auto i = 0; i < NUM_ITERATIONS; i++) {
            FindMaxSubarrayRecursive(arr, 0, inputSize);
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
            // Reset crossover point in case we got one earlier
            // This is due to fluctuation in system load
            crossOverInputSize = 0;
        }

        // Calculate run time for the mixed method
        start = std::chrono::high_resolution_clock::now();
        for (auto i = 0; i < NUM_ITERATIONS; i++) {
            FindMaxSubarrayLinear(arr, 0, inputSize);
        }
        stop = std::chrono::high_resolution_clock::now();
        auto timeLinear = (float) std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count() / (float) NUM_ITERATIONS;
        printf("%d \t %8.4f \t %7.4f \t %6.4f\n", inputSize, timeBruteForce, timeRecursive, timeLinear);

        // Free allocated memory
        delete arr;

        // Increment loop counter
        inputSize += 1;

        // Just for curiosity, want to run 4 extra loops after finding crossover point between brute force and recursive
        if (crossOverInputSize > 0 && inputSize > crossOverInputSize + 4) {
            done = true;
        }
    }

    return 0;
}
