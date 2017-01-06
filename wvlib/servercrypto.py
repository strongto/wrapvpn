import nacl.utils
import base64
from nacl.encoding import Base64Encoder as b64
from nacl.public import PrivateKey, PublicKey, Box

class CryptoContext(object):
    """
    Context used for performing cryptography on a stream
    """
    def __init__(self, pubkey, mypriv):
        super(CryptoContext, self).__init__()
        print(pubkey)
        print(len(pubkey))
        self.tcvpub = PublicKey(pubkey, encoder=b64)
        self.cvpriv = PrivateKey(mypriv, encoder=b64)
        self.cvpub = self.cvpriv.public_key

    def precompute(self):
        self.box = Box(self.cvpriv, self.tcvpub)
        print("Precomputation done, yay!")
        pass

    def encrypt(self, pt):
        nonce = nacl.utils.random(24)
        return base64.b64encode(self.box.encrypt(pt, nonce))

    def decrypt(self, ct):
        pt = None
        try:
            pt = self.box.decrypt(base64.b64decode(ct))
        except Exception:
            return b'', False
        else:
            return pt, False
        pass
