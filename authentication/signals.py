from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile

from .models import User

# 앞서 profile 모델에서 'User' 모델과 'Profile' 모델 사이를 One-to-One 관계로
# 정의했다. 장고에서 우리가 'User'를 만들 떄 'Profile'도 자동으로 만들어지면
# 좋겠지만 안타깝게도 One-to-One 관계로 묶는 것 만으로는 자동으로 하기는 어렵다.
# 자동으로 실행하기 위해서는 Django의 Signals framework를 사용해야 한다.
# 우리는 'User' instance가 만들어진 뒤 'Profile' instance를 만들기 위해 
# 'post_save'를 사용한다.

@receiver(post_save, sender=User)
def create_related_profile(sender, instance, created, *args, **kwargs):
    # Notice that we're checking for 'created' here. We only want to do this
    # the first time the 'User' instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)