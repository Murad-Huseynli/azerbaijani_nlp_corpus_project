import io
import time

start_time = time.time()

input_file = "text_corpus.txt"
output_file = "bpe_tokenized.txt"

with io.open(input_file, encoding='utf8') as file: 
  text = file.read()
  file.close()

vocabulary = set()
symbols = list()

for letter in text:
  if letter != " " and letter != "\n":
    vocabulary.add(letter)
    symbols.append(letter)
  else:
    if len(symbols) != 0 and symbols[len(symbols) - 1] != ">_<":
      symbols.append(">_<")
vocabulary.add(">_<")

def check_all_pairs() -> str:
  best = 0
  best_pair = ""
  pairs_cnt = dict()

  i = 0
  while i < len(symbols) - 1:
    if symbols[i] != ">_<" and symbols[i] + symbols[i + 1] not in pairs_cnt:
      pairs_cnt[symbols[i] + symbols[i + 1]] = 0
    if symbols[i] != ">_<":
      pairs_cnt[symbols[i] + symbols[i + 1]] += 1
    i += 1

  for pair, cnt in pairs_cnt.items():
    if cnt > best:
      best = cnt
      best_pair = pair
  return best_pair

def change_symbols(pair : str):
  global symbols
  new_symbols = list()
  i = 0
  while i < len(symbols):
    if i < len(symbols) - 1 and symbols[i] + symbols[i + 1] == pair:
      new_symbols.append(pair)
      i += 1
    else:
      new_symbols.append(symbols[i])
    i += 1
  symbols = new_symbols.copy()
          
for k in range (0, 1000):
  print(k)
  new_pair = check_all_pairs()
  change_symbols(new_pair)
  vocabulary.add(new_pair)

with io.open(output_file, 'w', encoding="utf-8") as file:
  for word in vocabulary:
    file.write(word + "\n")
  file.close()

end_time = time.time()

print("Time spent: " + str(end_time - start_time) + " seconds")