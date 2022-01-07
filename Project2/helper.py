# Import packages
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv (r'/Users/zuriel/Desktop/DataSapiens/Project2/synergy_logistics_database.csv')
# Remove unnecesary columns 
df = df.drop(columns = ['register_id', 'year'])

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


# Define function to process data
def helper_function():


    print(color.RED + "##############################################################################" + color.END)
    print(color.RED + "##############################################################################" + color.END)
    print(color.RED + "\n \n  A CONTINUACIÓN SE MUESTRA UN REPORTE DE LAS IMPORTACIONES Y EXPORTACIONES DE", color.BOLD + "Synergy Logistics" + color.END, "\n \n" + color.END)
    print(color.RED + "##############################################################################" + color.END)
    print(color.RED +"##############################################################################" + color.END)

    # Group data by Origin, Destination and Transport mode, then sum and sort values
    routes_df = df.groupby([df['origin'],df['destination'], df['transport_mode']]).sum('total_value').sort_values('total_value', ascending = False)
    # Select top 10 routes
    routes_top = routes_df.head(10)
    print(color.GREEN + "############################################################################## \n" + color.END)
    print('\n 10 Rutas más demandadas: \n',routes_top)
    print(color.GREEN + "############################################################################## \n" + color.END)

    # Group data by Transport mode, then sum and sort values
    transport_df = df.groupby([df['transport_mode']]).sum('total_value').sort_values('total_value', ascending = False)
    # Select top 3 transport modes
    transport_top = transport_df.head(3)
    print(color.YELLOW + "############################################################################## \n" + color.END)
    print('\n Medios de transporte más utilizados: \n', transport_top)
    print(color.YELLOW + "############################################################################## " + color.END)

    # Group data by Origin,  then sum and sort values
    total_origin = df.groupby([df['origin']]).sum('total_value').sort_values('total_value', ascending = False)
    # Get percent from total
    total_origin['percent'] = (total_origin['total_value'] / total_origin['total_value'].sum() * 100)
    # Reset index
    total_origin.reset_index(level=0, inplace= True)
    # Add column with cumulative sum
    total_origin['CUMSUM'] = total_origin['percent'].cumsum()
    # Filter by CUMSUM < 80%
    total_origin_result = total_origin[total_origin['CUMSUM'] <80]
    print(color.CYAN + "############################################################################## \n" + color.END)
    print('\nPaises que aportan el 80% de las exportaciones: \n',total_origin_result)
    print(color.CYAN + "############################################################################## " + color.END)

    # Group data by Destination,  then sum and sort values
    total_destination = df.groupby([df['destination']]).sum('total_value').sort_values('total_value', ascending = False)
    # Get percent from total
    total_destination['percent'] = (total_destination['total_value'] / total_destination['total_value'].sum() * 100)
    # Reset index
    total_destination.reset_index(level=0, inplace= True)
    # Add column with cumulative sum
    total_destination['CUMSUM'] = total_destination['percent'].cumsum()
    # Filter by CUMSUM < 80%
    total_destination_result = total_destination[total_destination['CUMSUM'] < 80]
    print(color.CYAN + "############################################################################## \n" + color.END)
    print('\nPaises que aportan el 80% de las importaciones: \n', total_destination_result)
    print(color.CYAN + "############################################################################## " + color.END)

    return 
