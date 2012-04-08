import os

from Concordance import Concordance
from flask import Flask
app = Flask(__name__)

concordance = Concordance()

@app.route('/count/<word>')
def word_count(word):
	count = concordance.count_for_word(word)
	return str(count)

@app.route('/most_common')
def most_common():
	words = concordance.most_common_words(10)
	return ','.join(words)

if __name__ == '__main__':
	for line in open('lovecraft.txt'):
		line = line.strip()
		concordance.feed(line)
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

