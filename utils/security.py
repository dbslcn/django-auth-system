# utils/security.py
from django.contrib.auth.hashers import make_password, check_password
import logging
import sys
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    stream=sys.stdout
)

logger = logging.getLogger(__name__)


class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Transforma senha pura em hash seguro (Argon2).
        """
        if not password or len(password) < 8:
            logger.warning("Attempt to hash a weak or empty password.")
            # Você pode decidir se quer barrar aqui ou na View
        
        hashed = make_password(password)
        logger.info("Password successfully hashed.")
        return hashed

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        Verifica se a senha digitada confere com o hash do banco.
        """
        is_valid = check_password(password, hashed_password)
        
        if is_valid:
            logger.info("Password verification: SUCCESS.")
        else:
            logger.error("Password verification: FAILED.")
            
        return is_valid

if __name__ == "__main__":
    hash=PasswordHasher.hash_password("12345678")
    print(hash)
    PasswordHasher.verify_password("12345678", "hash")
