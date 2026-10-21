
# plotly_science.py

import plotly.graph_objects as go
import plotly.io as pio

# Scientific color palette
SCIENCE_COLORS = [
    "#0072B2",  # blue
    "#D55E00",  # vermilion
    "#009E73",  # green
    "#CC79A7",  # reddish purple
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#333333",  # dark gray
]

# Define the scientific template
science = go.layout.Template(
    layout=go.Layout(
        # Typography
        font=dict(
            family="STIX Two Text, STIXGeneral, Times New Roman, serif",
            size=14,
            color="#222222",
        ),

        title=dict(
            font=dict(size=18),
            x=0.02,
            xanchor="left",
            y=0.98,
            yanchor="top",
        ),

        # White background
        paper_bgcolor="white",
        plot_bgcolor="white",
        colorway=SCIENCE_COLORS,

        # Figure dimensions and spacing
        margin=dict(l=85, r=30, t=75, b=75),
        autosize=True,

        # Axes
        xaxis=dict(
            showline=True,
            linecolor="#222222",
            linewidth=1,
            mirror=True,
            ticks="outside",
            tickcolor="#222222",
            tickwidth=1,
            ticklen=5,
            showgrid=False,
            zeroline=False,
            automargin=True,
            title=dict(standoff=12),
        ),

        yaxis=dict(
            showline=True,
            linecolor="#222222",
            linewidth=1,
            mirror=True,
            ticks="outside",
            tickcolor="#222222",
            tickwidth=1,
            ticklen=5,
            showgrid=False,
            zeroline=False,
            automargin=True,
            title=dict(standoff=12),
        ),

        # Legend
        legend=dict(
            bgcolor="rgba(255,255,255,0.8)",
            borderwidth=0,
            font=dict(size=12),
        ),

        # Interactive hover labels
        hoverlabel=dict(
            bgcolor="white",
            bordercolor="#444444",
            font=dict(
                family="STIX Two Text, STIXGeneral, Times New Roman, serif",
                size=13,
                color="#222222",
            ),
        ),

        # Clean, unobtrusive interaction toolbar
        hovermode="closest",
    ),

    # Default styling for bar charts
    
)

# Register the theme and activate it globally
pio.templates["science"] = science
pio.templates.default = "science"
