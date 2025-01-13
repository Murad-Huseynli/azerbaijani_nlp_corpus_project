import io
import re
import time
from heaps_law import Calculate as hl_calc

start_time = time.time()

input_file = "text_corpus.txt"
output_file = "sentences.txt"

general_regex = r"[!?\n]"
period_regex = r"\. "

with io.open(input_file, encoding='utf8') as file: 
  text = file.read()
  file.close()

sentences = re.split(general_regex + "|" + period_regex, text)

with io.open(output_file, 'w', encoding="utf-8") as file:
  for sentence in sentences:
    file.write(sentence + "\n")
  file.close()

end_time = time.time()

print("Time spent: " + str(end_time - start_time) + " seconds")