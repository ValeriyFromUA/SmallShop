from django.db import models


class Items(models.Model):
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False, max_length=1000)
    image = models.ImageField(blank=False, upload_to="shop")
    price = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
