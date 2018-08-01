import requests
import json
import sys
from requests_oauthlib import OAuth1

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

def search_tweets(query, count = 5):
	url = "https://api.twitter.com/1.1/search/tweets.json?q={}&count={}&result_type=popular&lang={}".format(query, count, 'en')
	auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

	result = requests.get(url, auth = auth)

	return result.json()

def main():

	count = 10
	if len(sys.argv) < 3:
		print("Erro ao ler os argumentos. Tente: ")
		print("")
		print("python3 " + sys.argv[0] + " query-de-busca contador")
		print("")
		print("query-de-busca: string utilizada para buscar os tweets")
		print("contador: numero de tweets a serem obtidos")
		print("")
		print("Atenção: Como esta é uma busca por meio de aplicação não paga, o limite de tweets disponiveis será limitado pelo twitter")
		quit()

	query = sys.argv[1]
	output_file = sys.argv[2]

	if len(sys.argv) > 3:
		try:
			count = int(sys.argv[3])
		except ValueError:
			print("Insira um valor numerico no 'contador'")
			quit()

	response = search_tweets('Donald Trump', count)
	
	with open('data.json', 'w') as fp:
		json.dump(response, fp)

if __name__ == "__main__":
	main()