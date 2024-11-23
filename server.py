import grpc
from concurrent import futures
import square_pb2
import square_pb2_grpc

class SquareService(square_pb2_grpc.SquareServiceServicer):
    def GetSquare(self, request, context):
        return square_pb2.SquareResponse(result=request.number ** 2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    square_pb2_grpc.add_SquareServiceServicer_to_server(SquareService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
