from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils.text import slugify
from django.db.models.signals import post_save
#####external pakage #####
from django_countries.fields import CountryField

class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=_("user"),on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)
    image=models.ImageField(_("IMAGE"),upload_to='profile_img',blank=True,null=True)
    country = CountryField()
    address = models.CharField(max_length=100,blank=True,null=True)
    join_date = models.DateTimeField(_("join date"),default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return '%s' %(self.user)

    def get_absolute_url(self):
        return reverse("accounts:Profile_detail", kwargs={"slug": self.slug})

#def create_profile(sender, **kwargs):
 #   if kwargs['created']:
  #      user_profile = Profile.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)