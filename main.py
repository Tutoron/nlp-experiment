import spacy

def process(sentence):
    nlp = spacy.load('en')
    doc = nlp(sentence)
    print([(w.text, w.pos_) for w in doc])

def main():
    print("starting main ...")
    process(u'This is a definition, and not an application of Bayes theorem, since Bayes theorem can only be applied when all distributions are proper. However, it is not uncommon for the resulting "posterior" to be a valid probability distribution.')

if __name__ == "__main__":
    main()
