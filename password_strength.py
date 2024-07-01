import re
from passlib.context import CryptContext
from owasp_password_strength import password_strength

# Configure bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_password_strength(password):
    # Length check
    length = len(password)
    
    # Check for numbers, special characters, uppercase and lowercase
    has_number = re.search(r"\d", password)
    has_special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    
    # OWASP password strength test
    owasp_strength = password_strength(password)
    
    # Password strength criteria
    strength = {
        'length': length,
        'has_number': bool(has_number),
        'has_special_char': bool(has_special_char),
        'has_upper': bool(has_upper),
        'has_lower': bool(has_lower),
        'owasp_strength': owasp_strength
    }
    
    return strength

def hash_password(password):
    return pwd_context.hash(password)
