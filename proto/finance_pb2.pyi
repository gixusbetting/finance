from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaynowPayload(_message.Message):
    __slots__ = ("ref", "amount", "email", "phone", "method")
    REF_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ref: str
    amount: float
    email: str
    phone: str
    method: str
    def __init__(self, ref: _Optional[str] = ..., amount: _Optional[float] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...

class PaynowResponse(_message.Message):
    __slots__ = ("ref", "url", "code", "expiry", "instructions", "statusCode")
    REF_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    ref: str
    url: str
    code: str
    expiry: str
    instructions: str
    statusCode: int
    def __init__(self, ref: _Optional[str] = ..., url: _Optional[str] = ..., code: _Optional[str] = ..., expiry: _Optional[str] = ..., instructions: _Optional[str] = ..., statusCode: _Optional[int] = ...) -> None: ...

class CryptoPayload(_message.Message):
    __slots__ = ("orderId", "amount", "method")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    orderId: str
    amount: float
    method: str
    def __init__(self, orderId: _Optional[str] = ..., amount: _Optional[float] = ..., method: _Optional[str] = ...) -> None: ...

class CryptoResponse(_message.Message):
    __slots__ = ("Network", "OrderID", "CreatedAt", "PayAmount", "PaymentID", "PayAddress", "PayCurrency", "PriceCurrency", "PaymentStatus", "ExpirationEstimateDate", "StatusCode", "Instructions")
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    PAYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENTID_FIELD_NUMBER: _ClassVar[int]
    PAYADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYCURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRICECURRENCY_FIELD_NUMBER: _ClassVar[int]
    PAYMENTSTATUS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATIONESTIMATEDATE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    Network: str
    OrderID: str
    CreatedAt: str
    PayAmount: float
    PaymentID: str
    PayAddress: str
    PayCurrency: str
    PriceCurrency: str
    PaymentStatus: str
    ExpirationEstimateDate: str
    StatusCode: int
    Instructions: str
    def __init__(self, Network: _Optional[str] = ..., OrderID: _Optional[str] = ..., CreatedAt: _Optional[str] = ..., PayAmount: _Optional[float] = ..., PaymentID: _Optional[str] = ..., PayAddress: _Optional[str] = ..., PayCurrency: _Optional[str] = ..., PriceCurrency: _Optional[str] = ..., PaymentStatus: _Optional[str] = ..., ExpirationEstimateDate: _Optional[str] = ..., StatusCode: _Optional[int] = ..., Instructions: _Optional[str] = ...) -> None: ...
