def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

print("Diffie-Hellman Key Exchange :-\n")
sender_name = str(input("Enter sender's name: "))
receiver_name = str(input("Enter receiver's name: "))

p = int(input("\nEnter a large prime number (p): "))
if p < 2:
    raise ValueError("Prime number must be greater than 1.")

g = int(input(f"Enter a base number (generator) less than {p}: "))
if g <= 1 or g >= p:
    raise ValueError(f"Base number must be > 1 and < {p}.")
if not is_primitive_root(g, p):
    raise ValueError(f"{g} is not a valid generator (primitive root) for {p}.")

sender_private = int(input(f"Enter {sender_name}'s private key (number < p): "))
receiver_private = int(input(f"Enter {receiver_name}'s private key (number < p): "))
if not (0 < sender_private < p and 0 < receiver_private < p):
    raise ValueError(f"Private keys must be between 1 and {p - 1}.")

sender_public = mod_exp(g, sender_private, p)
receiver_public = mod_exp(g, receiver_private, p)
sender_shared_key = mod_exp(receiver_public, sender_private, p)
receiver_shared_key = mod_exp(sender_public, receiver_private, p)

print("\nResults :-")
print(sender_name + "'s Public Key:", sender_public)
print(receiver_name + "'s Public Key:", receiver_public)
print(sender_name + "'s Shared Key:", sender_shared_key)
print(receiver_name + "'s Shared Key:", receiver_shared_key)

if sender_shared_key == receiver_shared_key:
    print("\nShared key successfully established!")
else:
    print("\nError: Shared keys do not match.")
