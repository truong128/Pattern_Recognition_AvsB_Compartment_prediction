import matplotlib.pyplot as plt
import numpy as np
import os

def main():
	data = {
		"Mean Baseline":[0.872,0.893,0.850,0.938,0.905,0.916],
		"CoRNN (our model)":[0.901,0.938,0.857,0.957,0.953,0.916],
		"GRU":[0.925,0.940,0.697,0.916,0.926,0.775],
		"Random Forest":[0.826, 0.785, 0.689, 0.723,0.790, 0.533],
		"Random Forest (add mean)":[0.837, 0.852,0.788, 0.872,0.880,0.810],
		"Logistic Regression":[0.815,0.806,0.506,0.738,0.533,0.653],
		"Logistic Regression (add mean)":[0.830,0.835,0.788,0.883,0.837,0.814]
	}
	labels = ["IMR90","K562", "NHEK", "HMEC", "GM12878", "HUVEC"]
	title = "Testing Performance"
	# colors = ["tab:blue","tab:orange","tab:cyan","tab:purple"]
	plotBarGraph_final_bar(labels,data,title)


	"100kb_rf_600":[0.819,0.748,0.641,0.659,0.532,0.501],
		"100kb_rf_600_with_mean":[0.842,0.836,0.770,0.783,0.773,0.589],


def plotBarGraph_final_bar(labels, data, title):
	labels_order = ["GM12878", "K562", "IMR90","HMEC", "NHEK", "HUVEC"]
	
	x = np.arange(len(labels))  # the label locations
	width = 0.1 # the width of the bars

	print(len(list(data)))
		
	fig, ax = plt.subplots(figsize=(12,5))
	bar_name = list(data.keys())
	bar_value = list(data.values())
	bar_value = np.array(bar_value)
	val_by_cell = {}


	for i, label in enumerate(labels):
		val_by_cell[label] = bar_value[:,i]

	print(val_by_cell)
	bar_val_updated = np.zeros((7,6))
	
	for i, label in enumerate(labels_order):
		bar_val_updated[:,i] = val_by_cell[label]
		
	print(bar_val_updated)
	bar_value = bar_val_updated


	colors = ['#88BEE7','#F0B67F','#8CC084','#9180C6','#D47395','#87d4d4','#F9D88A',]

	rects1 = ax.bar(x - 3*width, bar_value[0], width, label=bar_name[0],color = colors[0], edgecolor='white')
	rects2 = ax.bar(x - 2*width, bar_value[1], width, label=bar_name[1],color = colors[1], edgecolor='white')
	rects3 = ax.bar(x - width, bar_value[2], width, label=bar_name[2],color = colors[2], edgecolor='white')
	rects4 = ax.bar(x, bar_value[3], width, label=bar_name[3],color = colors[3], edgecolor='white')
	rects5 = ax.bar(x + width, bar_value[4], width, label=bar_name[4],color = colors[4], edgecolor='white')
	rects6 = ax.bar(x + 2*width, bar_value[5], width, label=bar_name[5],color = colors[5], edgecolor='white')
	rects7 = ax.bar(x + 3*width, bar_value[6], width, label=bar_name[6],color = colors[6], edgecolor='white')
	# Add some text for labels, title and custom x-axis tick labels, etc.
	ax.set_ylabel('Testing AUROC')
	ax.set_title(title)
	ax.set_xticks(x)
	ax.set_xticklabels(labels_order)
	plt.yticks(fontsize=10)
	ax.legend(loc='lower left',fontsize = 6)

	plt.ylim([0.3,1.0])

	bar_label_font_size = 4

	ax.bar_label(rects1, padding=3,fontsize=bar_label_font_size)
	ax.bar_label(rects2, padding=3,fontsize=bar_label_font_size)
	ax.bar_label(rects3, padding=3,fontsize=bar_label_font_size)
	ax.bar_label(rects4, padding=3,fontsize=bar_label_font_size)
	ax.bar_label(rects5, padding=3,fontsize=bar_label_font_size)
	ax.bar_label(rects6, padding=3,fontsize=bar_label_font_size)
	ax.bar_label(rects7, padding=3,fontsize=bar_label_font_size)

	# ax.bar_label(rects4, padding=3)

	fig.tight_layout()

	plt.show()
	plt.savefig("CoRNN-vs-baselines.eps", format='eps')
	plt.clf()

if __name__ == "__main__":
    main()