class RefreshTokenNotExpired(Exception):
  def __str__(self):
    return """Refresh Token is still valid. 
              System will maintain previous Refresh Token."""


class TokenNotFound(Exception):
  def __str__(self):
    return "Could not find 'refresh_token'."


class RefreshTokenExpired(Exception):
  def __str__(self):
    return "Refresh Token expired. Required to issue new Token."