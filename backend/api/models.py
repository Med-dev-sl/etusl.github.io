from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    # date of the event (can be set by admin when creating an event)
    event_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='events/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class AboutUniversity(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About University'
        ordering = ['-created_at']

    def __str__(self):
        return self.heading

class Faculty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Faculties'
        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    """News items that admins can create for the site homepage or highlights.

    Fields:
      - key_heading: a short label like "Key" or "Highlight"
      - heading: the main title of the news item
      - description: longer body for the news
      - date: date associated with the news (e.g., published date)
      - image: highlight image for the news item
    """
    key_heading = models.CharField(max_length=64, blank=True, help_text='Short label for the item (e.g. Key, Highlight)')
    heading = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='news/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.heading


class StrategicPlan(models.Model):
    """A Strategic Plan entity that can have multiple sections with images.
    Admins can create a plan with a title, summary, main image, and add ordered sections.
    """
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='strategic_plans/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Strategic Plan'
        verbose_name_plural = 'Strategic Plans'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class StrategicPlanSection(models.Model):
    plan = models.ForeignKey(StrategicPlan, related_name='sections', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='strategic_plans/sections/%Y/%m/%d/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Strategic Plan Section'
        verbose_name_plural = 'Strategic Plan Sections'

    def __str__(self):
        return f"{self.plan.title} — {self.heading}"