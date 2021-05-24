import grpc
import bc_pb2
import bc_pb2_grpc
from csv import reader
from google.protobuf import json_format
from concurrent import futures
from json import loads 

class usageService (bc_pb2_grpc.usageServicer):
    def sendMetricData(self,request,context):
        if request.sendFlag==1:
            #excel_data = bc_pb2.excelData()
            timeSeriesData=bc_pb2.timeSeries()
            with open('meterusage.1620825451.csv', 'r') as read_obj:
                     csv_reader = reader(read_obj)
                     header = next(csv_reader)
                     for row in csv_reader:
                      var=timeSeriesData.data.add()
                      var.time = row[0]
                      var.meterusage = row[1]
                      #excel_data.time = row[0]
                      #excel_data.meterusage = row[1]
                      #byytes = excel_data.SerializeToString()
                      byytes = timeSeriesData.SerializeToString()
                      #print(bbytes)
                     return bc_pb2.metricResponse(result=byytes)
                    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bc_pb2_grpc.add_usageServicer_to_server(
    usageService(), server
    )
    
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
