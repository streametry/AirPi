import output
import requests
import json

class Streametry(output.Output):
	requiredData = ["hostPort","FeedID"]
	optionalData = []
	def __init__(self,data):
		self.hostPort=data["hostPort"]
		self.FeedID=data["FeedID"]
	def outputData(self,dataPoints):
		arr = []
		data = {}
		for i in dataPoints:
			data[ i["name"] ] = i["value"]
			#arr.append({"id":i["name"],"current_value":i["value"]})
		a = json.dumps(data)
		print a
		try:
			z = requests.put("http://streametry.com:8181/demo/airpi/home1",headers={},data=a)
			if z.text!="": 
				print "Streametry Error: " + z.text
				return False
		except Exception:
			return False
		return True
