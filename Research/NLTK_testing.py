import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

class nltkTesting:

    def nltkDownloader(self):
        # function to run the NLTK downloader to download NLTK packages
        nltk.download()

    def sentenceTokenizing(self, sentence):

        print(sent_tokenize(sentence))

    def wordTokenizing(self, sentence):

        print(word_tokenize(sentence))
        print("\n")
        for i in word_tokenize(sentence):
            print(i)

    def wordFiltration(self, sentence):

        stop_words = set(stopwords.words("english"))
        #print(stop_words)

        words = word_tokenize(sentence)

        # Checking if stop words appear in sentence and filtering them out of sentence
        filtered_sentence = [i for i in words if not i in stop_words]

        print(filtered_sentence)

    def main(self):
        sentence = "There is only one Lord of the Ring, only one who can bend it to his will. And he does not share power."

        #self.nltkDownloader()
        #self.sentenceTesting(sentence)
        #self.wordTokenizing(sentence)
        self.wordFiltration(sentence)

if __name__ == '__main__':
    languageProcessing = nltkTesting()
    languageProcessing.main()