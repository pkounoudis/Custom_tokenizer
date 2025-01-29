from nltk import tokenize
import nltk
nltk.download('punkt')
import re

sentences = tokenize.sent_tokenize(BBC_Data[num]["content"])
pattern6 = r'(?<=[.?!])["\']?\s*(?=[A-Z])'

for sen in range(0, len(sentences)):

  matches = re.findall(pattern6, sentences[sen])

  if matches != []:
    sentences[sen] = re.split(r'(?<=[.?!])["\']?\s*(?=[A-Z])', sentences[sen])

new_text = []
for sentt in range(0, len(sentences)):
  if type(sentences[sentt]) == list:

    for j in sentences[sentt]:

      new_text.append(j)
  else:
    new_text.append(sentences[sentt])

print(new_text)
print()

newer_text = ". ".join(new_text)
new_est_text = newer_text.replace("..", ".")

print(new_est_text)
