import urllib.request,json
from .models import Quote


# Getting the movie base url
base_url = None


def configure_request(app):
    global base_url

    base_url = app.config['QUOTE_API_BASE_URL']


def get_quotes():
  '''Function that gets the json response from Url request'''
  get_quotes_url = base_url

  with urllib.request.urlopen(get_quotes_url) as url:
    get_quotes_data = url.read()
    get_quotes_response = json.loads(get_quotes_data)

    quotes_results = None

    if get_quotes_response:
      quotes_results_list = get_quotes_response
      quotes_results =quotes_results_list

  return quotes_results 

# def process_results(qoutes_list):
#   '''function to process qoutes results'''
#   quotes_results = []
#   for qoutes_item in qoutes_list:

#     author = qoutes_item.get('author')
#     id = qoutes_item.get('id')  
#     quote = qoutes_item.get('quote')
#     quotes_object = Quote(author,id,quote)
#     quotes_results.append(quotes_object)

#   return quotes_results


