from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#import pandas as pd
from collections import Counter
import pandas as pd
from collections import defaultdict
# Setting de colores para imprimir
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#lifestore_searches = [id_search, id product]
#lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
#lifestore_products = [id_product, name, price, category, stock]

# Creación de una función para ser llamada desde main
def helper_function():
    print(color.RED + "##############################################################################" + color.END)
    print(color.RED + "##############################################################################" + color.END)
    print(color.RED + "\n \n  A CONTINUACIÓN SE MUESTRA UN REPORTE DE LAS VENTAS DE", color.BOLD + "LifeStore" + color.END, "\n \n" + color.END)
    print(color.RED + "##############################################################################" + color.END)
    print(color.RED +"##############################################################################" + color.END)

    # Creación de data frames para un trabajo mas sencillo de los datos 
    df_lifestore_product = pd.DataFrame(lifestore_products, columns=["id_product", "name", "price", "category", "stock"])
    df_lifestore_sales = pd.DataFrame(lifestore_sales, columns=["id_sale", "id_product", "score" , "date", "refund"])
    df_lifestore_searches = pd.DataFrame(lifestore_searches, columns=["id_search", "id_product"])
    # Merge de productos y ventas 
    df_total = pd.merge(df_lifestore_product,df_lifestore_sales[["id_sale", "id_product", "score" , "date", "refund"]], on = "id_product")
    # Merge de searchs y productos 
    df_total_searches = pd.merge(df_lifestore_searches, df_lifestore_product[["id_product", "name", "category"]], on = "id_product")
    # Cambio de formato para la columna date
    df_total['date'] = pd.to_datetime(df_total['date'])
    # Filtrar productos en refund y no refund 
    saled = df_lifestore_sales["refund"] == 0

    filtered_lifestore_sales = df_lifestore_sales[saled]

    # conteo de productos totales vendidos
    filtered_df_total = df_total[saled]
    sales = filtered_lifestore_sales["id_product"].value_counts()
    sales = pd.DataFrame(sales)
    # Conteo de productos vendidos por categoria
    sales_category = df_total["category"].value_counts()


    print(color.GREEN + "############################################################################## \n" + color.END)
    print("Productos más vendidos y productos rezagados\n")
    print(color.GREEN + "############################################################################## \n" + color.END)

    # Conteo de los 5 productos más vendidos
    sales_name = df_total["name"].value_counts()
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print( "Los 5 productos más vendidos de toda la tienda son: \n \n", sales_name.head(5), "\n" )
    print(color.YELLOW + "############################################################################## " + color.END)

    # Conteo de el top 10 de busquedas
    top_searches = df_total_searches["name"].value_counts()
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 10 productos con mayores búsquedas en toda la tienda son: \n \n", top_searches.head(10), "\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)

    # Creación de data frames para ventas por categoria
    less_sales_tarjetas = df_total[(df_total.category == "tarjetas de video")]
    less_sales_audifonos = df_total[(df_total.category == "audifonos")]
    less_sales_pantallas = df_total[(df_total.category == "pantallas")]
    less_sales_bocinas = df_total[(df_total.category == "bocinas")]
    less_sales_memorias = df_total[(df_total.category == "memorias usb")]

    # Conteo de productos menos vendidos por categoría 
    top_less_sales_tarjetas = less_sales_tarjetas["name"].value_counts()
    top_less_sales_audifonos = less_sales_audifonos["name"].value_counts()
    top_less_sales_pantallas = less_sales_pantallas["name"].value_counts()
    top_less_sales_bocinas = less_sales_bocinas["name"].value_counts()
    top_less_sales_memorias = less_sales_memorias ["name"].value_counts()

    print(color.YELLOW + "##############################################################################" + color.END)
    print("Los 5 productos con menores ventas en toda la tienda son: \n \n", sales_name.tail(5), "\n \n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con menores ventas de la categoria Tarjetas de video son: \n \n", top_less_sales_tarjetas.tail(), "\n \n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con menores ventas de la categoria Audífonos son: \n \n", top_less_sales_audifonos.tail(), "\n \n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con menores ventas de la categoria Pantallas son: \n \n", top_less_sales_pantallas.tail(), "\n \n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con menores ventas de la categoria Bocinas son: \n \n", top_less_sales_bocinas.tail(), "\n \n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con menores ventas de la categoria Memorias son: \n \n", top_less_sales_memorias.tail(), "\n \n \n")

    # Creación de data frames para busquedas por categoria
    less_searches_tarjetas = df_total_searches[(df_total_searches.category == "tarjetas de video")]
    less_searches_audifonos = df_total_searches[(df_total_searches.category == "audifonos")]
    less_searches_pantallas = df_total_searches[(df_total_searches.category == "pantallas")]
    less_searches_bocinas = df_total_searches[(df_total_searches.category == "bocinas")]
    less_searches_memorias = df_total_searches[(df_total_searches.category == "memorias usb")]
    
    # Conteo de productos menos buscados por categoría 
    top_less_searches_tarjetas = less_searches_tarjetas["name"].value_counts()
    top_less_searches_audifonos = less_searches_audifonos["name"].value_counts()
    top_less_searches_pantallas = less_searches_pantallas["name"].value_counts()
    top_less_searches_bocinas = less_searches_bocinas["name"].value_counts()
    top_less_searches_memorias = less_searches_memorias["name"].value_counts()
    
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 10 productos con menores búsquedas de la categoría Tarjetas de video son: \n \n", top_less_searches_tarjetas.tail(10), "\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 10 productos con menores búsquedas de la categoría Audífonos son: \n \n", top_less_searches_audifonos.tail(10), "\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 10 productos con menores búsquedas de la categoría Pantallas son: \n \n", top_less_searches_pantallas.tail(10), "\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 10 productos con menores búsquedas de la categoría Bocinas son: \n \n", top_less_searches_bocinas.tail(10), "\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 10 productos con menores búsquedas de la categoría Memorias son: \n \n", top_less_searches_memorias.tail(10), "\n \n")
    
    print(color.GREEN + "############################################################################## \n" + color.END)
    print("Productos por reseña en el servicio\n")
    print(color.GREEN + "############################################################################## \n" + color.END)
    
    df_sort_scores = df_total.sort_values(by=["score"],ascending = False)
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con mejores reseñas son: \n \n",df_sort_scores.head(5), "\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 productos con peores reseñas son: \n \n",df_sort_scores.tail(5),"\n \n")
    

    print(color.GREEN + "############################################################################## \n" + color.END)
    print("Total de ingresos y ventas promedio mensuales\nTotal anual y meses con más ventas al año")
    print(color.GREEN + "############################################################################## \n" + color.END)
    
    # Creación de data frames filtrado por mes y año 
    df_total['date_month'] = df_total['date'].dt.strftime('%Y-%m')
    df_total['date_year'] = df_total['date'].dt.strftime('%Y')
    # Suma de ventas por mes y año 
    total_sales_month = df_total.groupby(['date_month'], as_index = False)['price'].sum()
    total_sales_year = df_total["price"].sum()
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("El monto total de ventas es de: \n \n", "$",total_sales_year,"\n \n")
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("El monto promedio de ventas mensual es de: \n \n", "$",total_sales_year/14,"\n \n")
    
    # Suma de el total e ventas por años 
    total_sales_years = df_total.groupby(['date_year'], as_index = False)['price'].sum()
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("El monto total de ventas por año es de: \n \n",total_sales_years,"\n \n")
    # Selección de los 5 meses con mayores ventas
    top_sales_month = total_sales_month.sort_values(by=["price"], ascending=False)
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print("Los 5 meses con mayores ventas son: \n \n",top_sales_month.head())
    print(color.YELLOW + "############################################################################## \n" + color.END)

    return
