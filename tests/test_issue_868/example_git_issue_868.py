#%%
import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import integrate

# set constants
ev_to_joule = 1.602177e-19
window = 100
prefix = '/home/nathan/Documents/electronic-parsers/tests/trace_spinrenormalization/'
example_files = ('fhi', 'vasp')
#%%
# read in data and store it in a dataframe or a dictionary
df = pd.DataFrame({})
normalization_factors = {}

for filename in example_files:
    program = filename.upper()
    fp = open(prefix + filename + '.json')
    data = json.load(fp)
    dos = data['run'][0]['calculation'][0]['dos_electronic'][0]
    fp.close()
    n_entries = len(dos['total'][0]['value'])
    marked_steps = int(n_entries / 1000)  # WARNING: parameter might need adjusting
    df['d' + program] = [x for i, x in enumerate(dos['total'][0]['value']) if (i % marked_steps) == 0]
    df['r' + program] = df['d' + program].rolling(window).mean().fillna(0)
    df['e' + program] = [x for i, x in enumerate(dos['energies']) if (i % marked_steps) == 0]
    df['e' + program] = df['e' + program] - dos['energy_fermi']
    normalization_factors[program] = dos['total'][0]['normalization_factor']
#%%
fig_fhi = px.line(df, x='eFHI', y='dFHI')
fig_vasp = px.line(df, x='eVASP', y='dVASP')
fig = go.Figure(data=fig_fhi.data + fig_vasp.data)
fig.show()

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
#%%
# Select comparison energy range
trimmed_axis = df.loc[(df['rVASP'] > 1e-10) & (df['rFHI'] > 1e-10), ['eFHI', 'eVASP']].dropna(axis=0)
lower = trimmed_axis.min().min()
upper = trimmed_axis.max().max()

# Define a common energy axis, bin the dos and average over bin
df['energy'] = pd.Series(np.linspace(lower, upper, df.shape[0]))
for filename in example_files:
    program = filename.upper()
    temp = [df.loc[(x < df['e' + program]) & (df['e' + program] < y), 'r' + program].tolist()
            for x, y in zip(df['energy'], df['energy'].shift(-1))]
    df['s' + program] = pd.DataFrame(temp).mean(axis=1, skipna=True)

# Compute and plot ratio
df['VASP/FHI'] = df['sVASP']/df['sFHI']
df_plot = df.dropna()
fig = px.line(df_plot, 'energy', 'VASP/FHI')
normalization_ratio = normalization_factors['VASP'] / normalization_factors['FHI']
fig.add_trace(go.Scatter(x=[df_plot['energy'].min(), df_plot['energy'].max()],
              y=[normalization_ratio, normalization_ratio], name='norm_factor ratio'))
fig.show()
#%%
dos_integral = {}
for filename in example_files:
    program = filename.upper()
    dos_integral[program] = integrate.trapz(df.loc[df['e' + program] < 0, 'd' + program], df.loc[df['e'+program] < 0, 'e'+program])
print(dos_integral['FHI'], dos_integral['VASP'], dos_integral['VASP'] / dos_integral['FHI'])
#%%
df
# %%