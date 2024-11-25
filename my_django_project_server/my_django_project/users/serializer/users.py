from rest_framework import serializers
from users.models.user import CustomUser
# from posts.serializer.posts import PostSerializer




class CustomUserSerializer(serializers.ModelSerializer):
    # post = PostSerializer() 
    # order = OrderSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email' ,'active', 'phone_num', '']