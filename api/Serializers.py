from rest_framework import serializers
from bookapi.models import bookmodel, Reviewmodel

class boolserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = bookmodel
        fields = '__all__'
        # extra_kwargs = {'user':{'write_only':True}}
        
        
    # def validate(self, data):
    #     bookdata = bookmodel.objects.filter(title =data['title']).exists()
    #     if(bookdata):
    #        raise serializers.ValidationError({'title':'this book is already added'})
    #     return data
