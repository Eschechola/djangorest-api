import uuid

from django.db import models


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    publishedAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        #order desc
        ordering = [ '-publishedAt' ]

    def __str__(self):
        return self.title


class Average(Base):
    courseId = models.ForeignKey(Course, related_name='averages', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rate = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Average'
        verbose_name_plural = 'Averages'
        unique_together = ['email', 'courseId']

    def __str__(self):
        return f'{self.name} average course {self.courseId} with {self.rate}'

