class RefreshTokenNotExpired(Exception):
  def __str__(self):
    return """Refresh Token is still valid. 
              System will maintain existed Refresh Token."""


class RefreshTokenNotFound(Exception):
  def __str__(self):
    return "Could not find 'refresh_token'."


class AccessTokenNotFound(Exception):
  def __str__(self):
    return "Could not find 'access_token'."


class RefreshTokenExpired(Exception):
  def __str__(self):
    return "Refresh Token expired. Need to issue new Token."