import requests
from rich.console import Console
from rich.table import Table

# RestCountries API to get water supply data (using natural resources as a proxy)
BASE_URL = "https://restcountries.com/v3.1/all"
console = Console()

def fetch_all_water_supply_data():
    try:
        # Make API request for all water supply data
        response = requests.get(BASE_URL)
        if response.status_code != 200:
            console.print(f"[red]Error fetching data: Status code {response.status_code}[/]")
            return None
        
        data = response.json()
        return data
    except Exception as e:
        console.print(f"[red]Error fetching data: {e}[/]")
        return None

def fetch_water_supply_data(country_name):
    try:
        # Make API request for specific country water supply data
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        if response.status_code != 200:
            console.print(f"[red]Error fetching data: Status code {response.status_code}[/]")
            return None
        
        data = response.json()
        return data[0] if len(data) > 0 else None
    except Exception as e:
        console.print(f"[red]Error fetching data: {e}[/]")
        return None

def display_water_supply_data(country_name):
    country_data = fetch_water_supply_data(country_name)
    
    if country_data is None:
        console.print(f"[red]No data found for country: {country_name}[/]")
        return
    
    # Extract water-related information (using area, population, and other resources as a proxy)
    country_name = country_data.get("name", {}).get("common", "N/A")
    population = country_data.get("population", 0)
    area = country_data.get("area", 1)  # Default area to 1 if missing to avoid division by zero
    water_resources = country_data.get("naturalResources", "N/A")
    region = country_data.get("region", "N/A")
    population_density = population / area if area > 0 else 0
    
    table = Table(title=f"Water Supply Data for {country_name}", show_header=True, header_style="bold magenta")
    
    # Create headers for the table
    table.add_column("Country", style="dim")
    table.add_column("Population")
    table.add_column("Region")
    table.add_column("Population Density (people per sq km)")
    table.add_column("Natural Resources")
    
    # Display data for the country
    table.add_row(country_name, f"{population:,}", region, f"{population_density:.2f}", str(water_resources))
    
    console.print(table)

def display_top_10_water_supply_countries():
    all_data = fetch_all_water_supply_data()
    
    if all_data is None:
        return
    
    # Extract population and country name
    country_list = []
    for country in all_data:
        country_name = country.get("name", {}).get("common", "N/A")
        population = country.get("population", 0)
        country_list.append((country_name, population))
    
    # Sort by population in descending order and take top 10
    top_countries = sorted(country_list, key=lambda x: x[1], reverse=True)[:10]
    
    table = Table(title="Top 10 Countries by Population", show_header=True, header_style="bold magenta")
    
    # Create headers for the table
    table.add_column("Country", style="dim")
    table.add_column("Population")
    
    # Display data for top 10 countries
    for country_name, population in top_countries:
        table.add_row(country_name, f"{population:,}")
    
    console.print(table)

def main():
    user_input = console.input("Enter the names of the countries (comma-separated) / type 'top' for top 10 countries by population: ").strip().lower()
    if user_input == "top":
        display_top_10_water_supply_countries()
    else:
        country_list = [name.strip() for name in user_input.split(',')]
        for country_name in country_list:
            display_water_supply_data(country_name)

if __name__ == "__main__":
    main()