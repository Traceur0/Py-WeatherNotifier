class RefreshTokenExpired(Exception):
    """
    리프레시 토큰이 만료되었습니다
    """

    def __str__(self):
        return "Refresh Token expired. Required to issue new Token."


class RefreshTokenStillValid(Exception):
    """
    리프레시 토큰이 아직 유효하므로 현재 토큰값을 유지합니다
    """

    def __str__(self):
        return """Refresh Token is still valid. 
              System will maintain previous Refresh Token."""


class TokenNotFound(Exception):
    """
    토큰을 찾을 수 없습니다. 에러로 인해 토큰은 발급되지 않습니다
    """

    def __str__(self):
        return "By Occuring Error, token has not been issued."
