from django.db import models

from django.utils import timezone
from taggit.managers import TaggableManager


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class USER
# usage_account


class PublicCardInfo(models.Model):
    url = models.URLField(max_length=200)
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.url


class PrivateCardInfo(models.Model):
    url = models.URLField(max_length=200)
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tags = TaggableManager()

    # group = models.CharField(max_length=250) # second tier
    # status = models.CharField(max_length=250) # second tier
    # usage_count? 這個是user 的data or card的data
    # discuss tag normalize/ UI 的形式
    # 公有惟讀tag 私有可編輯tag

    def __str__(self):
        return self.url


class PhoneModel(models.Model):
    phone = models.CharField(max_length=250)
    card_id = models.ForeignKey(PublicCardInfo, related_name="phones", on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()


class EmailModel(models.Model):
    email = models.EmailField(max_length=250)
    card = models.ForeignKey(PublicCardInfo, related_name="emails", on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()


class LinkModel(models.Model):
    url = models.URLField(max_length=200)
    card = models.ForeignKey(PublicCardInfo, related_name="links", on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"id={self.id} url={self.url}. card={self.card}"


class MemoModel(models.Model):
    memo = models.CharField(max_length=250)  # frontend use rich-text editor
    card = models.ForeignKey(PrivateCardInfo, on_delete=models.CASCADE)
    update_timestamp = models.DateTimeField(auto_now_add=True)
    order = models.PositiveSmallIntegerField()
