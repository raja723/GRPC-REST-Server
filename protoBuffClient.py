import grpc
import bc_pb2
from bc_pb2 import metricResponse
from bc_pb2 import metricRequest
from bc_pb2 import excelData
from bc_pb2_grpc import usageStub
from google.protobuf import json_format

#excel_data = bc_pb2.excelData()
timeSeriesData=bc_pb2.timeSeries()
channel = grpc.insecure_channel("localhost:50051")
client =usageStub(channel)
request=metricRequest(sendFlag=1)
finalResult=client.sendMetricData(request)
#print(finalResult)
#excel_data.ParseFromString(finalResult.result)
timeSeriesData.ParseFromString(finalResult.result)
#json_string = json_format.MessageToJson(excel_data)
json_string = json_format.MessageToJson(timeSeriesData)
#print(json_string) 
