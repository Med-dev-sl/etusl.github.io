from django.db import models
from .policy_model import PolicyDocument


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
    SECTION_TYPE_CHOICES = (
        ('overview', 'Overview'),
        ('vision_commitment', 'Vision & Strategic Commitments'),
        ('objectives', 'Strategic Plan Objectives'),
        ('goals', 'Goals'),
    )
    
    plan = models.ForeignKey(StrategicPlan, related_name='sections', on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255, blank=True, help_text='Optional subtitle or description')
    section_type = models.CharField(max_length=50, choices=SECTION_TYPE_CHOICES, default='overview')
    content = models.TextField(blank=True, help_text='Rich text content for the section')
    # JSON field to store list items (e.g., goals, commitments, objectives)
    items = models.JSONField(blank=True, null=True, help_text='List of items as JSON array of objects with title/description')
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


class AboutHistory(models.Model):
    """Stores university history content with featured image and text."""
    title = models.CharField(max_length=255, default='History')
    subtitle = models.CharField(max_length=255, blank=True, help_text='Introductory text (e.g., university name in uppercase)')
    image = models.ImageField(upload_to='about/history/%Y/%m/%d/', blank=True, null=True, help_text='Featured image for the history section')
    content = models.TextField(help_text='Main history text content (HTML supported)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About History'
        verbose_name_plural = 'About History'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class HistoryEvent(models.Model):
    """Key milestone events in university history."""
    history = models.ForeignKey(AboutHistory, related_name='events', on_delete=models.CASCADE)
    year = models.CharField(max_length=50, help_text='Year or date range (e.g., "1948" or "1948-1950")')
    title = models.CharField(max_length=255, help_text='Event title')
    name = models.CharField(max_length=255, blank=True, help_text='Alternative field for event name')
    description = models.TextField(blank=True, help_text='Event description')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-year']
        verbose_name = 'History Event'
        verbose_name_plural = 'History Events'

    def __str__(self):
        return f"{self.year} — {self.title}"


class HistoryImage(models.Model):
    """Historical images for the "Through the Years" gallery."""
    history = models.ForeignKey(AboutHistory, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about/history/images/%Y/%m/%d/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, help_text='Image caption or description')
    year = models.CharField(max_length=50, blank=True, help_text='Year associated with the image')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'History Image'
        verbose_name_plural = 'History Images'

    def __str__(self):
        return self.caption or (self.image.name if self.image else 'History Image')


class VisionMission(models.Model):
    """Vision and Mission statements with optional featured images."""
    vision_title = models.CharField(max_length=255, default='Our Vision')
    vision_text = models.TextField(help_text='Vision statement content')
    mission_title = models.CharField(max_length=255, default='Our Mission')
    mission_text = models.TextField(help_text='Mission statement content')
    featured_image = models.ImageField(upload_to='about/vision_mission/%Y/%m/%d/', blank=True, null=True)
    image_alt = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vision and Mission'
        verbose_name_plural = 'Vision and Mission'
        ordering = ['-created_at']

    def __str__(self):
        return 'Vision & Mission'


class CoreValue(models.Model):
    """Core values of the university."""
    title = models.CharField(max_length=255, help_text='Value name (e.g., Integrity, Commitment)')
    description = models.TextField(help_text='Description of the core value')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Core Value'
        verbose_name_plural = 'Core Values'
        ordering = ['order']

    def __str__(self):
        return self.title


class StrategicPriority(models.Model):
    """Strategic priorities or focus areas of the university."""
    title = models.CharField(max_length=255, default='Our Strategic Priorities')
    featured_image = models.ImageField(upload_to='about/strategic/%Y/%m/%d/', blank=True, null=True)
    image_alt = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Strategic Priority'
        verbose_name_plural = 'Strategic Priorities'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PriorityItem(models.Model):
    """Individual priority item within a strategic priority."""
    priority = models.ForeignKey(StrategicPriority, related_name='items', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, help_text='Priority item text')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Priority Item'
        verbose_name_plural = 'Priority Items'

    def __str__(self):
        return self.text


class Affiliate(models.Model):
    """Institutes/colleges affiliated to the university."""
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=512, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True, null=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=512, blank=True)
    featured_image = models.ImageField(upload_to='affiliates/%Y/%m/%d/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Affiliate'
        verbose_name_plural = 'Affiliates'

    def __str__(self):
        return self.name


class LeaderPosition(models.Model):
    """Position/Title hierarchy for leaders."""
    HIERARCHY_CHOICES = [
        (1, 'Top Level - Chancellor/Vice-Chancellor'),
        (2, 'Senior - Pro-Vice-Chancellor/Registrar'),
        (3, 'Director/Department Head'),
    ]
    
    title = models.CharField(max_length=255, help_text='Position title (e.g., Chancellor)')
    hierarchy_level = models.IntegerField(choices=HIERARCHY_CHOICES, default=1)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['hierarchy_level', 'order']
        verbose_name = 'Leader Position'
        verbose_name_plural = 'Leader Positions'

    def __str__(self):
        return f"{self.title} (Level {self.hierarchy_level})"


class Leader(models.Model):
    """University leadership team members."""
    from django.contrib.auth.models import User
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leader_profile', null=True, blank=True)
    position = models.ForeignKey(LeaderPosition, on_delete=models.PROTECT, related_name='leaders')
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='leaders/%Y/%m/%d/', help_text='Professional headshot')
    bio = models.TextField(blank=True, help_text='Short biography')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0, help_text='Display order within position level')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['position__hierarchy_level', 'order', 'name']
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'

    def __str__(self):
        return f"{self.name} - {self.position.title}"


class AcademicStatistic(models.Model):
    """Statistics for the academics overview page."""
    STATISTIC_TYPES = [
        ('courses', 'Courses Offered'),
        ('undergrad', 'Undergraduate Programmes'),
        ('graduate', 'Graduate Programmes'),
        ('faculty', 'Faculty Members'),
        ('students', 'Students'),
    ]
    
    statistic_type = models.CharField(max_length=20, choices=STATISTIC_TYPES, unique=True)
    value = models.CharField(max_length=50)  # e.g., "2000+"
    label = models.CharField(max_length=255)  # e.g., "Courses offered"
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Academic Statistic'
        verbose_name_plural = 'Academic Statistics'

    def __str__(self):
        return f"{self.label} - {self.value}"


class AdmissionType(models.Model):
    """Different types of admissions (Undergraduate, Graduate, Post-first degree)."""
    ADMISSION_CATEGORIES = [
        ('undergraduate', 'Undergraduate Admissions'),
        ('graduate', 'Graduate Admissions'),
        ('postfirst', 'Post-first degree Admissions'),
    ]
    
    category = models.CharField(max_length=20, choices=ADMISSION_CATEGORIES, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='admissions/%Y/%m/%d/', blank=True, null=True)
    link_url = models.URLField(blank=True, help_text='External link for the admission type')
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Admission Type'
        verbose_name_plural = 'Admission Types'

    def __str__(self):
        return self.title


class AcademicPage(models.Model):
    """Main content for the academics overview page."""
    page_title = models.CharField(max_length=255, default='Academics')
    hero_subtitle = models.CharField(max_length=500, default='Academic work is one of the most crucial aspects of the university experience and, therefore, requires discipline and commitment.')
    overview_title = models.CharField(max_length=255, default='Academic Excellence')
    overview_description = models.TextField(default='ETU offers a comprehensive range of academic programs across multiple faculties and disciplines.')
    nurture_title = models.CharField(max_length=255, default='Nurturing Success')
    nurture_description = models.TextField(default='Our serene atmosphere fosters academic excellence, empowering individuals to thrive in their diverse educational pursuits')
    study_with_us_link = models.URLField(blank=True, help_text='Link to "Study with us" section')
    student_handbook_link = models.URLField(blank=True, help_text='Link to student handbook')
    academic_calendar_link = models.URLField(blank=True, help_text='Link to academic calendar')
    academic_calendar_title = models.CharField(max_length=255, default='Academic Calendar')
    academic_calendar_description = models.TextField(default='See the academic calendar for various schedules and activities for the current academic year')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Academic Page'
        verbose_name_plural = 'Academic Pages'

    def __str__(self):
        return self.page_title