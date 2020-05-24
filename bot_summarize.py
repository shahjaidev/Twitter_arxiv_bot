from gensim.summarization.summarizer import summarize 
#import wikipedia
#import spacy


#wikisearch = wikipedia.page("Deep Learning") 
#wikicontent = wikisearch.content 
#nlp = spacy.load("en_core_web_sm")


doc_str= r"""Natural language is perhaps the most versatile and intuitive way for humans to communicate tasks to a robot. Prior work on Learning from Play (LfP) [Lynch et al, 2019] provides a simple approach for learning a wide variety of robotic behaviors from general sensors. However, each task must be specified with a goal image---something that is not practical in open-world environments. In this work we present a simple and scalable way to condition policies on human language instead. We extend LfP by pairing short robot experiences from play with relevant human language after-the-fact. To make this efficient, we introduce multicontext imitation, which allows us to train a single agent to follow image or language goals, then use just language conditioning at test time. This reduces the cost of language pairing to less than 1% of collected robot experience, with the majority of control still learned via self-supervised imitation. At test time, a single agent trained in this manner can perform many different robotic manipulation skills in a row in a 3D environment, directly from images, and specified only with natural language (e.g. "open the drawer...now pick up the block...now press the green button..."). Finally, we introduce a simple technique that transfers knowledge from large unlabeled text corpora to robotic learning. We find that transfer significantly improves downstream robotic manipulation. It also allows our agent to follow thousands of novel instructions at test time in zero shot, in 16 different languages. See videos of our experiments at language-play.github.io/"""


#doc_str= str(doc)
doc_length= len(doc_str)


tweet_ratio= 140/doc_length
print(tweet_ratio)
summarized = summarize(doc_str, ratio = tweet_ratio) 
print(summarized)
print(len(summarized))


next_sum= summarize(summarized, 0.7)