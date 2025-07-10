import grpc,os
from concurrent import futures
from dotenv import load_dotenv
import proto.finance_pb2_grpc as finance
from services.payment import PaymentService
load_dotenv()

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    finance.add_PaymentServicer_to_server(PaymentService(), server)
    server.add_insecure_port(f"[::]:{os.getenv('PORT')}")
    server.start()
    print(f"Server running on port {os.getenv('PORT')}")
    server.wait_for_termination()