class RefreshTokenNotExpired(Exception):
  def __str__(self):
    return """Refresh Token is still valid. 
              System will maintain previous Refresh Token."""


class TokenNotFound(Exception):
  def __str__(self):
    return "By Occuring Error, token has not been issued."


class RefreshTokenExpired(Exception):
  def __str__(self):
    return "Refresh Token expired. Required to issue new Token."