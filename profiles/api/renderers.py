from core.renderers import CoreJSONRenderer


class ProfileJSONRenderer(CoreJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_object_count = 'profilesCount'