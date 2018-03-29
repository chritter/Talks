
# coding: utf-8

# # <center> Jupyter Notebooks in Action </center>
# <center> Christian Ritter </center>
# <center> critter@uvic.ca </center>
# 
# <center> Notebooks @ https://github.com/chritter/Talks/blob/master/VicPiMakers </center> 
# 

# ## Setting up Jupyter

# * Notebook server start with `jupyter notebook`
# * Jupyter Notebook App starts dashboard
# * Port of choice 
# * separate configuration files
# * GUI through browser
# * Notebooks are in JSON format and human readable (metadata editable)
# * Configuration: jupyter_notebook_config.py
# * Support:
#     * Chrome
#     * Safari
#     * Firefox
# 

# In[30]:


get_ipython().magic('connect_info')


# ## Standard capabilities

# ### Basic Python

# * Only execution of one cell at a time
# * Serves as analysis, analytics platform but not for software development
# * Basic cell types are code cells and markdown cells 

# In[47]:


a = 3
print(a)


# Standard markdown Markdown
# * Test
# `Test`
# ***Test***
# 
# and Latex
# 
# $\int_0^3 x^2 dx$

# In[32]:


import pandas as pd
pd.DataFrame({'aa':[1,2,3],'bb':[2,3,4]})


# ### Plotting

# * Supports standard plotting capabilities of Python
# * Supports different backends such as the interactive `nbagg` backend

# In[33]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib nbagg')


# In[34]:


plt.plot([1,2,3],[2,2,1])
plt.savefig('line_plot.png')


# rendering images
# ![title](line_plot.png)

# ### Converting to other formats

# * Use GUI `File` tab
# * Command line via `nbconvert`

# In[35]:


get_ipython().run_cell_magic('bash', '', 'jupyter nbconvert CapabilityDemos.ipynb --to python  #--to pdf')


# ### Processing kernels

# * A variety of kernels allow to run Python2/3, Bash, R, Scala: https://github.com/jupyter/jupyter/wiki/Jupyter-kernels
# * `Kernel` menu

# * [RNotebook.ipynb](RNotebook.ipynb)

# ### Shell commands

# In[46]:


get_ipython().system('ls')


# ### Notebook magic

# In[37]:


get_ipython().run_cell_magic('time', '', '#Other magic commands available:\na = [i for i in range(1000000)]')


# Default kernel for notebook plus kernel can be switched via magic commands

# ### Executing external code

# In[38]:


get_ipython().magic('run utils.py')


# In[39]:


test_func()


# ### Security

# * Trusted notebooks: signature in notebook metadata ensures safe execution
# 
#     `jupyter trust mynotebook.ipynb`
# 
# * Password protection through jupyter_notebook_config.py

# In[40]:


#from notebook.auth import passwd
#passwd()


# ### Workflow

# * Create notebook/project (github?)
# * Create reproducable analysis (beware of random numbers)
# * Add layouts, organization
# * Publish/Share

# ### Deploying Notebooks

# * Viewer for notebooks @ https://nbviewer.jupyter.org/
# * Run your own Jupyter server in the cloud. 
# * Rendering on GitHub

# ### Presenting results
# 
# * https://damianavila.github.io/RISE/
# * https://github.com/Anaconda-Platform/nbpresent#install

# ### Reading from other Jupyter notebooks

# Disadvantage: Notebooks are typically separate workflows.

# In[41]:


import json


# In[42]:


f1 = open('DependA.ipynb')
lines=f1.readlines()
f1.close()

str_dum = ''
for l in lines:
    str_dum +=l


# In[43]:


d = json.loads(str_dum)


# In[44]:


d['cells']


# In[45]:


for cell in d['cells']:
    if len(cell['source'])>0:
        if 'velocity' in cell['source'][-1]:
            print(cell['outputs'][0]['data']['text/plain'])


# ## Adding other content

# In[9]:


from IPython.display import YouTubeVideo


# In[11]:


#https://www.youtube.com/watch?v=Iuj9vLOvVJo
YouTubeVideo("Iuj9vLOvVJo")


# ### Widgets

# * Interactive widgets (buttons, levels etc.) at http://jupyter.org/widgets
# * Easy integration with existing code, e.g. functions

# In[24]:


from ipywidgets import interactive
def myfunction(x):
    return x
w = interactive(myfunction, x= "Hello World ");
from IPython.display import display
display(w)


# * Building complex widgets: http://nugrid.github.io/NuPyCEE/webinterface.html

# In[ ]:





# ### Notebook Extensions
# * Community adds new extensions
# * Many extensions available but beware of compatibility

# In[ ]:




