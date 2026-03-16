from django.db import models
import uuid

class TravelProjects(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=64)
    description=models.TextField(blank=True, null=True)
    start_date=models.DateField(blank=True, null=True)
    completed=models.BooleanField(default=False)
    created_at=models.DateField(blank=True, auto_now_add=True)

    class Meta:
        verbose_name="Travel Project"
        verbose_name_plural="Travel Projects"

    def __str__(self):
        return f"{self.name}"

class ProjectPlace(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project=models.ForeignKey(TravelProjects, on_delete=models.CASCADE, related_name="place")
    external_id=models.CharField(max_length=255)
    notes=models.TextField(blank=True, null=True)
    visited=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Place"
        verbose_name_plural="Places"

    def __str__(self):
        return f"{self.project}-{self.external_id}"

