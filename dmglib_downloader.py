import requests
import urllib
import os




url_libro=input("Inserisci l'url del libro che vuoi scaricare: ")
book_id=url_libro.split('=')[-1]



with requests.session() as s:
	r=s.get(url_libro)

	#Getting the filenames
	point=r.text.lower().find('array')
	point=r.text.find('(',point+5)+1
	end_point=r.text.find(';',point)-1
	img_list=r.text[point:end_point]
	img_list=img_list.split(',')
	for i in range(len(img_list)):
		point=img_list[i].find('"')+1
		end_point=img_list[i].find('"',point)
		img_list[i]=img_list[i][point:end_point]


	#Downloading the files
	try:
		for i in range(len(img_list)):
				
			post_data={
			'pageID':i+1,
			'fileName':img_list[i],
			'bookid':book_id,
			'width':656,
			'height':898,
			'zoomfaktor':2,
			'MasterScaleFactor':1,
			'tooltips':'false',
			#searchstring
			'debugmode':'false',
			'enhancedContent':'true',
			'searchstringHighlight':'true',
			'commentVisible':'false',
			'hyperlinksVisible':'false',
			'pageAlign':1,
			'rotateImage':0,
			}
			
			r=s.post('http://www.dmg-lib.org/dmglib/streambook/template/pageLoad.jsp',data=post_data)
				
			if i==0 and r.status_code==200:
				print('\n\nDownload in corso...')
			
			point=r.text.find('src')
			point=r.text.find('"',point)+1
			end_point=r.text.find('"',point)
			img_dir=r.text[point+5:end_point]
			urllib.request.urlretrieve('http://www.dmg-lib.org'+img_dir,img_dir.split('/')[-1])
	except:
		print("\n\nErrore durante il download\n")




	print("Download completato.\n")
	input("Premi invio per continuare...")
