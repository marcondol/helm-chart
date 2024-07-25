import secrets

# Generate a 32-byte (256-bit) secret token
secret_token = secrets.token_hex(32)
print(secret_token)
