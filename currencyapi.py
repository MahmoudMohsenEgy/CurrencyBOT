import eventlet
eventlet.monkey_patch()
import requests

BASE_URL="https://api.frankfurter.app/latest?"
def getQuery(amount,cur1,cur2):
    query = "from="+cur1+"&to="+cur2+"&amount="+str(amount)
    return query

def callAPI(amount,cur1,cur2):
    print("HEllo from inside callAPI")
    final_URL = BASE_URL+getQuery(amount,cur1,cur2)
    print("I GOT QUERY "+ str(final_URL))
    response = requests.get(final_URL)
    print("response before jsonifying")
    response = response.json()
    print("response after jsonifying")

    print("Response\n\n\n\n")
    print(response)
    print("\n\n\n\n")
    final_response = str(response['amount']) +" "+ str(response['base'])   + " = " + str(response['rates'][cur2]) + " " +cur2
    return final_response

print(callAPI(70,"EUR","USD"))