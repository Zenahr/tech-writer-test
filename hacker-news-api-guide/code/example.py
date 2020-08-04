import requests

url = "https://hacker-news.firebaseio.com/v0/beststories.json"
response = requests.get(url).json()[:50]
print("Amount of results:", len(response))
print("IDs:", response)

def id_to_link(id):
    return "https://news.ycombinator.com/item?id=" + str(id)

def id_list_to_link_list(id_list):
    return [id_to_link(id) for id in id_list]

link_list = id_list_to_link_list(response)
print("Links:", link_list)