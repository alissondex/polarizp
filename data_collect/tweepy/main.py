import tweepy
import sys
import json

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

def search_tweets(query, count = 5):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	
	try:
		auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)
	except:
		print("Erro ao autenticar a aplicação")
		quit()

	list_of_tweets = []

	try:

		# TODO: e se não for adicionado o total 'count' de tweets ?
		for tweet in tweepy.Cursor(api.search, q = query, count = count, result_type = "recent", lang = "en").items():
			if tweet.retweeted == False:
				list_of_tweets.append(tweet._json)

			if(len(list_of_tweets) >= count):
				break

	except tweepy.TweepError as e:
		print("Erro ao buscar os tweets pelo tweepy")
		print("Detalhes: {}".format(str(e)))
		quit()

	return list_of_tweets

def write_tweets_to_file(tweets, output_file):

	with open(output_file, 'w') as fp:
		status = {"statuses" : tweets}
		json.dump(status, fp)
	fp.close()

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

	tweets = search_tweets(query, count)
	write_tweets_to_file(tweets, output_file)

if __name__ == "__main__":
	main()