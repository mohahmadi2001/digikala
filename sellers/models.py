from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.

class Seller(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("slug"),unique=True,db_index=True)
    

    class Meta:
        verbose_name = _("Seller")
        verbose_name_plural = _("Sellers")

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Seller_detail", kwargs={"pk": self.pk})
    
