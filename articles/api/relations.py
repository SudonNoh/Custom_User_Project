from rest_framework import serializers

from articles.models import Tag


class TagRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return Tag.objects.all()
    
    def to_internal_value(self, data):
        # get_or_create : 구하고자 하는 객체가 존재할 경우 객체를 불러오고, 
        #                 존재하지 않을 경우 생성하는 method
        #                 반환은 (object, created)로 튜플 형식으로 반환한다.
        #                 object 부분은 구하고자 하는 객체 부분이고,
        #                 created 부분은 인스턴스가 get_or_create에 의해 생성되면 True
        #                 그렇지 않고 기존 DB에서 불러왔으면 False를 반환한다
        tag, created = Tag.objects.get_or_create(tag=data, slug=data.lower())
        
        return tag
    
    def to_representation(self, value):
        return value.tag