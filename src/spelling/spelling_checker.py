import io
import time

start_time = time.time()

input_file = "types.txt"

suggestion_amount = 7
maximum_error = 7

with io.open(input_file, encoding='utf8') as file: 
  text = file.read()
  file.close()

text = text.split()
types = dict()
for i in range(0, len(text), 2):
  types[text[i]] = int(text[i + 1])

def lev_dist(s1 : str, s2 : str) -> int:
  ans = 0
  dist = list()
  for i in range(0, len(s1) + 1):
    dist.append(list())
    for j in range(0, len(s2) + 1):
      dist[i].append(0)

  for i in range(0, len(s1) + 1):
    dist[i][0] = i
  for i in range(0, len(s2) + 1):
    dist[0][i] = i

  for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
      dist[i][j] = min(dist[i - 1][j] + 1, dist[i][j - 1] + 1, dist[i - 1][j - 1] + 2 * (s1[i - 1] != s2[j - 1]))

  return dist[len(s1)][len(s2)]

while True:
  s = input("Enter the word to check the spelling or \"/exit\" to terminate: ")

  if s == "/exit":
    break

  suggestions = dict()

  for key in types.keys():
    suggestions[key] = lev_dist(s, key)

  suggestions = sorted(suggestions.items(), key=lambda item: item[1])

  print("Possible variants are: ")
  for i in range(0, suggestion_amount):
    if (suggestions[i][1] > maximum_error):
      break
    print(suggestions[i][0])
  print()

end_time = time.time()

print("Time spent: " + str(end_time - start_time) + " seconds")