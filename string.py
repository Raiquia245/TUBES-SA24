import timeit

def brute_force(text, pattern):
    n = len(text)
    all_attempts = []
    solusi = []

    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = text[start:end]
            all_attempts.append((start, substring))  

    for index, substring in all_attempts:
        if substring == pattern:  
            solusi.append(index)  

    return solusi




def backtrack(text, pattern):
    n = len(text)
    m = len(pattern)
    solusi=[]
    attempt=[]

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        
        attempt.append((i,j))

    for i, j in attempt:
        if j == m:  
            solusi.append(i)  
    
    return solusi







text = "SA itu menyenangkan bukan?"
pattern = "bukan"


num_trials = 5

# Mengukur waktu eksekusi masing-masing metode
time_backtrack = timeit.timeit(lambda: backtrack(text, pattern), number=num_trials) / num_trials
time_brute_force = timeit.timeit(lambda: brute_force(text, pattern), number=num_trials) / num_trials
# print(backtrack(text, pattern))
# print(brute_force(text, pattern))
# Menampilkan hasil
print(len(text))
print(len(pattern))
time_backtrack = round(time_backtrack, 10)
time_brute_force = round(time_brute_force, 10)
print("Waktu eksekusi rata-rata (Backtrack):", time_backtrack, "detik")
print("Waktu eksekusi rata-rata (Brute Force):", time_brute_force, "detik")
