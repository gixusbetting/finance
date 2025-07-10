import os,requests
from paynow import Paynow 
from dotenv import load_dotenv
import proto.finance_pb2 as types
import proto.finance_pb2_grpc as finance
from google.protobuf.json_format import Parse
load_dotenv()

result_url = f"{os.getenv('BASE_URL')}/result"
paynow = Paynow(os.getenv('INTEGRATION_ID'), os.getenv('INTEGRATION_KEY'),result_url,result_url)

class PaymentService(finance.PaymentServicer):
    def MakePaynowDeposit(self, request, context):
        try:
            payment = paynow.create_payment(request.ref, request.email)
            payment.add(request.ref, request.amount)
            response = paynow.send_mobile(payment, request.phone, request.method)
            if response.success:
                pollurl = response.data.get('pollurl') # type: ignore
                ref=response.data.get('paynowreference') # type: ignore
                instructions=response.data.get('instructions') # type: ignore
                code = response.data.get('authorizationcode') # type: ignore
                expiry = response.data.get('authorizationexpires') # type: ignore
                return types.PaynowResponse(ref=ref,url=pollurl,code=code,expiry=expiry,instructions=instructions)
            else:
                return types.Error(message=response.data.get('error')) # type: ignore
        except Exception as ex:
            return types.Error(message=str(ex))
        
    def MakeCryptoDeposit(self, request: types.CryptoPayload, context):
        webhook=f"{os.getenv('BASE_URL')}/finance/crypto/deposit/{request.orderId}"
        response = requests.post(f"{os.getenv('CRYPTO_BASE_URL')}/payment",json={
            "price_currency": "usd",
            "is_fee_paid_by_user": True,
            "ipn_callback_url": webhook,
            "order_id": request.orderId,
            "price_amount": request.amount,
            "pay_currency": request.method,
        },headers={"X-Api-Key": os.getenv('CRYPTO_API_KEY')})
        if response.status_code != 200: return types.Error(message=response.text)
        return Parse(response.json(), types.CryptoResponse())