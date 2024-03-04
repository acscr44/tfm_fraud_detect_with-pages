import streamlit as st




st.markdown("""
```python
# Mapa de calor para observar la correlaciones de los datos
f, (ax) = plt.subplots(1, figsize=(24,20))
sub_sample_corr = ccdf.corr()
sns.heatmap(sub_sample_corr, cmap='coolwarm_r')
plt.show()
```
""", unsafe_allow_html=True)