#!/usr/bin/env python
# coding: utf-8

# # Photodetection Statistical fluctuation
# October/2026
# NOMACHI, Masaharu
# 
# An activity of photon counting detection. 

# In[1]:


# import libraries, Plotly template and MathJax for Jupyter Notebook
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio

##############################
axis = {
    "mirror": True,
    "showline": True,
    "ticks": "inside",
    "showgrid": True,
    "minor_ticks": "inside",
}
pio.templates["science"] = {
    "layout": {
        "xaxis": axis,
        "yaxis": axis,
    },
}
pio.templates.default = "simple_white+science"


# We observed the peaks refered to *photon counting*.

# In[6]:


# data import and visualization
data = [
    pd.read_csv(file, usecols=["Center_V", "Counts"]).rename(
        columns={"Center_V": "voltage", "Counts": "counts"}
    )
    for file in ["MPPC_1.csv", "MPPC_2.csv"]
]

fig = px.bar(
    data[1],
    x="voltage",
    y="counts",
    title="Photon counting",
    labels={
        "voltage": r"label $V \text{ (V)}$", 
        "counts": r"label $N_{\text{counts}}$"
    },
)

fig.update_layout(
    xaxis=dict(
        title_font=dict(size=20),
    ),
    yaxis=dict(
        title_font=dict(size=20),
    ),
    xaxis_title_font=dict(size=20),
    yaxis_title_font=dict(size=20),
    title_font=dict(size=20),
)

fig.show()
data = data[1]


# In[7]:


# fig.write_html(
#     "photon_counting.html",
#     include_plotlyjs=True,
#     full_html=True,
# )


# # In[4]:


# print("Título X:", fig.layout.xaxis.title.font.size)
# print("Título Y:", fig.layout.yaxis.title.font.size)
# print("Fuente global:", fig.layout.font.size)
# print("Plantilla:", fig.layout.template)


# ## Data analysis

# Since the first data set has only one peak, 
# We're gonna do two methods: one simpler, as windows of voltage; one complex, as gaussian fit.

# ### A) windows

# In[3]:


# fig = px.bar(
#     data[1],
#     x="voltage",
#     y="counts",
#     title="Photon counting",
#     labels={
#         "voltage": r"$V \text{ (V)}$",  # Todo encerrado en $...$
#         "counts": r"$N_{\text{counts}}$"
#     },
# )

# fig.show()

