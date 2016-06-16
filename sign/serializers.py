from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Sign


class SignSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sign
		fields = ('id', 'text', 'author', 'created', 'expires', 'location')

	def to_representation(self, instance):
		data = super(SignSerializer, self).to_representation(instance)
		data.update({'author': instance.author.username})
		return data


class SignCreateSerializer(serializers.ModelSerializer):
	author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

	class Meta:
		model = Sign
		fields = ('text', 'expires', 'location', 'author')

	def to_representation(self, instance):
		data = super(SignCreateSerializer, self).to_representation(instance)
		data.update({'author': instance.author.username})
		return data
