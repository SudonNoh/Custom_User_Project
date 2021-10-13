import json
from rest_framework.renderers import JSONRenderer


# renderer 에 대해서 더 공부할 필요가 있음
class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If we recieve a 'token' key as part of the response, it will by a
        # byte object. Byte objects don't serializer well, so we need to
        # decode it before rendering the User object.
        token = data.get('token', None)
        
        # isinstance(a, bytes) "a"가 bytes 형이면 True, 아니면 False
        if token is not None and isinstance(token, bytes):
            # Also as mentioned above, we will decode 'token' if it is type
            # bytes.
            data['token'] = token.decode('utf-8')
            
        # Finally, we can render our data under the 'user' namespace.
        return json.dumps({
            'user':data
        })