import os
import time
from statistics import mean

from main import valid_words_search


def test_perf_measure():
    measure_result = []
    for i in range(20):
        time_start = time.time()
        valid_words_search()
        measure_result.append(time.time() - time_start)
    mean_performance = mean(measure_result)
    print(os.linesep)
    print(mean_performance)
    assert mean_performance < 0.5

