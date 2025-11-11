from flask import request
from corbado_python_sdk.generated.models import IdentifierList
from corbado_python_sdk import Config, CorbadoSDK, UserEntity

sdk: CorbadoSDK | None = None  # Global SDK instance

def init_corbado_sdk(app):
    """
    Initializes the Corbado SDK with the Flask app's configuration.
    """
    global sdk
    config = Config(
        project_id=app.config['CORBADO_PROJECT_ID'],
        api_secret=app.config['CORBADO_API_SECRET'],
        frontend_api=app.config['CORBADO_FRONTEND_API'],
        backend_api=app.config['CORBADO_BACKEND_API']
    )
    sdk = CorbadoSDK(config=config)

def get_authenticated_user_from_cookie() -> UserEntity | None:
    session_token = request.cookies.get('cbo_session_token')
    if not session_token:
        return None
    try:
        return sdk.sessions.validate_token(session_token)
    except:
        # use more sophisticated error handling in production
        return None


def get_authenticated_user_from_authorization_header() -> UserEntity | None:
    session_token = request.headers.get('Authorization')
    if not session_token:
        return None
    session_token = session_token.removeprefix("Bearer ")
    try:
        return sdk.sessions.validate_token(session_token)
    except:
        # use more sophisticated error handling in production
        return None



def get_user_identifiers(user_id: str) -> IdentifierList:
    return sdk.identifiers.list_identifiers(user_id=user_id)
