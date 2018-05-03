# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class sensor(models.Model):
	sensor_value = models.CharField(max_length=250)
	sensor_position_x = models.CharField(max_length=250)
	sensor_position_y = models.CharField(max_length=250)