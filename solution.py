from sample_data import PROPERTY_DATA,QUERY_DATA

for req in QUERY_DATA:
	ans = []
	for i in PROPERTY_DATA:
		match = 0

		dist = ((req['lat'] - i['lat'])**2) + ((req['long'] - i['long'])**2)
		if dist <=4:
			match+=30
		elif dist<=100:
			match+=15
		else:
			continue

		if 'min_price' in req and 'max_price' in req:
			l = req['min_price']
			r = req['max_price']
			ll = req['min_price']*0.75
			rr = req['max_price']*1.25
		elif 'min_price' in req:
			l = req['min_price']*0.9
			r = req['min_price']*1.1
			ll = req['min_price']*0.75
			rr = req['min_price']*1.25
		elif 'max_price' in req:
			l = req['max_price']*0.9
			r = req['max_price']*1.1
			ll = req['max_price']*0.75
			rr = req['max_price']*1.25

		if ll < i['price'] and rr > i['price']:
			if l < i['price'] and r > i['price']:
				match +=30
			else:
				match+=15
		else:
			continue

		if 'min_rooms' in req and 'max_rooms' in req:
			l = req['min_rooms']
			r = req['max_rooms']
			ll = req['min_rooms']-2
			rr = req['max_rooms']+2
		elif 'min_rooms' in req:
			l = req['min_rooms']
			r = req['min_rooms']
			ll = req['min_rooms']-2
			rr = req['min_rooms']+2
		elif 'max_rooms' in req:
			l = req['max_rooms']
			r = req['max_rooms']
			ll = req['max_rooms']-2
			rr = req['max_rooms']+2

		if ll <= i['n_bed'] and rr >= i['n_bed']:
			if l <= i['n_bed'] and r >= i['n_bed']:
				match+=20
			else:
				match+=10
		else:
			continue


		if 'min_bath' in req and 'max_bath' in req:
			l = req['min_bath']
			r = req['max_bath']
			ll = req['min_bath']-2
			rr = req['max_bath']+2
		elif 'min_bath' in req:
			l = req['min_bath']
			r = req['min_bath']
			ll = req['min_bath']-2
			rr = req['min_bath']+2
		elif 'max_bath' in req:
			l = req['max_bath']
			r = req['max_bath']
			ll = req['max_bath']-2
			rr = req['max_bath']+2

		if ll <= i['n_bath'] and rr >= i['n_bath']:
			if l <= i['n_bath'] and r >= i['n_bath']:
				match+=20
			else:
				match+=10
		else:
			continue


		if match >= 40:
			ans.append([i['id'],match])
		else:
			continue

	print(req['id'], ans)