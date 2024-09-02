#importar las librerias que necesites
from odoo import models, fields, _, api
from odoo.exceptions import UserError

#Declara la clase que tendrá tu modelo y los métodos
class NombreClase(models.Model):
  _name='nombre.modelo'  #asi declaras el nombre de tu modelo, que será el nombre de la tabla en la base de datos

  #puedes declarar todos los campos Many2One que necesites
  #Un campo many2One, muestra todos los registros que se encuentren dentro de un modelo.

  #Creamos un campo para mostrar los paises
  countries_id = fields.Many2one('res.country', string='País')

  #creamos un campo para mostrar los contactos
  partners_id = fields.Many2one('res.partner', string='Contactos')

  #creamos un campo para mostrar las ventas
  orders_id = fields.Many2one('sale.order', string='Ventas')

  #Y así sucesivamente con todos los campos Many2One que quieras crear



