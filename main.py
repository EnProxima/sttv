import argparse
import spacy
import pandas as pd

# Load Spanish tokenizer, tagger, parser and NER
nlp = spacy.load("es_core_news_lg")
#Command line parcer settings
parser = argparse.ArgumentParser(description='Text to Vocabulary - Spanish')
parser.add_argument('infile', type=str, help='Input filename')
parser.add_argument('outfile', type=str, help='Output filename')
args = parser.parse_args()


try:
    print("try to open '%s' file..."% args.infile, end =" ")
    text=open(args.infile,encoding='utf-8-sig').read()
    print('OK')
except:
    print (' ')
    print ("can't read '%s'. Please, check  the filepath" % args.infile)
    exit()

print('analyze text...',end =" ")
doc = nlp(text)
print('OK')
# Analyze
words_df=pd.DataFrame()
i=1

for token in doc:
    if not token.pos_ in('PUNCT', 'DET', 'ADP', 'SPACE','CCONJ','NUM','SYM'):
      words_df=words_df.append({'type':token.pos_, 'word':token.lemma_}, ignore_index=True)
      print('build vocabulary...',i, end="\r")
      i=i+1
print('build vocabulary... OK')
print('lowercase vocabulary...',end =" ")
words_df['word']=words_df['word'].str.lower()
print('OK')
print('drop duplicates...',end =" ")
words_df=words_df.drop_duplicates(subset='word', keep='first')
print('OK')
try:
    print("try to save to '%s' file.."% args.outfile,end =" ")
    words_df.to_csv(args.infile)
    print('OK')
    print ('--------------------')
    print ('Vocabulary length: ',len(words_df))
except:
    print ("Can't save to %s file." % args.infile)









