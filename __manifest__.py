# -*- coding: utf-8 -*-
{
    'name': "Compute Price_List",

    'summary': """
        Aplicación para calcular el precio de venta con el margen y costo de flete ingresado""",

    'description': """
        La app agrega los campos margen y costo de flete. con estos valores y el costo calcula el precio de venta
    """,

    'author': "Matias Marinelli",
    'website': "https://www.devcode73.com.ar",
    'installable': True,
    'application': False,  # Indica que es una aplicación


    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'views/compute_price_temp.xml',
        'views/compute_price_prod.xml',
    ],
}
