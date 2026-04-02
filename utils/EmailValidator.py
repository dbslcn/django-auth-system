# utils/validators.py
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import logging
import sys

# CONFIGURAÇÃO DE LOG: Isso aqui faz o terminal "escutar" o logger
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    stream=sys.stdout
)

logger = logging.getLogger(__name__)

class EmailValidator:
    @staticmethod
    def is_valid(email: str) -> bool:
        """Validação técnica com log imediato."""
        try:
            validate_email(email)
            logger.info(f"Valid email: {email}")
            return True
        except (ValidationError, TypeError):
            logger.error(f"Invalid email: {email}")
            return False

if __name__ == "__main__":
    # Agora isso vai printar no seu terminal!
    EmailValidator.is_valid("test@example.com")
    EmailValidator.is_valid("email-errado.com")