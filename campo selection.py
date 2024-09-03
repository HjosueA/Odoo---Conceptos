#importar las librerias que necesites
from odoo import models, fields, _, api
from odoo.exceptions import UserError

#Declara la clase que tendrá tu modelo y los métodos
class NombreClase(models.Model):
  _name='nombre.modelo'  #asi declaras el nombre de tu modelo, que será el nombre de la tabla en la base de datos

  #puedes declarar todos los campos Selection que necesites
  #Un campo Selection, muestra todos los registros que se encuentren dentro de un modelo.

  #Creamos un campo para mostrar los estados de un formulario
  state = fields.Selection([('borrador', 'Borrador'), ('hecho', 'Hecho')], string='Estado', default='borrador')

  #Y así sucesivamente con todos los campos Selection que quieras crear
