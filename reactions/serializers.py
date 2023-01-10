from rest_framework import serializers
from reactions.models import User, Account, Stori, Stori_reaction, Comment_reaction, Stori_category,Stori_comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, required=False)
    class Meta:
        model = Account
        fields = '__all__'

class StoriCategoySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stori_category
        fields = '__all__'

class StoriSerializer(serializers.ModelSerializer):
    category = StoriCategoySerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Stori
        fields = '__all__'

class StoriReactionSerializer(serializers.ModelSerializer):
    stori = StoriSerializer(read_only=False, required=True)
    class Meta:
        model = Stori_reaction
        fields = '__all__'

class StoriCommentSerializer(serializers.ModelSerializer):
    stori = StoriSerializer(read_only=False, required=True)
    class Meta:
        model = Stori_comment
        fields = '__all__'

class CommentReactionSerializer(serializers.ModelSerializer):
    comment = StoriSerializer(read_only=False, required=True)
    class Meta:
        model = Comment_reaction
        fields = '__all__'
