from textblob import TextBlob
import random


"""
this is our grammar, it represents the structure of one or more sentences
we are going to use it as a reference to generate concrete sentences.
some abbreviations are as follows:
    S: sentence
    NP: noun phrase
    VP: verb phrase
    N: noun
    V: verb
    J: adjective
    PP: prepositional phrase
    PP: preposition
    det: determinant/article
"""

my_grammar = {
        "S": ["NP VP NP"],                              # the left part is called an axiom
        "NP": ["det ADJ N"],                    # the right part is a list of which elements that axiom is made of
        "det": ["the", "a"],
        "VP": ["V3"],                       # notice how the list on the left sometimes contains other axioms
        "N": ["feeling", "emotion", "euphoria", "affection","sentiment","passion","desire","guilt","wrongdoing","evil","wickedness","sin","immorality","deception"],
        "V3": ["demonstrates", "manifests", "presents", "shows", "exhibits"],
        "ADJ": ["burning","captivating","lustful","pleasing","gorgeous","grotesque","horrid", "hideous", "deformed","disfigured","loathsome"]
        }


# this is the function that is going to generate a sentence.
# its arguments are a grammar (the rules to follow) and an axiom (the starting point)
def write_a_sentence(grammar, axiom):

    sentence = list()                                               #we start by creating a list which will store all the words for our sentence

    if axiom in grammar:                                            # if we find one of the axioms (such as NP, V, etc.) as a key in our grammar
        expansion = random.choice(grammar[axiom])                   # then we pick one random item from the list on the left side of the corresponding axiom

        for token in expansion.split():                             # we split the element in separate tokens (e.g. "the N" becomes ["the", "N"]) and we can then look for "N"
            sentence.extend(write_a_sentence(grammar, token))       # if we've found an axiom, we call our function again to dive deeper into our grammar
    else:
        sentence.append(axiom)                                      # until we find nothing, in which case we will append the current axiom (which will be a word, instead of something like "N", or "VP")

    return sentence                                                 # and we return all that we've found!


for i in range(0, 5):                                               # this is how you write a for loop in python
    words = write_a_sentence(my_grammar, "S")                       # we want a write a sentence using my_grammar defined above, and with the starting point "S"
    my_sentence = " ".join(words)                                   # because it returns a list, we need to join all elements with a space
    print my_sentence + "."                                         # and we print it!