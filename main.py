import ons


val = ons.gdp.get_gdp()
print(val)

val = ons.gdp.get_infl_from_gdp(val)
print(val)

print(ons.__version__)
