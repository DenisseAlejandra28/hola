import sys #permite trabajar con linea de comandos
import requests # importa la biblioteca requests

if len(sys.argv) != 2:
    sys.exit()


response = resquests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1])
o = response-json()

#print(json.dumps(response.json(), indent=2))
for result in o ["results"]:
    print(result["trackname"])