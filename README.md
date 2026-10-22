# Experiment - Masaharu
October/2026
NOMACHI, Masaharu
An activity of photon counting detection.

## Introduction
This activity tries to achieve photon counting from a weak light source where photons are emited. If we have a highly sensitive detector (SiPM) with enough gain we can collect some of the photons.
## Setup experiment
![[IEEE - SPSS School-1792628113191.webp]]
DAQ processing are gonna be in Red Pitaya and data lecture and analysis in a conventional laptop connected via WiFi.
### Light Pulser
![[IEEE - SPSS School-1792628217844.webp]]Light was emitted by blue LED ($\lambda=465\,\text{nm}$) where all charge is given by capacitor $c=100\,\text{pF}$. Exceded voltage allows excedent of charge that leads to LED bright.
> [!success] Necessary energy of a blue photon.
> It will require
> $$
> E=h\nu=\frac{hc}{\lambda}= \frac{2\pi \hbar c}{\lambda}= \frac{2\pi (197\,\text{eV}\cdot\text{nm})}{465\,\text{nm}}=2.67\,\text{eV}
> $$
> This is the minimum voltage, but it will be barely visible.

In this exercise, we will need 3.2 V due to resistence and so on. For example, if 4.8 V is applied, the excess voltage is 1.6 V. Then charge is $Q=CV=(100\,\text{pF})(1.6\,\text{V})=160\,\text{pC}$.

> [!success] 160 pC of electrons ﬂow through the LED. How many electrons is that?
> $$
> N_{e} = \frac{C}{e} = \frac{160\,\text{pF}}{1.6\times10^{-19}\,\text{C}} = 10^9\,\text{electrons}
> $$

It's hard to predict how much photons will emitt (LED properties, internal resistance, etc.).

Pulses were seen on a digital oscilloscope *MPPC Scope*. It was set the trigger rate to 1000 Hz for a bias voltage of -11 to -13 V. This will emitt even less light for photon counting. For emitting light it's necessary to get 
### MPPC (Multi-pixel Photon Counter)
![[IEEE - SPSS School-1792631808190.webp]]
- Composed of many pixels, each of one an avalanche photodiode. 
- Operates in Geiger mode. 
- S10362-11-050C has 400 pixels. 
- Don't operate under bright light.
- Reverse voltage of 70 V→ dark current.

MPPC Scope for this dark current (100 kcps) takes in a coarse frame (4 µs) around 0.4 counts. That is approximately 0-2 pulses expected. *This is a signal to continue.*

## Histogram
In our case, there were **two measurements**

![[figs/window_histogram_0.png|344]]![[figs/window_histogram_1.png|342x171]]

where the results are

![[poisson_fit_0.png]]![[poisson_fit_1.png]]

Accurated analysis on notebook.