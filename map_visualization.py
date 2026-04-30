import pandas as pd
import pydeck as pdk

FACTORIES = {
    "Lot's O' Nuts": (32.881893, -111.768036),
    "Wicked Choccy's": (32.076176, -81.088371),
    "Sugar Shack": (48.11914, -96.18115),
    "Secret Factory": (41.446333, -90.565487),
    "The Other Factory": (35.1175, -89.971107)
}

def create_map(factory_name, customer_lat=28.6139, customer_lon=77.2090):

    factory_lat, factory_lon = FACTORIES[factory_name]

    data = pd.DataFrame({
        'from_lon': [factory_lon],
        'from_lat': [factory_lat],
        'to_lon': [customer_lon],
        'to_lat': [customer_lat],
    })

    layer = pdk.Layer(
        "ArcLayer",
        data,
        get_source_position='[from_lon, from_lat]',
        get_target_position='[to_lon, to_lat]',
        get_width=5,
        get_source_color=[255, 0, 0],
        get_target_color=[0, 255, 0],
    )

    view_state = pdk.ViewState(
        latitude=(factory_lat + customer_lat) / 2,
        longitude=(factory_lon + customer_lon) / 2,
        zoom=3
    )

    return pdk.Deck(layers=[layer], initial_view_state=view_state)