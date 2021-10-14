from rest_framework import serializers
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # The Serializer class is itself a type of Field, and can be used to
    # represent relationships where one object type is nested inside another.
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        # Profile 에서 우리가 원하는 field 들만 json 형태로 만듦
        # 아래의 예시에서는 username, bio, image를 json 형태로 변환
        fields = ('username', 'bio', 'image', )
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image
        return 'https://static.productionready.io/images/smiley-cyrus.jpg'