from django.db import models

# Create your models here.
LANGUAGE_CHOICES = (
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('java', 'Java'),
    ('ruby', 'Ruby'),
    # Add more languages as needed
)

STYLE_CHOICES = (
    ('friendly', 'Friendly'),
    ('bw', 'Black and White'),
    ('colorful', 'Colorful'),
    # Add more styles as needed
)


class Snippet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)