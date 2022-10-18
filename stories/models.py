from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class feature(models.Model):
    feature_name = models.TextField()

    def __str__(self):
        return self.feature_name

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=12)
    contact_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)

class contact_us_detail(models.Model):
    address1 = models.TextField()
    address2 = models.TextField(default='Hoshiarpur-146001 PUNJAB')
    email = models.EmailField()
    contact_number1 = models.CharField(max_length=12)
    contact_number2 = models.CharField(max_length=12 , blank=True)

    def __str__(self):
        return self.address1

class institute_deatil(models.Model):
    main_quote_line1 = models.TextField()
    main_quote_line2 = models.TextField()
    main_thumbnail = models.ImageField(null=True)

    def __str__(self):
        return self.main_quote_line1
class add_review(models.Model):
    name = models.TextField(max_length=40, blank=True, null=True)
    message = models.TextField()
    def __str__(self):
        return self.name

class author(models.Model):
    author_name = models.TextField(max_length=40, blank=True, null=True)
    author_image = models.ImageField(null=True)
    def __str__(self):
        return self.author_name

class our_course(models.Model):
    course_name = models.TextField(max_length=40, blank=True, null=True)
    course_description = models.TextField(max_length=250, blank=True, null=True)
    course_logo = models.ImageField(null=True)
    def __str__(self):
        return self.course_name

class why_choose_learning_point(models.Model):
    line = models.TextField(max_length=40)
    def __str__(self):
        return self.line

class ourcard(models.Model):
    card_name = models.TextField(max_length=20 )
    card_description = models.TextField()
    card_icon = models.TextField()
    def __str__(self):
        return self.card_name

class StoriesView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey('Stories', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Stories(models.Model):
    student_name = models.CharField(max_length=100)
    student_overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    band_score = models.CharField(max_length=50, default='0.0')
    writing_score = models.CharField(max_length=50, default='0.0')
    reading_score = models.CharField(max_length=50, default='0.0')
    speaking_score = models.CharField(max_length=50 , default='0.0')
    listening_score = models.CharField(max_length=50,default='0.0')
    thumbnail = models.ImageField()
    previous_story = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_story = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse('story-detail', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('story-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('story-delete', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')



    # @property
    # def view_count(self):
    #     return StoriesView.objects.filter(post=self).count()
