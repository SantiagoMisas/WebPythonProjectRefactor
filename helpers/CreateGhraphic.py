import matplotlib.pyplot as plt

colors = ['blue', 'green', 'yellow', 'orange', 'purple']
graphicsRoute = "figures/graphic.png"

def generategraphic(list, xatribute, yatribute, xname, yname, title, pngroute, pdfroute, colors):
  list = list.astype(str)
  plt.figure(figsize=(10, 10))
  plt.bar(xatribute, yatribute, color=colors)
  plt.xlabel(xname)
  plt.ylabel(yname)
  plt.title(title)
  plt.xticks(rotation=45)
  plt.savefig(pngroute)
  plt.savefig(pdfroute)
  plt.show()