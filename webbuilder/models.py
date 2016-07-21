from django.db import models

class Webbuilder_Task(models.Model):

    class Meta:
        permissions = (
            ("can_view", "Can use webbuilder"),
            ("can_edit", "Can edit source code"),
        )