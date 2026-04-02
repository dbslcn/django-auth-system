from utils.SupabaseClient import SupabaseClient

from utils.security import PasswordHasher

from utils.EmailValidator import EmailValidator

if __name__ == "__main__":
    
    hash = PasswordHasher.hash_password("12345678")
    #PasswordHasher.verify_password("12345678", hash)
    email = "test@example.com"
    if email:
        EmailValidator.is_valid(email)
    #EmailValidator.is_valid("email-errado.com")

        client = SupabaseClient()

        client.insert("profiles", {"username": email, "password_hash":hash})
    else:
        print("Email inválido")