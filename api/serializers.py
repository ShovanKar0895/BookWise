from rest_framework import serializers
from api.models import BookModel
from datetime import datetime

class BookModelerializer(serializers.ModelSerializer):

    published_date = serializers.SerializerMethodField()
    added_date = serializers.SerializerMethodField()
    last_updated_date = serializers.SerializerMethodField()

    class Meta:
        model = BookModel
        
        fields = ['_id', 'title', 'author','isbn','published_date','genre','description','copies_available','total_copies','publisher','language','keywords','shelf_location','added_date','last_updated_date','status']

    def get_published_date(self, obj):
        return self.convert_timestamp_to_date(obj.published_date)

    def get_added_date(self, obj):
        return self.convert_timestamp_to_date(obj.added_date)

    def get_last_updated_date(self, obj):
        return self.convert_timestamp_to_date(obj.last_updated_date)

    def convert_timestamp_to_date(self, timestamp):
        if timestamp:
            return datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')
        else:
            return None
    
    def validate_isbn(self,value):
        try:
            # Check if the ISBN already exists and is not marked as deleted
            hello = BookModel.objects.filter(isbn=value).exclude(status='5')
            print(hello)
            if BookModel.objects.filter(isbn=value).exclude(status='5').exists():
                raise serializers.ValidationError("ISBN must be unique among active records.")
        except Exception as e:
            print(f"Exception occurred: {e}")
            raise serializers.ValidationError("An error occurred during ISBN validation.")
        return value
    
    def validate(self,data):
        if data['copies_available']>data['total_copies']:
            raise serializers.ValidationError("Copies available cannot exceed total copies.")
        return data