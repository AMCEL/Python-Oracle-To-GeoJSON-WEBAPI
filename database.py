import cx_Oracle
import simplejson

con_oracle = cx_Oracle.connect(u'USERNAME/PASSWORD@TNS')

def glebas():
	glebas = []
	cursor = con_oracle.cursor()
	cursor.execute('select id_gleba, nm_gleba from florestal.gleba order by nm_gleba')
	for gleba in cursor:
		row = {
			'id_gleba': gleba[0],
			'nm_gleba': gleba[1]
		}
		glebas.append(row)
	return simplejson.dumps(glebas)
