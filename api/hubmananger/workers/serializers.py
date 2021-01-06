from api.serializers import serializers 
from users.models import Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields=['id','first_name','last_name','email','password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user 