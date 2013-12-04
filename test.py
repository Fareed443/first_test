from openerp.osv import osv, fields
from datetime import datetime,time

class test(osv.osv):
    """Test Class"""

    _name = 'test'
    _description = 'test'
    
    _columns = {
        'name': fields.char('Name', size=64, required=True , tranlsate = True),
        'date': fields.date('Date',),
        'city': fields.char('City',required=True, size=50),
#        'testing': fields.char('City',required=True, size=50),
        'state':fields.char('State',required=True, size=50),
        'zip'  :fields.char('Zip', size=50),   
        'lines' : fields.one2many('test.child','test_ids',ondelete = 'cascade'),  
    }
    
    _defaults = {
    
                    'date'   : lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }
test()   

class test_child(osv.osv):
	"""Test Child"""		
	
	_name = 'test.child'
	_description = 'Test Child'
	_columns = {
		'test_ids': fields.many2one('test','TEstChild',hidden=True),
		'name' : fields.char('Name',size=5,required=True),
		'desc' : fields.text('Description',size=10),
			}		
test_child()	
	
