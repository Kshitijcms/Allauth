from django.conf import settings
from django.db import models


class LoginHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="login_history",
    )
    login_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
    )
    user_agent = models.TextField(blank=True)

    class Meta:
        ordering = ["-login_time"]
        verbose_name = "Login History"
        verbose_name_plural = "Login Histories"

    def __str__(self):
        return f"{self.user} - {self.login_time}"
