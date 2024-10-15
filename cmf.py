import requests
api_key = "f5aacd4fc380bce272fd76faee48cdf290d9a105"
year = 2023
month = 11

url = f"https://api.cmfchile.cl/api-sbifv3/recursos_api/resultados/{year}/{month}/instituciones?apikey={api_key}&formato=json"

response = requests.get(url)
data = response.json()
print(data)
for cod in data["DescripcionesCodigosdeInstituciones"]:
    if cod["CodigoInstitucion"] != ´999´:
        print(cod["CodigoInstitucion"], cod["NombreInstitucion"]