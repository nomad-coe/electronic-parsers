# %%
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import integrate

# set constants
ev_to_joule = 1.602177e-19
window = 100
example_files = ('fhi', 'vasp')
# %%
# Read in data and store it in a dataframe or a dictionary
df = pd.DataFrame({})

for filename in example_files:
    program = filename.upper()
    fp = open(filename + '.json')
    data = json.load(fp)
    dos = data['run'][0]['calculation'][0]['dos_electronic'][0]
    fp.close()
    n_entries = len(dos['total'][0]['value'])
    marked_steps = int(n_entries / 1000)  # WARNING: parameter set manually might need adjusting
    df['d' + program] = [x for i, x in enumerate(dos['total'][0]['value']) if (i % marked_steps) == 0]
    df['r' + program] = df['d' + program].rolling(window).mean().fillna(0)
    df['e' + program] = [x for i, x in enumerate(dos['energies']) if (i % marked_steps) == 0]
    df['e' + program] -= dos['energy_fermi']

# Fermi energy for FHIaims version 210716 not properly extracted
df['eFHI'] -= -6.15211356 * ev_to_joule
# %%
# Plot raw (unaligned) DOS
fig_fhi = px.line(df, x='eFHI', y='dFHI')
fig_vasp = px.line(df, x='eVASP', y='dVASP')
fig = go.Figure(data=fig_fhi.data + fig_vasp.data)
fig.show()
# %%
# Plot rolling averages
fig_fhi = px.line(df, x='eFHI', y='rFHI')
fig_fhi.data[0]['line']['color'] = 'orange'
fig_fhi.data[0]['hovertemplate'] = 'FHI<br>eVASP=%{x}<br>rVASP=%{y}<extra></extra>'
fig_vasp = px.line(df, x='eVASP', y='rVASP')
fig_vasp.data[0]['line']['color'] = 'blue'
fig_vasp.data[0]['hovertemplate'] = 'VASP<br>eVASP=%{x}<br>rVASP=%{y}<extra></extra>'

fig = go.Figure(data=fig_fhi.data + fig_vasp.data)
fig.update_layout(title='Rolling average (window = ' + str(window) + ' pts)')
fig.show()
# %%
# Compute the integral (#valence electrons and the ratio)
dos_integral = {}
for filename in example_files:
    program = filename.upper()
    dos_integral[program] = integrate.trapz(df.loc[df['e' + program] < 0, 'd' + program], df.loc[df['e' + program] < 0, 'e' + program])
print('FHI: ' + str(dos_integral['FHI']))
print('VASP:' + str(dos_integral['VASP']))
print('VASP/FHI' + str(dos_integral['VASP'] / dos_integral['FHI']))
