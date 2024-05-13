from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False

private_key, public_key = generate_key_pair()

message = b"Hello, this is a test message."
print("Original Message:", message)

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(message)
hashed_message = digest.finalize()
print("Hashed Message:", hashed_message.hex())

signature = sign_message(private_key, hashed_message)
print("Signature:", signature.hex())

verification_result = verify_signature(public_key, hashed_message, signature)
print("Signature Verification Result:", verification_result)