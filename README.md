# Photon Counting

Photon-counting analysis using an MPPC/SiPM and two measurement datasets.
The project includes Bokeh and Plotly versions, along with the resulting
figures.

## Packages Used

- **NumPy** and **Pandas**: data handling and analysis.
- **SciPy**: curve fitting and Poisson distribution analysis.
- **Bokeh**: interactive plots in the main notebook.
- **Plotly**: alternative interactive visualization.
- **CairoSVG**: exporting SVG plots to PDF.
- **JupyterLab**: running the notebooks.

## Installation

From the project directory, install the required packages with:

```bash
python -m pip install numpy pandas scipy bokeh plotly cairosvg jupyterlab
```

## Reproducing the Analysis

1. Open the project directory in a terminal.
2. Start JupyterLab:

   ```bash
   jupyter lab
   ```

3. Open either `photon_counting.ipynb` or `photon_counting_plotly.ipynb`.
4. Run all cells from beginning to end.

Keep `MPPC_1.csv` and `MPPC_2.csv` in the project directory so the notebooks
can load the measurement data.

## Files

- `photon_counting.ipynb`: main analysis using Bokeh.
- `photon_counting_plotly.ipynb`: alternative analysis using Plotly.
- `photon_counting.py`: executable version of the Plotly analysis.
- `plotly_science.py`: scientific visualization template for Plotly.
- `photon_counting.html`: HTML export of an interactive plot.
- `MPPC_1.csv` and `MPPC_2.csv`: data from the two measurements.
- `figs/`: histograms, Poisson fits, and exported figures.
- `Photon Counting Experiment.pdf`: experiment report.
- `docs/Photosensor-2026 October v2.0.pdf`: photosensor documentation.
- `docs/Photon-counting-exercise-2026-v1.pdf`: exercise guide.
