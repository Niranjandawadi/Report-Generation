from django.db import models

class datas(models.Model):

	distance_from_river = models.DecimalField(max_digits=20, decimal_places=4)
	road_access = models.CharField(max_length=100)
	distance_from_main_city = models.DecimalField(max_digits=20, decimal_places=4)
	slope = models.CharField(max_length=100)
	direct_distance_from_forest = models.DecimalField(max_digits=20, decimal_places=4)
	high_voltage_transmisison_line = models.CharField(max_length=100)
	flood_risk_level = models.DecimalField(max_digits=20, decimal_places=4)
	land_slide_risk = models.DecimalField(max_digits=20, decimal_places=4)
	elevation = models.DecimalField(max_digits=20, decimal_places=4)
	land_type = models.CharField(max_length=100)
	land_use = models.CharField(max_length=100)