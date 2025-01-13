import json
import io
import time

start_time = time.time()

input_file = "json_text/sputnikaz.json"
output_file = "text_corpus.txt"

with open(input_file, encoding="utf-8") as file:
  data = json.load(file)
  file.close()

with io.open(output_file, 'a', encoding="utf-8") as file:
  for msg in data["messages"]:
    for msg_data in msg["text_entities"]:
      file.write(msg_data["text"])
    file.write("\n")
  print()
  file.close()

end_time = time.time()

print("Time spent: " + str(end_time - start_time) + " seconds")