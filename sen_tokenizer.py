from nltk import tokenize
import nltk
nltk.download('punkt')
import re

text = """A man who left a three-month-old child fighting for life after forcing a baby wipe into his bottom to prevent a dirty nappy has been admonished.Graeme McArthur, 39, from Cambuslang, South Lanarkshire, admitted endangering the boy's life in February last year.But at the High Court in Glasgow, judge Lord Turnbull described his actions as "misguided intervention rather than as an act of malice".It is unclear if the injured child will make a full recovery.At an earlier hearing, the court heard how the incident occurred as McArthur, who was looking after the child, changed his nappy.The wipe was deliberately put into the child's body in a bid to stop him from soiling his nappy.The next day in a bid to remove the wipe using his fingers, McArthur caused significant internal injuries, including a perforated bowel.The baby's mother later took him to a local GP as he was quiet and pale and whimpering. The doctor immediately arranged for an ambulance to take the child to Hairmyres Hospital in East Kilbride.When he was admitted, the baby was close to death and had to be resuscitated. He was then transferred to Yorkhill Hospital in Glasgow and underwent a four-and-a-half hour operation to repair his bowel. During the operation the wipe was removed from inside the child's abdomen.A consultant paediatrician was of the opinion that the pain for the baby would have been excruciating.When McArthur was questioned by police about the injuries they found him to be somewhat vague and evasive.After the case went to court he admitted acting culpably and recklessly and with utter disregard for the consequences and to the danger of the life of the baby boy between 14 and 17 February last year.In a judgement read in court, Lord Turnbull said: "I am not saying he was right to do what he did or that it could be condoned."However, I reject as baseless any suggestion that his behaviour was sexually motivated."Lord Turnbull said that this was one of the most anxious cases ever to have appeared before him and said that McArthur presented as "a distraught and flawed man".Admonishing McArthur, he added that his conduct was the result of "wholly misguided intervention rather than as an act of malice".The ruling means McArthur's conviction is still recorded but he is neither imprisoned nor fined."""

sentences = tokenize.sent_tokenize(text)
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
