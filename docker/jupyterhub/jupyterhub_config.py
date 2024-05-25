import os
import json
import urllib.parse
import hashlib
import base64

from oauthenticator.oauth2 import OAuthenticator
from tornado import httpclient
from tornado.log import app_log

class WorldIDOAuthenticator(OAuthenticator):
    login_service = "World ID"
    authorize_url = "https://id.worldcoin.org/authorize"
    token_url = "https://id.worldcoin.org/token"
    userdata_url = "https://id.worldcoin.org/userinfo"
    introspect_url = "https://id.worldcoin.org/introspect"  # Assuming there is an introspection endpoint
    scope = ['openid', 'profile', 'email']
    username_map = {}

    async def authenticate(self, handler, data=None):
        code = handler.get_argument("code")
        state = handler.get_argument("state", "")
        app_log.debug(f"Received OAuth callback with code={code} and state={state}")

        http_client = httpclient.AsyncHTTPClient()
        body = urllib.parse.urlencode({
            "redirect_uri": self.get_callback_url(handler),
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "scope": " ".join(self.scope)
        })
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        app_log.debug(f"Requesting access token with body: {body}")

        try:
            response = await http_client.fetch(self.token_url, method="POST", headers=headers, body=body, request_timeout=120.0)
            access_token = json.loads(response.body).get('access_token', None)
            app_log.debug(f"Received access token: {access_token}")

            if not access_token:
                app_log.error("Failed to retrieve access token")
                return None

            # Validate the access token
            # validation_result = await self.validate_access_token(http_client, access_token)
            # if not validation_result:
            #     app_log.error("Invalid access token")
            #     return None

            # Fetch user information with the validated access token
            req = httpclient.HTTPRequest(self.userdata_url, method="GET", headers={"Authorization": f"Bearer {access_token}"})
            user_response = await http_client.fetch(req)
            user_data = json.loads(user_response.body)
            app_log.debug(f"Received user data: {user_data}")

            # Hash the 'sub' field using SHA-256 and then base64 encode it
            sub = user_data.get('sub')
            hashed_sub = hashlib.sha256(sub.encode('utf-8')).digest()
            base64_hashed_sub = base64.urlsafe_b64encode(hashed_sub).decode('utf-8')

            # Return a more comprehensive user dictionary
            user_info = {
                'name': base64_hashed_sub,
                'email': user_data.get('email'),
                'fullname': user_data.get('name'),
                'profile': user_data.get('profile'),
                'scope': self.scope
            }
            app_log.debug(f"user info: {user_info}")
            return user_info

        except httpclient.HTTPError as e:
            app_log.error(f"HTTPError fetching access token: {str(e)}")
        except Exception as e:
            app_log.error(f"Error during OAuth authentication: {str(e)}")

        return None

    async def validate_access_token(self, http_client, access_token):
        """
        Validates the access token using the introspection endpoint.
        """
        try:
            body = urllib.parse.urlencode({
                "token": access_token,
                "client_id": self.client_id,
                "client_secret": self.client_secret
            })
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            app_log.debug(f"Validating access token with body: {body}")

            response = await http_client.fetch(self.introspect_url, method="POST", headers=headers, body=body)
            introspection_result = json.loads(response.body)
            app_log.debug(f"Introspection result: {introspection_result}")

            # Return the "active" status of the token
            return introspection_result.get("active", False)
        except httpclient.HTTPError as e:
            app_log.error(f"HTTPError during token introspection: {str(e)}")
        except Exception as e:
            app_log.error(f"Error during token introspection: {str(e)}")

        return False

c.JupyterHub.authenticator_class = WorldIDOAuthenticator
c.WorldIDOAuthenticator.client_id = os.environ.get('OAUTH_CLIENT_ID')
c.WorldIDOAuthenticator.client_secret = os.environ.get('OAUTH_CLIENT_SECRET')
c.WorldIDOAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL', 'http://localhost:8000/hub/oauth_callback')
c.WorldIDOAuthenticator.admin_users = { os.environ.get('JUPITER_ADMIN') } 
c.WorldIDOAuthenticator.allow_all = True

c.JupyterHub.debug_proxy = False
c.JupyterHub.log_level = os.environ.get('JUPITER_LOGLEVEL')
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = 'jupyterhub'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.network_name = os.environ.get('JUPITER_NETWORK')
c.DockerSpawner.image = os.environ.get('JUPITER_SPAWNIMAGE')
c.DockerSpawner.http_timeout = 60