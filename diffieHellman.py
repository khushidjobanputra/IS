# Publicly known prime number and base
p = 23  # Prime number
g = 5   # Base

# Alice's private key
private_key_A = int(input("Enter key for Alice: "))
# Bob's private key
private_key_B = int(input("Enter key for Bob: "))

# Calculate Xa (Alice's public key)
Xa = (g ** private_key_A) % p 
# Calculate Xb (Bob's public key)
Xb = (g ** private_key_B) % p

# Calculate Ak (Alice's secret key)
Ak = (Xb ** private_key_A) % p
# Calculate Bk (Bob's secret key)
Bk = (Xa ** private_key_B) % p

print("Xa (Alice's public key):", Xa)
print("Xb (Bob's public key):", Xb)
print("Ak (Alice's secret key):", Ak)
print("Bk (Bob's secret key):", Bk)