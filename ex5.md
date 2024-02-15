Exercise 5:

1.
Timing a program can be tricky due to various factors like system changes and background processes.
Python's timeit module offers two ways to handle this. The first method, using the number parameter,
ensures the timing is done a specific number of times to smooth out small variations.
The second method, using repeat, runs the code multiple times, giving a list of timings for statistical analysis to account for variability.
Choosing between them depends on the need for a single accurate measurement (use timeit) or a more comprehensive analysis of variations (use repeat).

2.
For the output of timeit.timeit(), it's best to use the average statistic. This function gives the time for a single run,
and averaging over multiple runs helps create a stable and representative measurement, minimizing the impact of short-term fluctuations.
On the other hand, for the output of timeit.repeat(), which provides a list of timings from several runs,
it's more suitable to use statistics like minimum, maximum, and average.
These statistics offer a broader perspective on performance variability across different executions, providing a comprehensive assessment of the code's efficiency.