########### Python 3.2 #############

#Personalize user experiences with emotion recognition
# 30,000 transactions, 20 per minute.
# Endpoint: https://westus.api.cognitive.microsoft.com/emotion/v1.0
# Key 1: 316ceff7c3af49acbaecdd4dd478438a
# Key 2: bfffe1c81e45472d8c3f63f2b912caef

import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '316ceff7c3af49acbaecdd4dd478438a',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'https://www.ynetnews.com/articles/0,7340,L-5076828,00.html' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
except Exception as e:
    print(e.args)
####################################
