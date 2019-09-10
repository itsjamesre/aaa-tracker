from django.db import models

# Create your models here.

class Category(models.Model):
	full_name = models.CharField(max_length=200)
	short_code = models.CharField(max_length=200)

	class Meta:
		abstract = True


class Club(Category):
	def __str__(self):
		return self.full_name


class Specialist(Category):
	def __str__(self):
		return self.full_name


class BusinessLine(Category):
	def __str__(self):
		return self.full_name


class TestType(Category):
	def __str__(self):
		return self.full_name


class Component(Category):
	def __str__(self):
		return self.full_name


class Variable(Category):
	def __str__(self):
		return self.full_name


class Winner(Category):
	def __str__(self):
		return self.full_name


class Status(Category):
	def __str__(self):
		return self.full_name


class Test(models.Model):
	specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, null=True)
	business_line = models.ForeignKey(BusinessLine, on_delete=models.CASCADE, null=True)
	club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
	test_type = models.ForeignKey(TestType, on_delete=models.CASCADE, null=True)
	component = models.ForeignKey(Component, on_delete=models.CASCADE, null=True)
	variable = models.ForeignKey(Variable, on_delete=models.CASCADE, null=True)
	winner = models.ForeignKey(Winner, on_delete=models.CASCADE, null=True)
	status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
	code = models.CharField(max_length=200)
	product = models.CharField(max_length=200)
	
	def __str__(self):
		return self.code