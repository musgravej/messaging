from os import name
from django.db import models
from django.db.models import UniqueConstraint, constraints


class MessageThread(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField()
    created = models.DateTimeField()

    def __str__(self):
        return str(self.title)


class MessageSubscriber(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("archived", "Archived"),
    )

    subscriber = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    message_thread = models.ForeignKey(
        MessageThread,
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="active")
    last_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [UniqueConstraint(name="thread_subscriber", fields=["subscriber", "message_thread"])]


class MessageMessage(models.Model):
    text = models.CharField(max_length=255)
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    message_thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE)
    message_sent_dt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.text)
