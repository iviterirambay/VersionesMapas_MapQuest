import urllib.parse
import requests

main_api="https://www.mapquestapi.com/directions/v2/route?"
key="KEY"

while True:
    orig=input("Starting Location: ").lower()
    if orig == "quit" or orig == "q":
        break
    dest=input("Destination: ").lower()
    if dest == "quit" or dest == "q":
        break
    url=main_api+urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    print("URL: "+(url))
    json_data=requests.get(url).json()
    json_status=json_data["info"]["statuscode"]
    if json_status==0:
        print("APIStatus: "+str(json_status)+" = A successful route call.\n")
        print("=============================================")
        print("Directions from "+(orig)+" to "+(dest))
        print("Trip Duration: "+(json_data["route"]["formattedTime"]))
        print("Kilometers: "+str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("FuelUsed(Ltr): "+str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")