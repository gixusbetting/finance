import grpc
import os,requests
from dotenv import load_dotenv
import proto.finance_pb2 as types
import proto.finance_pb2_grpc as finance
load_dotenv()

class PaymentService(finance.PaymentServicer):
    def MakeCryptoDeposit(self, request: types.CryptoPayload, context: grpc.aio.ServicerContext):
        try:
            webhook=f"{os.getenv('BASE_URL')}/finance/deposit-webhook/{request.orderId}?provider=crypto"
            response = requests.post(f"{os.getenv('CRYPTO_BASE_URL')}/payment",json={
                "price_currency": "usd",
                "is_fee_paid_by_user": True,
                "ipn_callback_url": webhook,
                "order_id": request.orderId,
                "price_amount": request.amount,
                "pay_currency": request.method,
            },headers={"X-Api-Key": os.getenv('CRYPTO_API_KEY')})
            if response.status_code != 201: return types.CryptoResponse(Instructions=response.text,StatusCode=response.status_code)
            data = response.json()
            return types.CryptoResponse(
                Network=data.get("network"),
                OrderID=data.get("order_id"),
                CreatedAt=data.get("created_at"),
                PayAmount=data.get("pay_amount"),
                PaymentID=data.get("payment_id"),
                PayAddress=data.get("pay_address"),
                PayCurrency=data.get("pay_currency"),
                PriceCurrency=data.get("price_currency"),
                PaymentStatus=data.get("payment_status"),
                ExpirationEstimateDate=data.get("expiration_estimate_date"),
                StatusCode=200
            )
        except Exception as ex:
            return types.CryptoResponse(Instructions=str(ex),StatusCode=500)