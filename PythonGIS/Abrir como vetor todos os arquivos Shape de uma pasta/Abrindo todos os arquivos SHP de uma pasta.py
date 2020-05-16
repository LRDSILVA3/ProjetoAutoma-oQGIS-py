import os
# pasta onde se envontra as imagens que deseja trabalhar
pathName = 'c:\\Perimetros'

for folderName, subfolders, filenames in os.walk(pathName):
	print('O diretório corrente é  ' + folderName)
	
	cont_name = 0
	saida = 'c:\\Perimetros'
	# Percorre todos os arquivos da pasta indicada
	for filename in filenames:
		
		# Abrindo o arquivo
		print('Percorrendo o arquivo: ' + filename)
		if'.shp' in filename:#Cria um Vetor para cada arquivo
			print('Abrindo o arquivo:'+filename)
			layer = iface.addVectorLayer(folderName,filename,'ogr')
			# Carregando o vetorn no QGIS
			canvas = qgis.utils.iface.mapCanvas()
