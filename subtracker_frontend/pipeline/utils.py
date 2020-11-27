from django.conf import settings

USER_FIELDS = ['username','email','first_name','last_name']
def load_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}
    fields = get_user_prop(details,backend,args,kwargs)
    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }   
def social_details(backend, details, response, *args, **kwargs):
    return {'details': dict(email=response["emails"][0],first_name=response["given_name"],last_name=response["family_name"],name=response["given_name"] + " " + response["family_name"],username=response["emails"][0])}


def load_uid(backend, details, response, *args, **kwargs):
    user_id_attr = getattr(settings, "SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_ID_KEY", 'userId')
    user_id = response.get(user_id_attr)
    return {'uid': user_id}

def load_username(strategy, details, backend, user=None, *args, **kwargs):
    print(details['username'])
    return {'username': details['username']}

def get_user_prop(details,backend,*args, **kwargs):
    props = dict()
    for prop_name in backend.setting('USER_FIELDS', USER_FIELDS):
        prop_value = kwargs.get(prop_name, details.get(prop_name))
        if isinstance(prop_value,list):
            props[prop_name] = prop_value[0]
        else:
            props[prop_name] = prop_value
    return props
