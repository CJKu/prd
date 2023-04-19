from django.contrib.auth.models import User
from rest_framework import serializers

from .models import PublicCardInfo, LinkModel, EmailModel, PhoneModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class OrderCardSz(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    card = serializers.PrimaryKeyRelatedField(queryset=PublicCardInfo.objects.all(), read_only=False, required=False)
    order = serializers.IntegerField(required=False)


class LinkModelSz(OrderCardSz):
    class Meta:
        model = LinkModel
        fields = "__all__"


class PhoneModelSz(OrderCardSz):
    class Meta:
        model = PhoneModel
        fields = "__all__"


class EmailModelSz(OrderCardSz):
    class Meta:
        model = EmailModel
        fields = "__all__"


def update_ordered_list(instance, model_class, data_list):
    object_list = model_class.objects.filter(card_id=instance.id)
    ids = set([data["id"] for data in data_list if data.get("id") is not None])
    for obj in [obj for obj in object_list if obj.id not in ids]:
        obj.delete()

    for order, data in enumerate(data_list):
        data_id = data.get("id")
        if data_id:
            model_class.objects.filter(id=data_id).update(**{**data, "order": order})
        else:
            obj = model_class.objects.create(**{**data, "order": order, "card": instance})
            obj.save()


class PublicCardInfoSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), read_only=False)
    links = LinkModelSz(many=True, required=False)
    phones = PhoneModelSz(many=True, required=False)
    emails = EmailModelSz(many=True, required=False)

    class Meta:
        model = PublicCardInfo
        fields = ["id", "url", "name", "creator", "links", "phones", "emails"]

    def create(self, validated_data):
        links = validated_data.pop("links", None)
        phones = validated_data.pop('phones', None)
        emails = validated_data.pop('emails', None)
        instance = PublicCardInfo.objects.create(**validated_data)

        if links is not None:
            update_ordered_list(instance, LinkModel, links)
        if phones is not None:
            update_ordered_list(instance, PhoneModel, phones)
        if emails is not None:
            update_ordered_list(instance, EmailModel, emails)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        links = validated_data.pop("links", None)
        if links is not None:
            update_ordered_list(instance, LinkModel, links)
        phones = validated_data.pop('phones', None)
        if phones is not None:
            update_ordered_list(instance, PhoneModel, phones)
        emails = validated_data.pop('emails', None)
        if emails is not None:
            update_ordered_list(instance, EmailModel, emails)

        instance.url = validated_data.get("url", instance.url)
        instance.name = validated_data.get("name", instance.name)
        instance.creator = validated_data.get("creator", instance.creator)

        instance.save()
        return instance
