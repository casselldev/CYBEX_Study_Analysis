# Description: Runs ANOVA tests on parametric data from the CYBEX-P user
#              study. Also optionally runs post-hoc pairwise t-tests.
#              Pingouin functions are used for this analysis.

import numpy as np
import pandas as pd
import pingouin as pg

# This script is grouped by dataset. Only one dataset is intended to be used
# at a time. For significant data, additional data_post dataframes are used
# for the poc-hoc tests and include the additional 'Participant' column.

# Read in select event dataset
df = pd.read_csv('ANOVA_selects.csv')
# Select just small graph select data
# ***This one is significant
data = df[["small_size","small_color","small_colorAndSize"]]
data_post = df[["Participant","small_size","small_color","small_colorAndSize"]]
# Select large graph select data
#data = df[["large_size","large_color","large_colorAndSize"]]


# Read in task hover event dataset
# df = pd.read_csv('ANOVA_hovers.csv')
# Select just small graph
# data = df[["small_size","small_color","small_colorAndSize"]]
# Select large graph
# data = df[["large_size","large_color","large_colorAndSize"]]

# Read in task completion time dataset
# df = pd.read_csv('ANOVA_time.csv')
# Select just small graph
# ***This one approaches significance
# data = df[["small_size","small_color","small_colorAndSize"]]
# Select large graph
# data = df[["large_size","large_color","large_colorAndSize"]]

# Read in total interactions time dataset
# ***These all fail significance
# df = pd.read_csv('ANOVA_interactions.csv')
# Select just small graph
# This one approaches significance
# data = df[["small_size","small_color","small_colorAndSize"]]
# Select large graph
# data = df[["large_size","large_color","large_colorAndSize"]]

# Run the repeated-measures ANOVA (because this is within-subjects)
aov = pg.rm_anova(data, detailed=True)
pg.print_table(aov)
#print(aov)


# Dataset must be expressed in long format for the pairwise t-tests:
melted = pd.melt(
    data_post, 
    id_vars=['Participant'], 
    value_vars=["small_size","small_color","small_colorAndSize"], 
    var_name='condition'
)

post_hocs = pg.pairwise_ttests(dv='value', within='condition', subject='Participant', data=melted)
post_hocs.round(3)
pg.print_table(post_hocs)