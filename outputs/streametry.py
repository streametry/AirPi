import output
import requests
import json

class Streametry(output.Output):
	requiredData = ["url"]
	optionalData = []
	def __init__(self,data):
		self.url=data["url"]

	def outputData(self,dataPoints):
		arr = []
		data = {}
		for i in dataPoints:
			data[ i["name"] ] = i["value"]
			
		jsonData = json.dumps(data)
		
		try:
			z = requests.put(self.url,headers={},data=jsonData)
			if z.text!="": 
				print "Error: " + z.text
				return False
		except Exception:
			return False
		return True
