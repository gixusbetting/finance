import grpc,json
import proto.finance_pb2 as types
import proto.finance_pb2_grpc as finance
from google.protobuf.json_format import MessageToJson

def run():
    stub = finance.PaymentStub(grpc.insecure_channel('localhost:50057'))
    # response = stub.MakePaynowDeposit(types.PaynowPayload(
    #     ref="123",
    #     amount=10,
    #     method="omari",
    #     phone="0786854223",
    #     email="dzbusiness01@gmail.com",
    # ))
    # print(response)
    response = stub.MakeCryptoDeposit(types.CryptoPayload(
        amount=50,
        orderId="123",
        method="usdttrc20"
    ))
    print(response)

if __name__ == '__main__':
    run()