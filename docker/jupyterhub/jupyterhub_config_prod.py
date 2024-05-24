import os
import json
import urllib.parse

from oauthenticator.oauth2 import OAuthenticator
from tornado import httpclient
from tornado.log import app_log

class WorldIDOAuthenticator(OAuthenticator):
    login_service = "World ID"
    authorize_url = "https://id.worldcoin.org/authorize"
    token_url = "https://id.worldcoin.org/token"
    userdata_url = "https://id.worldcoin.org/userinfo"
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

            req = httpclient.HTTPRequest(self.userdata_url, method="GET", headers={"Authorization": f"Bearer {access_token}"})
            user_response = await http_client.fetch(req)
            user_data = json.loads(user_response.body)
            app_log.debug(f"Received user data: {user_data}")
            return {'name': user_data.get('sub')}

        except httpclient.HTTPError as e:
            app_log.error(f"HTTPError fetching access token: {str(e)}")
        except Exception as e:
            app_log.error(f"Error during OAuth authentication: {str(e)}")

        return None

c.JupyterHub.authenticator_class = WorldIDOAuthenticator
c.WorldIDOAuthenticator.client_id = os.environ.get('OAUTH_CLIENT_ID')
c.WorldIDOAuthenticator.client_secret = os.environ.get('OAUTH_CLIENT_SECRET')
c.WorldIDOAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL', 'http://localhost:8000/hub/oauth_callback')
c.WorldIDOAuthenticator.admin_users = {'0x1dd9a0e2e874145ab5c4873b9285d08cb9c5fc5328aaee1dc329e2158dc68349'} # https://simulator.worldcoin.org/id/0x18310f83
c.WorldIDOAuthenticator.allow_all = True

c.JupyterHub.debug_proxy = False
c.JupyterHub.log_level = 'INFO'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_ip = 'jupyterhub'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.network_name = 'jupyter-prod'
c.DockerSpawner.image = 'blockscience:latest'
c.DockerSpawner.http_timeout = 60