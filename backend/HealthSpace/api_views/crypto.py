import bcrypt

def create(password):
    
    password = bytes(password, "utf-8")
    salt = bcrypt.gensalt(rounds=9)
    hashed = bcrypt.hashpw(password, salt)
    hashed = hashed.decode('utf-8')
    
    return hashed


def compare_password(password,hash):
    
    hash = bytes(hash, "utf-8")
    password = bytes(password, "utf-8")

    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False