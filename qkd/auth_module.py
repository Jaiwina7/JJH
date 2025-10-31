
import hashlib
import uuid
import logging

logging.basicConfig(filename='auth.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Sample user database (username: hashed_password)
users = {"alice": hashlib.sha256("password123".encode()).hexdigest(),
         "bob": hashlib.sha256("securepass".encode()).hexdigest()}

# Active session tokens
active_tokens = {}

def authenticate(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if username in users and hashed == users[username]:
        # Generate token
        token = str(uuid.uuid4())
        active_tokens[username] = token
        logging.info(f"{username} authenticated successfully. Token: {token}")
        print(f"{username} authenticated successfully. Token issued.")
        return token
    else:
        logging.warning(f"Failed authentication attempt for user: {username}")
        print("Authentication failed.")
        return None

def verify_token(username, token):
    return active_tokens.get(username) == token

# Example usage jaiwin thaa poole
if __name__ == "__main__":
    token = authenticate("alice", "password123")
    if token and verify_token("alice", token):
        print("Token verified. Ready for QKD session.")
        