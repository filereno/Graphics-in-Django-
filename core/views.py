from django.shortcuts import render
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
 
class DadosJSONView(BaseLineChartView):
    
	def get_labels(self):

		labels = [
			"Janeiro",
			"Fevereiro",
			"Marco",
			"Abril",
			"Maio",
			"Junho",
			"Julho"
		]
		return labels

	def get_providers(self):

		datasets = [
			"Central",
			"Eastside",
			"Westside"
		]

		return datasets

	def get_data(self):

		# dados = []
		# for l in range(6):
		# 	for c in range(12):
		# 		dado = [
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200),
		# 			randint(1, 200)
		# 		]
		# 	dados.append(dado)
		# return dados
		return [[75, 44, 92, 11, 44, 95, 35],
                	  [41, 92, 18, 3, 73, 87, 92],
                    [87, 21, 94, 3, 90, 13, 65]]