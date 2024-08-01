#Tem como objetivo retirar o préfixo 'Bearer' que ia escrito antes de colar o token gerado.

from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    def get_header(self, request):
        """
        Extracts the token from the 'Authorization' header without any prefix.
        """
        header = request.headers.get('Authorization')
        if header is None:
            return None

        # Return the header directly without prefix
        return header

    def get_raw_token(self, header):
        """
        Validates the raw token provided.
        """
        return header
