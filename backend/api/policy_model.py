from django.db import models


class PolicyDocument(models.Model):
    """Policy document (PDF/DOCX) available for download."""
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=512, blank=True)
    file = models.FileField(upload_to='policies/%Y/%m/%d/')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Policy Document'
        verbose_name_plural = 'Policy Documents'

    def __str__(self):
        return self.title
