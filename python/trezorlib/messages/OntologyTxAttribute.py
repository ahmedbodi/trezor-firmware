# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p


class OntologyTxAttribute(p.MessageType):

    def __init__(
        self,
        usage: int = None,
        data: bytes = None,
    ) -> None:
        self.usage = usage
        self.data = data

    @classmethod
    def get_fields(cls):
        return {
            1: ('usage', p.UVarintType, 0),
            2: ('data', p.BytesType, 0),
        }
