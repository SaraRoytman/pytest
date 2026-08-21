def add(a, b):
    return a + b

def rollingAvg(arr, n):
    res = []
    
    for i in range(len(arr) - n + 1):
        window_sum = sum(arr[i:i+n])
        res.append(window_sum / n)
    return res