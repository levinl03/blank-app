import streamlit as st
import pandas as pd
import plotly.express as px
import apiget

st.title("Shark Tracker Dashboard")
st.markdown("This dashboard shows realtime tracking of sharks")

df = apiget.df
# Toggle button for the legend
show_legend = st.checkbox("Toggle Legend", value=True)
# Interactive map
fig = px.scatter_mapbox(
    df,
    lat='latitude',
    lon='longitude',
    color='species',
    hover_name='name',
    hover_data=['species', 'last_ping'],
    zoom=2,
    height=600,
    opacity=0.8
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(
    clickmode='event+select',  # Click behavior to toggle items
    legend=dict(
        title=dict(text="Shark Species", font=dict(size=14, color="black")),
        font=dict(size=12, color="black"),  # Smaller font size for the legend
        bgcolor="rgba(255,255,255,0.7)",  # Transparent background
        x=1.05,  # Move legend outside the map area to the right
        xanchor='left',  # Anchor legend position
        y=0.5,
        yanchor='middle',  # Center legend vertically
        itemsizing='constant',  # Maintain consistent item size
        itemwidth=40,  # Adjust width of legend items
        tracegroupgap=5,  # Space between groups in the legend
        visible=show_legend  # toggle button for visibility
    ),
    hoverlabel=dict(
        font_size=10,  # Smaller font size for hover labels
        font_family="Arial"
    ),
    annotations=[
        dict(
            x=1.05,  # Position near the legend
            y=1.1,  # Place the button above the legend
            xref='paper',
            yref='paper',
            text="Toggle Legend",  # Button text
            showarrow=False,
            font=dict(size=12, color="blue"),
            align="center",
            bgcolor="rgba(200, 200, 200, 0.5)",  # Light background for the button
            bordercolor="black",
            borderwidth=1
        )
    ]
)
# Display the map
st.plotly_chart(fig)

