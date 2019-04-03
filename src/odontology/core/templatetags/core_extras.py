from django import template

register = template.Library()

@register.filter(name='get_avatar_url')
def get_avatar_url(user):
    if user.socialaccount_set.exists():
        avatar = user.socialaccount_set.first().get_avatar_url()
    else:
        avatar = None
    return avatar

@register.filter(name='get_gender')
def get_gender(user):
    if user.socialaccount_set.exists():
        gender = user.socialaccount_set.first().extra_data.get('gender')
    else:
        gender = None
    return gender
