from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    active = models.BooleanField(default=True)
    # mark announcement to appear as a featured link in the sidebar
    is_featured = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
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


class FooterSection(models.Model):
    """Represents a column/section in the footer (e.g., Colleges, Quick-Links, Admissions, Alumni)."""
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Footer Section'
        verbose_name_plural = 'Footer Sections'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    """A link within a footer section."""
    section = models.ForeignKey(FooterSection, related_name='links', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    # optional slug for internal pages (e.g. 'engineering-innovation')
    slug = models.SlugField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Footer Link'
        verbose_name_plural = 'Footer Links'

    def __str__(self):
        return f"{self.section.title} — {self.label}"

    def get_target(self):
        """Return the preferred target URL for the link: slug => '/{slug}', else url."""
        if self.slug:
            # use root-level slug path for internal pages
            return f"/{self.slug.strip('/') }"
        return self.url or '#'


class AboutSection(models.Model):
    """A logical section on the About pages (e.g. Overview, History, Mission)."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'About Section'
        verbose_name_plural = 'About Sections'

    def __str__(self):
        return self.title


class AboutOverview(models.Model):
    """The editable overview content for the About page.

    Admins can provide a short/brief description, additional rich content,
    and attach images, campus entries and statistic entries.
    """
    section = models.OneToOneField(AboutSection, related_name='overview', on_delete=models.CASCADE)
    brief = models.TextField(blank=True, help_text='Short brief about the university')
    content = models.TextField(blank=True, help_text='Longer content or rich text (HTML allowed)')
    # JSON field to store key/value statistics (e.g. {"students": 1200, "staff": 150})
    statistics = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About Overview'
        verbose_name_plural = 'About Overviews'

    def __str__(self):
        return f"Overview — {self.section.title}"


class AboutImage(models.Model):
    about = models.ForeignKey(AboutOverview, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about/images/%Y/%m/%d/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'About Image'
        verbose_name_plural = 'About Images'

    def __str__(self):
        return self.caption or (self.image.name if self.image else 'About Image')


class Campus(models.Model):
    about = models.ForeignKey(AboutOverview, related_name='campuses', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='about/campuses/%Y/%m/%d/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Campus'
        verbose_name_plural = 'Campuses'

    def __str__(self):
        return self.name


class Statistic(models.Model):
    about = models.ForeignKey(AboutOverview, related_name='stat_items', on_delete=models.CASCADE)
    label = models.CharField(max_length=120)
    value = models.CharField(max_length=120)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'About Statistic'
        verbose_name_plural = 'About Statistics'

    def __str__(self):
        return f"{self.label}: {self.value}"