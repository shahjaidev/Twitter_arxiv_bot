from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
 
def read_article(file_name):
    """
    file = open(file_name, "r")
    filedata = file.readlines()
    """
    doc_str= r"""Natural language is perhaps the most versatile and intuitive way for humans to communicate tasks to a robot. Prior work on Learning from Play (LfP) [Lynch et al, 2019] provides a simple approach for learning a wide variety of robotic behaviors from general sensors. However, each task must be specified with a goal image---something that is not practical in open-world environments. In this work we present a simple and scalable way to condition policies on human language instead. We extend LfP by pairing short robot experiences from play with relevant human language after-the-fact. To make this efficient, we introduce multicontext imitation, which allows us to train a single agent to follow image or language goals, then use just language conditioning at test time. This reduces the cost of language pairing to less than 1% of collected robot experience, with the majority of control still learned via self-supervised imitation. At test time, a single agent trained in this manner can perform many different robotic manipulation skills in a row in a 3D environment, directly from images, and specified only with natural language (e.g. "open the drawer...now pick up the block...now press the green button..."). Finally, we introduce a simple technique that transfers knowledge from large unlabeled text corpora to robotic learning. We find that transfer significantly improves downstream robotic manipulation. It also allows our agent to follow thousands of novel instructions at test time in zero shot, in 16 different languages. See videos of our experiments at language-play.github.io/"""

    article_li = doc_str.split(". ")
    sentences = []

    for sentence in article_li:
        #print(sentence)
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop() 
    
    print(sentences)
    return sentences

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    sentences =  read_article(file_name)

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize texr
    print("Summarize Text: \n", ". ".join(summarize_text))

# let's begin
generate_summary( "msft.txt", 1)