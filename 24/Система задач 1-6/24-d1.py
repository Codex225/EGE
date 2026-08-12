import time

start_time = time.time()

line = open("24-d1.txt").readline()
maxlen = 0
s = ""
for i in range(len(line)):

    if line[i] in "ACGK":
        s = s + line[i]
    else:
        maxlen = max(maxlen, len(s))
        s = ""
print(maxlen)
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")

s = open('24-d1.txt').read().strip()

k = m = 0
for i in range(len(s)):
  if s[i] in 'ACGK':
    k += 1
    m = max(m,k)
  else:
    k = 0
print(m)

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")
