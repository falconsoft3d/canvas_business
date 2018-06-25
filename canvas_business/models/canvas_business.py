# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class canvas_business(models.Model):
    _description = "canvas business"
    _name = 'canvas.business'

    name = fields.Char('Nombre', translate=True )
    texto = fields.Text('Texto', translate=True ,default='''Business model canvas, traducido como lienzo de modelo de negocio, es una plantilla de gestión estratégica para el desarrollo de nuevos modelos de negocio o documentar los ya existentes. Es un gráfico visual con elementos que describen propuesta de producto o de valor de la empresa, la infraestructura, los clientes y las finanzas. Ayuda a las empresas a alinear sus actividades mediante la ilustración de posibles compensaciones. El modelo de negocio del lienzo fue propuesto inicialmente por Alexander Osterwalder1​ sobre la base de su trabajo anterior sobre la ontología de los modelos de negocio. Desde la publicación de la obra de Osterwalder en 2008, han aparecido nuevos lienzos para nichos específicos, como el Lienzo Lean. Las descripciones formales del negocio se convierten en los bloques de construcción para sus actividades. Existen muchas diferentes conceptualizaciones de negocio; El trabajo de Osterwalder y tesis (2010, de 2004) proponen un modelo único de referencia basada en las similitudes de una amplia gama de conceptualizaciones de modelo de negocio. Con su diseño de la plantilla modelo de negocio, una empresa puede describir fácilmente su modelo de negocio.''')

    partners_clave = fields.Text('Partners Clave', translate=True, default='¿Qué pueden hacer los partner mejor que tú o con un coste menor y , por tanto enriquecer tu modelo de negocio?')
    actividades_clave = fields.Text('Actividades Clave', translate=True, default='¿Qué actividades clave hay que desarrollar en su modelo de negocio de que manera las llevas a cabo?')
    propuesta_de_valor = fields.Text('Propuesta de Valor', translate=True, default='¿Qué problemas solucionamos?¿Qué necesidad satisfacemos?¿Qué beneficios aporta?')
    relacion_con_clientes = fields.Text('Relación con Clientes', translate=True, default='¿Qué tipo de relaciones esperan tus clientes que establezcas y mantengas con ellos?')
    segmentos_de_clientes = fields.Text('Segmentos de Clientes', translate=True, default='¿A quién nos dirigimos?¿Qué segmentos consideramos?¿Cuales son prioritarios?')
    recursos_claves = fields.Text('Recursos Claves', translate=True, default='¿Qué recursos clave requiere tu modelo de negocio?')
    canales = fields.Text('Canales', translate=True, default='¿A través de qué canales/medios contactarás y atenderás a tus clientes?')
    estructura_de_coste = fields.Text('Estructura de Coste', translate=True, default='¿Cuál es la estructura de costes de tu modelo de negocio?')
    flujos_de_ingresos = fields.Text('Flujos de Ingresos', translate=True, default='¿Qué valor están dispuestos a pagar tus clientes por tu solución y mediante qué formas de pago?¿Qué margenes obtengo?')

